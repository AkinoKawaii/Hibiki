import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('how are you'):
        await client.send_message(message.channel,"""Im fine""")
		
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzMzMDgxMjEyMDY1Mjg0MDk2.DGhzpQ.1aGHRakWrOz-MMDk6i5m6KsJ7ag')
