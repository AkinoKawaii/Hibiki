import discord

client = discord.Client()

@client.event
async def on_message(message)
if message.content.startswith('hi'):
        await client.send_message(message.channel,"Hello")

@client.event
async def on_message(message):
   if message.content.startswith('how are you'):
        await client.send_message(message.channel,"Im fine, and you?")

@client.event
async def on_message(message):
   if message.content.startswith('Im good'):
        await client.send_message(message.channel,"Nice")


@client.event
async def on_message(message):
    if message.content.startswith('good morning'):
        await client.send_message(message.channel,"Good morning")

@client.event
async def on_message(message):
   if message.content.startswith('good evening'):
        await client.send_message(message.channel,"Good evening")

@client.event
async def on_message(message):
    if message.content.startswith('good afternoon'):
        await client.send_message(message.channel,"Good Afternoon")

@client.event
async def on_message(message):
   if message.content.startswith('good night'):
        await client.send_message(message.channel,"Good Night")


@client.event
async def on_message(message):
   if message.content.startswith('what are you doing'):
        await client.send_message(message.channel,"I always stay online, and always ready to play music")

@client.event
async def on_message(message):
    if message.content.startswith('how old are you'):
        await client.send_message(message.channel,"Im 15 years old in human age")

@client.event
async def on_message(message):
  if message.content.startswith('who are you'):
        await client.send_message(message.channel,"Im Hibiki A.I Bot")

@client.event
async def on_message(message):
   if message.content.startswith('whats your name'):
        await client.send_message(message.channel,"My name is Hibiki Desu!")


@client.event
async def on_message(message):
   if message.content.startswith('where do you live'):
        await client.send_message(message.channel,"I live in Internet")


@client.event
async def on_message(message):
   if message.content.startswith('lol'):
        await client.send_message(message.channel,"what you are laughing for?")

		
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzMzMDgxMjEyMDY1Mjg0MDk2.DGhzpQ.1aGHRakWrOz-MMDk6i5m6KsJ7ag')
