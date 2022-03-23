import discord
import asyncio
import os
from discord.ext import tasks, commands
from cogs import crud, models, schemas
from cogs.db import SessionLocal
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)


class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('notification_tasks')
        self.mikonotice_chid = int(os.environ.get("MIKONOTICE_CHID"))
        self.youtube_notice.start()
    
    def cog_unload(self):
        self.youtube_notice.cancel()


    # YouTube Notice
    @tasks.loop(seconds=5)
    async def youtube_notice(self):
        return

    
    @youtube_notice.before_loop
    async def wait_notification_tasks(self):
        await self.bot.wait_until_ready()
        self.logger.info('Notification tasks start waiting...')
        
def setup(bot):
    return bot.add_cog(Notification(bot))