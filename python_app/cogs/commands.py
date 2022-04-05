import os
import discord
from discord.ext import commands
from discord.commands import Option
from cogs import crud, schemas, embed_msg
from cogs.db import SessionLocal
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)
command_guilds = [
    785157404161081374
    ]

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('commands')
    
    @commands.slash_command(description='にゃっはろ～!!', guild_ids=command_guilds)
    async def nyahello(self, ctx: discord.ApplicationContext, name: Option(str, '名前を入力して下さい', default=None)):
        name = name or ctx.author.name
        try:
            await ctx.respond(f'{name}さん、にゃっはろ～!!')
        except Exception as e:
            self.logger.error(e)
            
    @commands.slash_command(description='みこちのチャンネル内にある配信/動画/スペースの情報を表示します', guild_ids=command_guilds)
    async def eb_serch_video(
        self,
        ctx: discord.ApplicationContext,
        platform: Option(str, 'プラットフォームを選択してください', choices=['YouTube', 'Twitch', 'Twitter'], default='YouTube'),
        id: Option(str, '配信/動画/スペースのIDを入力してください')
        ):
        pass
        #with SessionLocal as db:
        #    if platform == 'YouTube':
        #        data = crud.get_ytvideo(db, id)
        #        embed = embed_msg.ytvideo_info(data)
        #    elif platform == 'Twitch':
        #        data = crud.get_tcstream(db, id)
        #        embed = embed_msg.twitch_embed(id)
        #    elif platform == 'Twitter':
        #        data = crud.get_twspace(db, id)
        #        embed = embed_msg.twitter_embed(id)
        
        #try:
        #    await ctx.respond(embed=embed)
        #except Exception as e:
        #    self.logger.error(e)

    
        
def setup(bot):
    return bot.add_cog(Commands(bot))