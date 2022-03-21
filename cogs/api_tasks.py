import asyncio
import aiohttp
import os
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
        self.youtube_videos = []
        self.twitch_channel = {}
        self.twitch_streams = []
        self.twitter_account = {}
        self.twitter_space = []
        
        self.youtube_data.start()
        self.twitch_data.start()
        self.twitter_data.start()

    def cog_unload(self):
        self.youtube_data.cancel()
        self.twitch_data.cancel()
        self.twitter_data.cancel()
    
    # Async HTTP requests
    async def aioget(self, session, url: str, params: dict = None):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        async with session.get(url=self.api_base + url, headers=headers, params=params) as resp:
            if resp.status != 200:
                self.logger.error("API connection failed.", resp.status)
                return
            return await resp.json()
        

    # Get YouTube data.
    @tasks.loop(seconds=5)
    async def youtube_data(self):
        async with aiohttp.ClientSession() as session:
            # Get YouTube channel data.
            request_url = "/youtube/"
            self.youtube_channel = await self.aioget(session, request_url)
            
            # Get YouTube videos data.
            skip = 0
            limit = 35
            while True:
                request_url = "/youtube/videos/"
                params = {
                    'order': 'created_at',
                    'skip': skip,
                    'limit': limit,
                }
                data = await self.aioget(session, request_url, params)
                if data == []:
                    break
                self.youtube_videos.extend(data)
                skip += 35
                limit += 35
                await asyncio.sleep(float(0.2))
                
    
    # Get Twitch data.
    @tasks.loop(seconds=5)
    async def twitch_data(self):
        async with aiohttp.ClientSession() as session:
            # Get Twitch channel data.
            request_url = "/twitch/"
            self.twitch_channel = await self.aioget(session, request_url)
        
            # Get Twitch streams data.
            skip = 0
            limit = 35
            while True:
                request_url = "/twitch/streams/"
                params = {
                    'order': 'created_at',
                    'skip': skip,
                    'limit': limit,
                }
                data = await self.aioget(session, request_url, params)
                if data == []:
                    break
                self.twitch_streams.extend(data)
                skip += 35
                limit += 35
                await asyncio.sleep(float(0.2))
    
    
    # Get Twitter data.
    @tasks.loop(seconds=5)
    async def twitter_data(self):
        async with aiohttp.ClientSession() as session:
            # Get Twitter aount data.
            request_url = "/twitter/"
            self.twitter_account = await self.aioget(session, request_url)
        
            # Get Twitter space data.
            skip = 0
            limit = 35
            while True:
                request_url = "/twitter/space/"
                params = {
                    'order': 'created_at',
                    'skip': skip,
                    'limit': limit,
                }
                data = await self.aioget(session, request_url, params)
                if data == []:
                    break
                self.twitter_space.extend(data)
                skip += 35
                limit += 35
                await asyncio.sleep(float(0.2))

              
    @youtube_data.before_loop
    @twitch_data.before_loop
    @twitter_data.before_loop
    async def wait_api_tasks(self):
        await self.bot.wait_until_ready()
        self.logger.info('API tasks start waiting...')
        

def setup(bot):
    return bot.add_cog(APITasks(bot))