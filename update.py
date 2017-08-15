import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel,":thumbsup:")
#your things here.............................................................................

@client.event#copy this section only
async def on_member_update(before, after):
        server = after.server
        member = after
        if before.name != after.name:
            embed = discord.Embed(description='From {0.name} ({0.id}) to {1.name}'.format(before, after))
            embed.set_author(name='Name changed', icon_url=server.icon_url)
            await client.send_message(after.server, embed=embed)
        if before.nick != after.nick:
            embed = discord.Embed(description='From {0.nick} ({0.id}) to {1.nick}'.format(before, after))
            embed.set_author(name='Nickname changed', icon_url=server.icon_url)
            await client.send_message(after.server, embed=embed)
        if before.roles != after.roles:
            if len(before.roles) > len(after.roles):
                for role in before.roles:
                    if role not in after.roles:
                        embed = discord.Embed(description='{0.display_name} ({0.id}) lost the {1.name} role'.format(before, role))
                        embed.set_author(name='Role removed', icon_url=server.icon_url)
                        await client.send_message(after.server, embed=embed)
            elif len(before.roles) < len(after.roles):
                for role in after.roles:
                    if role not in before.roles:
                        embed = discord.Embed(description='{0.display_name} ({0.id}) got the {1.name} role'.format(before, role))
                        embed.set_author(name='Role applied', icon_url=server.icon_url)
                        await client.send_message(after.server, embed=embed)
