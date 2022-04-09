import os
import discord
from discord.ext import commands
from discord.commands import Option
from cogs import crud, schemas, embed_msg
from cogs.db import async_session
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('commands')
    
    @commands.slash_command(guild_ids=[785157404161081374], description='にゃっはろ～!!')
    async def nyahello(self, ctx: discord.ApplicationContext, name: Option(str, '名前を入力して下さい', default=None)):
        name = name or ctx.author.name
        try:
            await ctx.respond(f'{name}さん、にゃっはろ～!!')
        except Exception as e:
            self.logger.error(e)
            
    @commands.slash_command(guild_ids=[785157404161081374], description='みこちのチャンネル内にある配信/動画/スペースの情報を表示します')
    async def eb_serch_video(
        self,
        ctx: discord.ApplicationContext,
        platform: Option(str, 'プラットフォームを選択してください', choices=['YouTube', 'Twitch', 'Twitter']),
        id: Option(str, '配信/動画/スペースのIDを入力してください')
        ):
        try:
            await ctx.respond(f'{platform}の{id}の情報を取得しています...')
        except Exception as e:
            self.logger.error(e)

        
def setup(bot):
    return bot.add_cog(Commands(bot))