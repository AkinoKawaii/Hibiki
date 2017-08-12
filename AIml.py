import discord

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('how are you'):
        await client.send_message(message.channel,"""Im fine""")
		
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzMzMDgxMjEyMDY1Mjg0MDk2.DGhzpQ.1aGHRakWrOz-MMDk6i5m6KsJ7ag')
