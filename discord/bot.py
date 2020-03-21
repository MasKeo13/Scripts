# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, How\'r now?'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    wayne_quotes = [
        'Fuck Lemony Snicket, what a serious of unfortunate events you fuckin been through you ugly fuck.',
        'Pitter patter, let\’s get at \‘er.',
        'Give yer balls a tug.',
        'YEW!',
        'What sort of backwards fucking padgentry is that?',
        'You going to fight with those shades or play pokerstars.com',
        'I wish you weren\’t so fucking awkward, bud.',
        'Does a duck with a boner drag weeds?',
        'Hard no.',
        'Not my pig, not my farm.',
        'You\’re made of spare parts, aren\’t you, bud?',
        'You\'re 10 ply.'
    ]

    if message.content == '!letter':
        response = random.choice(wayne_quotes)
        await message.channel.send(response)

    if message.content == 'How\'r ya now?':
        answer ='Good\'n you?'
        await message.channel.send(answer)


client.run(TOKEN)

