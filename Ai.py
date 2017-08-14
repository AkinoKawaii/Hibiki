import discord
import asyncio
import re

@client.event
async def on_message(message):
    random_color = colors()
 #   if message.content.startswith('=ok'):
     #   await client.send_message(message.channel,'ok')
    
      if message.content.startswith('hello'):
         await client.send_message(message.channel,"Hi Im Hibiki")
            
    elif message.content.startswith('how are you'):
        await client.send_message(message.channel,"Im fine, and you?")
     
    elif message.content.startswith('Im good'):
        await client.send_message(message.channel,"Nice")
        
    elif message.content.startswith('good morning'):
        await client.send_message(message.channel,"Good morning")
        
    elif message.content.startswith('good evening'):
        await client.send_message(message.channel,"Good evening")
        
    elif message.content.startswith('good afternoon'):
        await client.send_message(message.channel,"Good Afternoon")
        
    elif message.content.startswith('good night'):
        await client.send_message(message.channel,"Good Night")
        
    elif message.content.startswith('what are you doing'):
        await client.send_message(message.channel,"I always stay online, and always ready to play music")
        
    elif message.content.startswith('how old are you'):
        await client.send_message(message.channel,"Im 15 years old in human age")
        
    elif message.content.startswith('who are you'):
        await client.send_message(message.channel,"Im Hibiki A.I Bot")
        
    elif message.content.startswith('whats your name'):
        await client.send_message(message.channel,"My name is Hibiki Desu!")
    
    elif message.content.startswith('where do you live'):
        await client.send_message(message.channel,"I live in Internet")
        
    elif message.content.startswith('lol'):
        await client.send_message(message.channel,"what you are laughing for?")
        
    elif message.content.startswith('Im fine too'):
        await client.send_message(messsage.channel,"Im glad to hear that")
    
    elif message.content.startswith('can you'):
        await client.send_message(message.channel,"Sure ;D")
        
    elif message.content.startswith('what do you think'):
        await client.send_message(message.channel,"hmm, let me think first")
        
    elif message.content.startswith('hi'):
        await client.send_message(message.channel,"heyyooo")
        
    elif message.content.startswith('anyone'):
        await client.send_message(message.channel,"Im here")
        
    elif message.content.startswith('Im bored'):
        await client.send_message(message.channel,"Why??")
        
    elif message.content.startswith('what time is it'):
        await client.send_message(message.channel,"sorry we are in different region")
        
    elif message.content.startswith('can I'):
        await client.send_message(message.channel,"sure")
        
    elif message.content.startswith('help'):
        await client.send_message(message.channel,"what can i do for u?")
    
    elif message.content.startswith('I will'):
        await client.send_message(message.channel,"Really?")
        
    elif message.content.startswith('really'):
        await client.send_message(message.channel,"yes")
        
    elif message.content.startswith('thank you'):
        await client.send_message(message.channel,"ur welcome")
