import asyncio
import discord
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('cmd'):
        em=discord.Embed(description='test')
        em.set_author(name='test')
        await client.send_message(message.channel,embed=em)
        
@client.event
async def on_messsage(message):
    if message.content.startswith('null'):
        await client.send_message(message.channel, '0')
        
