import discord
import asyncio
import hibi3
import someem
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
print('Starting....')
client.run('MzMzMDgxMjEyMDY1Mjg0MDk2.DRs-OA.inWxGr07ZiJmOTVsAvMKiuYyRwU')

