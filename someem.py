import re
import asyncio
import discord

@client.event
async def on_message(message):
    if message.content.startswith('cmd'):
        em=discord.Embed(description='test')
        embed.set_author(name='test')
        await client.send_message(message.channel,embed=em)
        
@client.event
async def on_messsage(message):
    if message.content.startswith('null'):
        await client.send_message(message.channel, '0')
