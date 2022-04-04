import os
from discord.ext import commands
from discord.commands import Option
from cogs import crud, schemas, embed_msg
from cogs.db import SessionLocal
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('commands')
        
    @commands.slash_command(guild_ids=[785157404161081374])
    async def nyahello(self, ctx,
        name: Option(str, '名前を入力してください'),
        gender: Option(str, '性別を選択してください', choices=['男性', '女性', 'その他']),
        age: Option(int, '年齢を入力してください', required=False, default=18),
    ):
        await ctx.respond(f'{name}さん、にゃっはろ～!!')
        
def setup(bot):
    return bot.add_cog(Commands(bot))