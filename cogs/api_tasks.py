import discord
import asyncio
import aiohttp
import os
import time
from discord.ext import tasks, commands

api_base = os.environ.get("API_URL")


class APITasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_tasks.start()

    def cog_unload(self):
        self.api_tasks.cancel()
        
    @tasks.loop(seconds=5)
    async def api_tasks(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api_base}/youtube/") as resp:
                if resp.status != 200:
                    return
                
                
        
        
    @api_tasks.before_loop
    async def wait_api_tasks(self):
        print('tasks start waiting...')
        await self.bot.wait_until_ready()
        

def setup(bot):
    return bot.add_cog(APITasks(bot))