import yaml


import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
#aldığımız bilgiler dosyaya gelir 
import logging 



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


token = yaml.safe_load(open("denem.yaml"))["token"]
print(token)



@client.event
async def on_ready():
    all_channels = client.get_all_channels()


    members = set()

    for channel in all_channels:
        channel_members = channel.guild.members
        for member in channel_members:
            if member != client.user:
              members.add(member)


    for member in members:
        await member.send("Merhaba sunucumuza hoşgeldiniz ben botunuz HCT ")

    genel = client.get_channel(938952909771657299)
    await genel.send("GENEL KANAALINA HOŞGELDİNİZ")

    deneme = client.get_channel(940760484972470302)
    await deneme.send("DENEME KANALINA HOŞGELDİNİZ")

    for channel in all_channels:
        if str(channel.type) == "text":
            await channel.send("BU HER METİN KANALINA GÖNDERİLEN GENEL BİR MESAJDIR")
    # kullanıcıdan gelen mesajları terminalde bize verir
    async def on_message(self, message):
        print(f"{message.author}: {message.content} channel : {message.channel}")

@client.event
async def on_message(message):

    if message.content.startswith('!topla '):
        command = message.content.split()[0]
        params = message.content.split('!topla')[1].split()
        toplam = sum(map(int, params))

        title = "TOPLAM"
        description = "+".join(params) + "="+ str(toplam)
        color = discord.Colour.red()
        embed= discord.Embed(title=title,description=description,colour=color)

        await message.channel.send(embed=embed)


client.run(token)