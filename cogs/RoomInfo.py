import discord
import os
from discord.ext import commands
from datetime import datetime

class RoomInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is loaded!')

    @commands.command()
    async def get_room_info(self, ctx):
        PROFILE_NAME = os.getenv('USERPROFILE')
        ROOM_INFO_DIR = PROFILE_NAME + "\\Documents\\GTA San Andreas User Files\\SAMP\\room_info.txt"

        with open(ROOM_INFO_DIR, 'r') as file:
            lines = file.readlines()

        header = lines[0]
        
        info_embed = discord.Embed(title='Список арендаторов', description=header, color=discord.Color.green())

        renters = ''.join(
            f"{i + 1}. {line}".replace('\t', ' ')
           .replace(' $', '$')
           .replace('[ ', '[')
           .replace(' ]', ']')
            for i, line in enumerate(lines[1:][:-1])
        )

        info_embed.add_field(name='', value=f'```{renters}```', inline=False)
        info_embed.timestamp = datetime.utcnow()
        info_embed.set_footer(text=f'Request by {ctx.author.name}', icon_url=ctx.author.avatar)
        
        await ctx.send(embed=info_embed)

async def setup(bot):
    await bot.add_cog(RoomInfo(bot))