import discord

intents = discord.Intents.default()

intents.message_content = True
intents.messages = True

def create_client():
    client = discord.Client(intents = intents)
    return client