import discord
import asyncio
import os
from discord.ext import tasks, commands
from cogs import crud, models, schemas
from cogs.db import SessionLocal
from cogs import embed_msg
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)


class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('notification_tasks')
        self.notice_chid = int(os.environ.get('MIKONOTICE_CHID'))
        self.youtube_id = os.environ.get('YOUTUBE')
        self.twitter_id = os.environ.get('TWITTER')
        self.twitch_id = os.environ.get('TWITCH')
        self.ytch_notice.start()
        self.ytvideo_notice.start()
    
    def cog_unload(self):
        self.ytch_notice.cancel()
        self.ytvideo_notice.cancel()


    # YouTube Channel Notice
    @tasks.loop(seconds=5)
    async def ytch_notice(self):
        notice_ch = self.bot.get_channel(self.notice_chid)
        with SessionLocal() as db:
            ch_latest = crud.get_ytch(db, self.youtube_id)
            ch_old = crud.get_ytch_old(db, self.youtube_id)
            

            if not ch_latest:
                self.logger.error('Not found YouTube channel in DB.')
                return
            if not ch_old:
                self.logger.warn('Not found YouTube channel in Old DB.')
                crud.update_ytch_old(db, ch_latest)
                return
        

            # YouTubeチャンネル名が変更された時
            if ch_latest.name != ch_old.name:
                self.logger.info(f'Update YouTube channel name. {ch_old.name} -> {ch_latest.name}')
                msg = await notice_ch.send(embed=embed_msg.ytch_notice_name(ch_latest.id, ch_old.name, ch_latest.name, ch_latest.icon))
                await msg.publish()
                ch_old.name = ch_latest.name
                
            # YouTubeチャンネルアイコンが変更された時
            #if ch_latest.icon != ch_old.icon:
            #    self.logger.info(f'Update YouTube channel icon. {ch_old.icon} -> {ch_latest.icon}')
            #    msg = await notice_ch.send(embed=embed_msg.ytch_notice_icon(ch_latest.id, ch_latest.name, ch_latest.icon, ch_old.icon))
            #    await msg.publish()
            #    ch_old.icon = ch_latest.icon
            
            # YouTubeチャンネル概要が変更された時
            #if ch_latest.description != ch_old.description:
            #    self.logger.info(f'Update YouTube channel description.')
            #    msg = await notice_ch.send(embed=embed_msg.ytch_notice_description(ch_latest.id, ch_latest.name, ch_latest.icon))
            #    await msg.publish()
            #    ch_old.description = ch_latest.description
                
            # YouTubeチャンネル登録者数が更新された時
            if ch_latest.subsc_count != ch_old.subsc_count:
                self.logger.info(f'Update YouTube channel subscriber count. {ch_old.subsc_count} -> {ch_latest.subsc_count}')
                msg = await notice_ch.send(embed=embed_msg.ytch_notice_subsc(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.subsc_count))
                await msg.publish()
                ch_old.subsc_count = ch_latest.subsc_count
                
            # YouTubeチャンネル総再生回数が更新された時
            if ch_latest.play_count != ch_old.play_count:
                self.logger.info(f'Update YouTube channel total play count. {ch_old.play_count} -> {ch_latest.play_count}')
                if round(ch_latest.play_count, -6) > round(ch_old.play_count, -6):
                    msg = await notice_ch.send(embed=embed_msg.ytch_notice_play(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.play_count))
                    await msg.publish()
                    ch_old.play_count = ch_latest.play_count
                
            # YouTubeチャンネル総動画本数が更新された時
            if ch_latest.video_count != ch_old.video_count:
                self.logger.info(f'Update YouTube channel total video count. {ch_old.video_count} -> {ch_latest.video_count}')
                if round(ch_latest.video_count, -2) > round(ch_old.video_count, -2):
                    msg = await notice_ch.send(embed=embed_msg.ytch_notice_video(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.video_count))
                    await msg.publish()
                    ch_old.video_count = ch_latest.video_count
                
            db.commit()
            

    # YouTube Video Notice
    @tasks.loop(seconds=5)
    async def ytvideo_notice(self):
        with SessionLocal() as db:
            return

    
    @ytch_notice.before_loop
    @ytvideo_notice.before_loop
    async def wait_notification_tasks(self):
        await self.bot.wait_until_ready()
        self.logger.info('Notification tasks start waiting...')
        
def setup(bot):
    return bot.add_cog(Notification(bot))