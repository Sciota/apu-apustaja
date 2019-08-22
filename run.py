#!/usr/bin/env python3

#import dipendencies
import os
import sys
import json
import sqlite3
import discord
import asyncio
from datetime import datetime
from discord.ext import commands


description = """hello frens"""
dir_path = os.path.dirname(os.path.realpath(__file__)) #Set working directory to bot's folder
os.chdir(dir_path) #Move to bot's folder
prefixes = commands.when_mentioned_or('apu ') #Set prefix
bot = commands.Bot(command_prefix=prefixes, description=description, pm_help=None)


#Read config
if not os.path.isfile("config.json"):
    sys.exit("Set up your config.json file.")

with open('config.json') as data:
    bot.config = json.load(data)


#initialize db connection
bot.db = sqlite3.connect('main.db')
#create tables for muted members and access roles. Necessary for basic functionality
bot.db.execute('CREATE TABLE IF NOT EXISTS mutes (id integer NOT NULL primary key AUTOINCREMENT, member_id varchar, member_name varchar, mute_time integer, server_id varchar)')
bot.db.execute('CREATE TABLE IF NOT EXISTS roles (id integer NOT NULL primary key AUTOINCREMENT, role_id varchar, role varchar, level int, serverid int)')
bot.db.commit()


#global storages
bot.access_roles = {} #roles
bot.unmute_timers = {} #mutes
bot.server_settings = {} #per server settings


@bot.event
async def on_ready():
    bot.start_time = datetime.today()

    print("{} has started!".format(bot.user.name))
    print("Current time is {}".format(bot.start_time))

    cursor = bot.db.cursor()
    
    for server in bot.guilds:
        bot.access_roles.update({server.id : {}}) #add server to access_role storage
        bot.unmute_timers.update({server.id: {}}) #add server to unmute_timers storage
        bot.server_settings.update({server.id : {'wiki_lang':'eng'}})

        #preload roles in storage
        cursor.execute("SELECT * FROM roles WHERE serverid={}".format(server.id))
        roles_data = cursor.fetchall()
        if roles_data:
            for row in roles_data:
                # row[0] - ID
                # row[1] - role name
                # row[2] - role level
                # row[3] - server id
                bot.access_roles[server.id].update({row[1] : row[3]})
            
        print("Connected to {} with {:,} members.".format(server.name, server.member_count))
    
    cursor.close()

    print("\n\nLoading addons:")
    for extension in bot.config['extensions']:
        try:
            bot.load_extension(extension['name'])
        except Exception as e:
            print('{} failed to load.\n{}: {}'.format(extension['name'], type(e).__name__, e))
    
    print("\n\nAddons loaded successfully.\n\n")
    await bot.change_presence(activity=discord.Game(name='Hello frens | apu help'))


if bot.config['type'] == "user":
    bot.run(bot.config['user_token'], bot=False)
else:
    bot.run(bot.config['token'])