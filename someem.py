import re
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('cmd'):
        em=discord.Embed(description='commands')
        embed.set_image(url='https://raw.githubusercontent.com/AkinoKawaii/Hibiki/master/command.jpeg')
        await client.send_message(message.channel,embed=em)
