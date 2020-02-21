import discord
import os
import addons.checks as checks
from datetime import datetime
from random import randint
from discord.ext import commands


class Events(commands.Cog):
    """
    Events
    """

    #Construct
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))
    
    #@commands.Cog.listener()
    #async def on_message(self, msg):
    #    if msg.author.id == 329410106523648002 or msg.author.id == 479979609757188096:
    #        await msg.channel.send("Zitto magrebino.")
    #        return

     @commands.Cog.listener()
     async def on_reaction_add(self, reaction, user):
 
         weeb   = '👹'  #:japanese_ogre:                                                   
         hacker = '💻'  #:computer:                                                        
         gamer  = '🕹️   #:joystick:                                                        
 
         roles_msg = await reaction.message.channel.fetch_message(680467368752840721)
         print(roles_msg)
 
         if (reaction.message.channel.id != 680100806791528452):
             print("diocane")
             return
         
         guild = user.guild
 
         if reaction.emoji == hacker and reaction.message == roles_msg:
             roleHacker = guild.get_role(680437984231030801)
             await user.add_roles(roleHacker, reason="Clicked the get-roles button")
             
         if reaction.emoji == weeb  and reaction.message == roles_msg:
             roleWeeb = guild.get_role(680437936214376455)
             await user.add_roles(roleWeeb, reason="Clicked the get-roles button")
 
         if reaction.emoji == gamer and reaction.message == roles_msg:
             roleGamer = guild.get_role(680437915888910405)
             await user.add_roles(roleGamer, reason="Clicked the get-roles button")

     @commands.Cog.listener()
     async def on_reaction_remove(self, reaction, user):
 
         weeb   = '👹'
         hacker = '💻'
         gamer  = '🕹️'
 
         roles_msg = await reaction.message.channel.fetch_message(680467368752840721)
         print(roles_msg)
 
         if (reaction.message.channel.id != 680100806791528452):
             print("diocane")
             return
         
         guild = user.guild
 
         if reaction.emoji == hacker and reaction.message == roles_msg:
             roleHacker = guild.get_role(680437984231030801)
             await user.remove_roles(roleHacker, reason="Clicked the get-roles button")
 
         if reaction.emoji == weeb  and reaction.message == roles_msg:
             roleWeeb = guild.get_role(680437936214376455)
             await user.remove_roles(roleWeeb, reason="Clicked the get-roles button")
 
         if reaction.emoji == gamer and reaction.message == roles_msg:
             roleGamer = guild.get_role(680437915888910405)
             await user.remove_roles(roleGamer, reason="Clicked the get-roles button")
 



def setup(bot):
    bot.add_cog(Events(bot))
