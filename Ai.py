import discord

@client.event
async def on_message(message)
    if message.content.startswith("how are you"):
        msg = "{}".format(Im good and you?)
        await client.send_message(message.channel,msg)
