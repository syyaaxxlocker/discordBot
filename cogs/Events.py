import discord
from discord.ext import commands
from datetime import datetime

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is loaded!')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        log_edit_channel = discord.utils.get(after.guild.channels, name='logs-edited-msg')
        
        event_embed = discord.Embed(title='Сообщение было отредактировано.', description='', color=discord.Color.blue())
        event_embed.add_field(name='До:', value=f"```{before.content}```", inline=False)
        event_embed.add_field(name='После:', value=f"```{after.content}```", inline=False)
        event_embed.add_field(name='Перейти', value=after.jump_url, inline=True)
        event_embed.add_field(name='Автор', value=f'{after.author} - {after.author.mention}', inline=True)
        event_embed.add_field(name='Канал', value=f'{after.channel} - {after.channel.mention}', inline=True)
        event_embed.timestamp = datetime.utcnow()
        event_embed.set_footer(text=f'ID Сообщения: {after.id}')

        await log_edit_channel.send(embed=event_embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        log_edit_channel = discord.utils.get(message.guild.channels, name='logs-deleted-msg')
        
        event_embed = discord.Embed(title='Сообщение было удалено.', description='', color=discord.Color.blue())
        event_embed.add_field(name='Содержимое:', value=f"```{message.content}```", inline=False)
        event_embed.add_field(name='Автор', value=f'{message.author} - {message.author.mention}', inline=True)
        event_embed.add_field(name='Канал', value=f'{message.channel} - {message.channel.mention}', inline=True)
        event_embed.add_field(name='Отправлено в ', value=message.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=True)
        event_embed.timestamp = datetime.utcnow()   
        event_embed.set_footer(text=f'ID Сообщения: {message.id}')

        await log_edit_channel.send(embed=event_embed)



async def setup(bot):
    await bot.add_cog(Events(bot))