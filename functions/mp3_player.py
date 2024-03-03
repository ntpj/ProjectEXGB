import youtube_dl
import subprocess
import os
from logMsg import log
from datetime import datetime

def audio_check(directory):
    for file in os.listdir(directory):
        if file.endswith(".mp3") or file.endswith(".webm"):
            music = f"cache_sound_{datetime.now()}.webm"
            os.rename(file, music)
            print('Name changed')
            return music
    return None

def audio_dl(url):
    log("Youtube MP3 Downloaded")
    command = f'yt-dlp --extract-audio --audio-format mp3 {url}'
    process = subprocess.run(command, capture_output=True, text=True, shell=True)
    audio_check("./functions")
    
# For testing
if False:
    audio_dl('https://www.youtube.com/watch?v=c3VzXwKiKYg&ab_channel=LuckFast')