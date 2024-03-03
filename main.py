# %% Imports

import os
import traceback
import sys

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
# from discord_slash import SlashCommand
import asyncio
import youtube_dl
import pickle
from dotenv import load_dotenv

sys.path.append('./functions')
from functions.mp3_player import audio_check
from functions.logMsg import log, logtb
from exgbClass import user

# %% Start 
##### Start 
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

##### Event
@bot.event
async def on_ready():
    log(f'Logged in as {bot.user}')


# %% Function

    # KJ's Note: 
''' I want to check profile of the one who got @ instead of the user who calls the function,
    in this case, default is still user's (caller's) profile.
    It's still nto done tho so gl
'''

@bot.event
async def on_message(message):
    if '@' not in message.content:
        user.data = message
        user.id = message.author.id
        user.name = message.author.name
        user.avatar = message.author.avatar
        user.global_name = message.author.global_name
    elif '@' in message.content:
        data = await bot.fetch_user(message)
        user.data = data
        user.id = data.id
        user.name = data.name
        user.avatar = data.author.avatar
        user.global_name = data.author.global_name
        print(data)

    if message.content.startswith('!'):
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
   
   
   # KJ's Note
''' Still need some more debugging and feature to check if user is in the channel or not, 
    then let the bot join/leave accordingly'''
@bot.command()     
async def play(ctx, url):
    try:
        voice_state = ctx.author.voice
        if voice_state is None:
            await ctx.send("You need to be in a voice channel to use this command.")
        else:
            voice_channel = ctx.author.voice.channel
            if voice_channel:
                music = audio_check(url)
                vc = await voice_channel.connect()
                vc.play(discord.FFmpegPCMAudio(music))
                os.remove(music)
    except:
        await ctx.send("Error")
        await ctx.send(f"```{traceback.format_exc()}```")
        logtb(traceback.format_exc())


@bot.command() # Not working
async def leave(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client:
        await voice_client.disconnect()
        
        
@bot.command()
async def pinfo(ctx, type: str='short'): # Return information of the user (extracted from message/user fetch)
    if type == "short":
        await ctx.send(f"```UID : {user.id}\nName: {user.name}\nAlias: {user.global_name}```{user.avatar}")
    elif type == "msg_data":
        await ctx.send(f"```Message data:\n{user.data}```")
        
        
@bot.command()
async def cache()

# %% Main

# Test command
@bot.command(name="ping")
async def ping(ctx):
    log("Reply to ping")
    await ctx.send("OK")

if __name__ == "__main__":
    user = user()
    bot.run(TOKEN)