import discord
import asyncio
import aiohttp
import json
import os
import time
from discord.ext import tasks, commands
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)


class APITasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('api_tasks')
        self.api_base = os.environ.get("API_URL")
        self.youtube_channel = {}
        self.youtube_data.start()

    def cog_unload(self):
        self.youtube_data.cancel()
        

    @tasks.loop(seconds=5)
    async def youtube_data(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_base}/youtube/") as resp:
                if resp.status != 200:
                    self.logger.error("API connection failed.")
                    return
                self.youtube_channel = await resp.json()
                
    
        
            
            
            
                
                
        
        
    @youtube_data.before_loop
    async def wait_api_tasks(self):
        await self.bot.wait_until_ready()
        self.logger.info('API tasks start waiting...')
        

def setup(bot):
    return bot.add_cog(APITasks(bot))