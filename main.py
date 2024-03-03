import os
import traceback
import sys

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
from dotenv import load_dotenv

sys.path.append('./functions')
from functions.mp3_player import audio_check
from functions.logMsg import log, logtb
load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Online check
@bot.event
async def on_ready():
    log(f'Logged in as {bot.user}')
    
  
# %% Functions
if True: # Not working
    @bot.command(name='play')
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

    # Test command
    @bot.command(name="ping")
    async def ping(ctx):
        log("Reply to ping")
        await ctx.send("OK")

# %% Run

if __name__ == "__main__":
    bot.run(TOKEN)