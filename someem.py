import re
import asyncio
import discord
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('cmd'):
        em=discord.Embed(description='commands')
        embed.set_author(name='test')
        await client.send_message(message.channel,embed=em)
