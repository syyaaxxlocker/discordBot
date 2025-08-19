import discord
import os, time
from discord.ext import commands
from datetime import datetime

class RoomInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is loaded!')

    @commands.command()
    async def renters(self, ctx):
        PROFILE_NAME = os.getenv('USERPROFILE')
        ROOM_INFO_DIR = PROFILE_NAME + "\\Documents\\GTA San Andreas User Files\\SAMP\\room_info.txt"
        try:
            with open(ROOM_INFO_DIR, 'r') as file:
                lines = file.readlines()

            header = lines[0]
            renters = ''.join(
                f"{i + 1}. {line}".replace('\t', ' ')
            .replace(' $', '$')
            .replace('[ ', '[')
            .replace(' ]', ']')
                for i, line in enumerate(lines[1:][:-1])
            )
            last_update = datetime.fromtimestamp(os.path.getmtime(ROOM_INFO_DIR)).strftime('%Y-%m-%d %H:%M:%S')

            info_embed = discord.Embed(title='Список арендаторов', description=header, color=discord.Color.green())
            info_embed.add_field(name='', value=f'```{renters}```', inline=False)
            info_embed.add_field(name='Дата последнего обновления', value=last_update, inline=False)
            info_embed.timestamp = datetime.utcnow()
            info_embed.set_footer(text=f'Request by {ctx.author.name}', icon_url=ctx.author.avatar)
            
            await ctx.send(embed=info_embed)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(RoomInfo(bot))