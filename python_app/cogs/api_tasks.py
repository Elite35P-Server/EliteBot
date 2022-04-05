import asyncio
import aiohttp
import os
from discord.ext import tasks, commands
from cogs import async_crud, schemas
from cogs.db import async_session
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)

class APITasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('api_tasks')
        self.api_base = os.environ.get('API_URL')
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
                self.logger.error('API connection failed.', resp.text)
                return
            return await resp.json()
        

    # Get YouTube data.
    @tasks.loop(seconds=5)
    async def youtube_data(self):
        async with aiohttp.ClientSession() as session:
            # Get YouTube channel data.
            request_url = "/youtube/"
            youtube_channel = await self.aioget(session, request_url)
            if youtube_channel:
                ch = schemas.YouTubeCh(
                    id=youtube_channel['id'],
                    name=youtube_channel['name'],
                    icon=youtube_channel['icon'],
                    description=youtube_channel['description'],
                    subsc_count=youtube_channel['subsc_count'],
                    play_count=youtube_channel['play_count'],
                    video_count=youtube_channel['video_count'],
                    updated_at=youtube_channel['updated_at'],
                    status=youtube_channel['status'],
                    #videos = [],
                )
                #print(ch)
                async with async_session() as db:
                    try:
                        await async_crud.update_ytch(db=db, ch=ch)
                    except Exception as e:
                            self.logger.error(e)
            
            # Get YouTube videos data.
            skip = 0
            limit = 35
            request_url = "/youtube/videos/"
            async with async_session() as db:
                while True:
                    params = {
                        'order': 'created_at',
                        'skip': skip,
                        'limit': limit,
                    }
                    data = await self.aioget(session, request_url, params)
                    if data == []:
                        break
                    for video in data:
                        youtube_video = schemas.YouTubeVideo(
                            id=video['id'],
                            title=video['title'],
                            thumbnails=video['thumbnails'],
                            description=video['description'],
                            url=video['url'],
                            play_count=video['play_count'],
                            like_count=video['like_count'],
                            comment_count=video['comment_count'],
                            status=video['status'],
                            current_viewers=video['current_viewers'],
                            ss_time=video['ss_time'],
                            as_time=video['as_time'],
                            ae_time=video['ae_time'],
                            updated_at=video['updated_at'],
                            created_at=video['created_at'],
                        )
                        #print(youtube_video)
                        try:
                            await async_crud.update_ytvideo(db=db, ch_id=youtube_channel['id'], video=youtube_video)
                        except Exception as e:
                            self.logger.error(e)
                    skip += 35
                    limit += 35
                    await asyncio.sleep(float(0.2))
                
    
    # Get Twitch data.
    @tasks.loop(seconds=5)
    async def twitch_data(self):
        async with aiohttp.ClientSession() as session:
            # Get Twitch channel data.
            request_url = "/twitch/"
            twitch_channel = await self.aioget(session, request_url)
            if twitch_channel:
                ch = schemas.TwitchCh(
                    id=twitch_channel['id'],
                    display_id=twitch_channel['display_id'],
                    name=twitch_channel['name'],
                    icon=twitch_channel['icon'],
                    offline_img=twitch_channel['offline_img'],
                    description=twitch_channel['description'],
                    subsc_count=twitch_channel['subsc_count'],
                    play_count=twitch_channel['play_count'],
                    status=twitch_channel['status'],
                    updated_at=twitch_channel['updated_at'],
                )
                #print(ch)
                async with async_session() as db:
                    try:
                        await async_crud.update_tcch(db=db, ch=ch)
                    except Exception as e:
                            self.logger.error(e)
        
            # Get Twitch streams data.
            skip = 0
            limit = 35
            request_url = "/twitch/streams/"
            async with async_session() as db:
                while True:
                    params = {
                        'order': 'created_at',
                        'skip': skip,
                        'limit': limit,
                    }
                    data = await self.aioget(session, request_url, params)
                    if data == []:
                        break
                    for stream in data:
                        twitch_stream = schemas.TwitchStream(
                            id=stream['id'],
                            title=stream['title'],
                            thumbnail=stream['thumbnail'],
                            description=stream['description'],
                            url=stream['url'],
                            type=stream['type'],
                            game_id=stream['game_id'],
                            game_name=stream['game_name'],
                            status=stream['status'],
                            current_viewers=stream['current_viewers'],
                            view_count=stream['view_count'],
                            as_time=stream['as_time'],
                            ae_time=stream['ae_time'],
                            created_at=stream['created_at'],
                            updated_at=stream['updated_at'],
                        )
                        #print(twitch_stream)
                        try:
                            await async_crud.update_tcstream(db=db, ch_id=twitch_channel['id'], stream=twitch_stream)
                        except Exception as e:
                            self.logger.error(e)
                    skip += 35
                    limit += 35
                    await asyncio.sleep(float(0.2))
    
    
    # Get Twitter data.
    @tasks.loop(seconds=5)
    async def twitter_data(self):
        async with aiohttp.ClientSession() as session:
            # Get Twitter aount data.
            request_url = "/twitter/"
            twitter_account = await self.aioget(session, request_url)
            if twitter_account:
                tw = schemas.Twitter(
                    id=twitter_account['id'],
                    display_id=twitter_account['display_id'],
                    name=twitter_account['name'],
                    icon=twitter_account['icon'],
                    description=twitter_account['description'],
                    followers_count=twitter_account['followers_count'],
                    following_count=twitter_account['following_count'],
                    tweet_count=twitter_account['tweet_count'],
                    status=twitter_account['status'],
                    updated_at=twitter_account['updated_at'],
                )
                #print(tw)
                async with async_session() as db:
                    try:
                        await async_crud.update_twac(db=db, tw=tw)
                    except Exception as e:
                            self.logger.error(e)
                
            # Get Twitter space data.
            skip = 0
            limit = 35
            request_url = "/twitter/space/"
            async with async_session() as db:
                while True:
                    params = {
                        'order': 'created_at',
                        'skip': skip,
                        'limit': limit,
                    }
                    data = await self.aioget(session, request_url, params)
                    if data == []:
                        break
                    for space in data:
                        twitter_space = schemas.TwitterSpace(
                            id=space['id'],
                            title=space['title'],
                            url=space['url'],
                            status=space['status'],
                            audience_count=space['audience_count'],
                            ss_time=space['ss_time'],
                            as_time=space['as_time'],
                            ae_time=space['ae_time'],
                            created_at=space['created_at'],
                            updated_at=space['updated_at'],
                        )
                        #print(twitter_space)
                        try:
                            await async_crud.update_twspace(db=db, tw_id=twitter_account['id'], space=twitter_space)
                        except Exception as e:
                            self.logger.error(e)
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