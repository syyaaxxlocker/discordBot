import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
TOKEN: str = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online!')

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())
