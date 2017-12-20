import discord
import asyncio
import hibi3
client = discord.Client()
@client.event
async def on_message(message):
    if message.content.startswith('cmd'):
        embed=discord.Embed(color=0x00ce5c)
        embed.set_author(name='Command List',icon_url='https://raw.githubusercontent.com/AkinoKawaii/Hibiki/master/hibiki-2.png')
        embed.add_field(name='user', value='User info', inline=False)
        embed.add_field(name='say', value='Repeat your words', inline=False)
        embed.add_field(name='Invite', value='Send Invite(bot) link', inline=False)
        embed.add_field(name='Hibiki', value='Talk with hibiki', inline=False)
        embed.add_field(name='hsummon', value='Hibiki will connected in your #VoiceChannel', inline=False)
        embed.add_field(name='hplay', value='Request music', inline=False)
        embed.add_field(name='hnp', value='Show playing music', inline=False)
        embed.add_field(name='hqueue', value='Show the queue', inline=False)
        embed.add_field(name='hshuffle', value='Shuffle the song', inline=False)
        embed.add_field(name='hpause', value='pause the song', inline=False)
        embed.add_field(name='hresume', value='resume the paused song', inline=False)
        embed.add_field(name='hskip', value='to skip song', inline=False)
        embed.add_field(name='hvolume', value='set the volume (5~100)', inline=False)
        embed.add_field(name='hsearch', value='searching the song #YouTube', inline=False)
        embed.add_field(name='hdisconnect', value='disconnect Hibiki from #VoiceChannel', inline=False)
        embed.set_footer(text='made by OnikaStudio')
        embed.set_image(url='https://raw.githubusercontent.com/AkinoKawaii/Hibiki/master/music.png')
        await client.send_message(message.channel,embed=embed)
        
client.run('MzMzMDgxMjEyMDY1Mjg0MDk2.DRs-OA.inWxGr07ZiJmOTVsAvMKiuYyRwU')
