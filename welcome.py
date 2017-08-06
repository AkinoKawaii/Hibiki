import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('MzMzMDgxMjEyMDY1Mjg0MDk2.DGhtbg.qdzFSqklMQ9LfBRU2fN5mF25S1o')
