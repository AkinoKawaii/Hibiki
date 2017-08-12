import discord

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

   elif message.content.startswith('how are you'):
        msg = 'Im good and you?'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Im good'):
	msg = 'nice'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('good morning'):
	msg = 'Good morning'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('goodevening'):
	msg = 'Good evening'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('good afternoon'):
	msg = 'Good afternoon'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('good night'):
	msg = 'Good night'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('what are you doing'):
	msg = 'Im always stay online, and playing music'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('how old are you'):
	msg = 'Im 15 years old in human age'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('who are you')
	msg = 'Im Hibiki A.I Bot'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('whats your name')
	msg = 'my name is Hibiki Desu!'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('where do you live')
	msg = 'Im AI so I live in Internet'.format(message)
	await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('lol')
	msg = 'what are you laugh for?'.format(message)
	await client,send_message(message.channel, msg)
		
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzMzMDgxMjEyMDY1Mjg0MDk2.DGhzpQ.1aGHRakWrOz-MMDk6i5m6KsJ7ag')
