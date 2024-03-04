import interactions
import os
from dotenv import load_dotenv
TOKEN = os.getenv('TOKEN')

bot = interactions.Client(token=TOKEN)

@interactions.slash_command(
    name="ping",
    description="Ping command"
)
async def ping(ctx: interactions.ComponentContext):
    await ctx.send("Pong!")

# Replace YOUR_DISCORD_TOKEN with your actual Discord bot token
bot.start()