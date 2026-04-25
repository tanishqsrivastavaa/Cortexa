import os
from dotenv import load_dotenv
from bot.client import create_client
from bot.handlers import format_message

load_dotenv()

client = create_client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    
    if message.author.bot:
        return

    event = format_message(message)

    print(event)  

client.run(os.getenv("DISCORD_TOKEN"))