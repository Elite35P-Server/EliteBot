import os
from discord.ext import tasks, commands
from cogs import crud, models
from cogs.db import SessionLocal
from cogs import embed_msg
from logging import getLogger, config
from main import log_config
from cogs import schemas

config.dictConfig(log_config)


class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger('notification_tasks')
        self.notice_chid = int(os.environ.get('MIKONOTICE_CHID'))
        self.notice_role = os.environ.get('MIKONOTICE_ROLE')
        self.youtube_id = os.environ.get('YOUTUBE')
        self.twitter_id = os.environ.get('TWITTER')
        self.twitch_id = os.environ.get('TWITCH')
        self.ytch_notice.start()
        self.ytvideo_notice.start()
        self.tcch_notice.start()
        self.tcstream_notice.start()
        self.twac_notice.start()
        self.twspace_notice.start()
    
    def cog_unload(self):
        self.ytch_notice.cancel()
        self.ytvideo_notice.cancel()
        self.tcch_notice.cancel()
        self.tcstream_notice.cancel()
        self.twac_notice.cancel()
        self.twspace_notice.cancel()


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
                msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.ytch_notice_name(ch_latest.id, ch_old.name, ch_latest.name, ch_latest.icon))
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
            elif ch_latest.subsc_count > ch_old.subsc_count:
                self.logger.info(f'Update YouTube channel subscriber count. {ch_old.subsc_count} -> {ch_latest.subsc_count}')
                if int(ch_latest.subsc_count/50000) > int(ch_old.subsc_count/50000):
                    msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.ytch_notice_subsc(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.subsc_count, ch_latest.updated_at))
                else:
                    msg = await notice_ch.send(embed=embed_msg.ytch_notice_subsc(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.subsc_count, ch_latest.updated_at))
                await msg.publish()
                ch_old.subsc_count = ch_latest.subsc_count
                
            # YouTubeチャンネル総再生回数が更新された時
            elif ch_latest.play_count > ch_old.play_count:
                self.logger.info(f'Update YouTube channel total play count. {ch_old.play_count} -> {ch_latest.play_count}')
                if ch_latest.play_count < 200000000:
                    if int(ch_latest.play_count/10000000) > int(ch_old.play_count/10000000):
                        msg = await notice_ch.send(embed=embed_msg.ytch_notice_play(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.play_count, ch_latest.updated_at))
                        await msg.publish()
                else:
                    if int(ch_latest.play_count/20000000) > int(ch_old.play_count/20000000):
                        msg = await notice_ch.send(embed=embed_msg.ytch_notice_play(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.play_count, ch_latest.updated_at))
                        await msg.publish()
                ch_old.play_count = ch_latest.play_count
                
            # YouTubeチャンネル総動画本数が更新された時
            elif ch_latest.video_count != ch_old.video_count:
                self.logger.info(f'Update YouTube channel total video count. {ch_old.video_count} -> {ch_latest.video_count}')
                if int(ch_latest.video_count/100) > int(ch_old.video_count/100):
                    msg = await notice_ch.send(embed=embed_msg.ytch_notice_video(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.video_count, ch_latest.updated_at))
                    await msg.publish()
                ch_old.video_count = ch_latest.video_count
                
            db.commit()
            

    # YouTube Video Notice
    @tasks.loop(seconds=5)
    async def ytvideo_notice(self):
        notice_ch = self.bot.get_channel(self.notice_chid)
        with SessionLocal() as db:
            ch_latest = crud.get_ytch(db, self.youtube_id)
            videos_latest = crud.get_ytvideos_date(db)
            videos_old = crud.get_ytvideos_date_old(db)
            
            if videos_latest == []:
                self.logger.error('Not found YouTube videos in DB.')
                return
            
            
            for video_latest in videos_latest:
                if videos_old == []:
                    self.logger.warn(f'Not found YouTube video in Old DB.')
                    video = schemas.YouTubeVideo(
                        id=video_latest.id, 
                        title=video_latest.title,
                        thumbnails=video_latest.thumbnails,
                        description=video_latest.description,
                        url=video_latest.url,
                        play_count=video_latest.play_count,
                        like_count=video_latest.like_count,
                        comment_count=video_latest.comment_count,
                        status=video_latest.status,
                        current_viewers=video_latest.current_viewers,
                        ss_time=video_latest.ss_time,
                        as_time=video_latest.as_time,
                        ae_time=video_latest.ae_time,
                        created_at=video_latest.created_at,
                        updated_at=video_latest.updated_at,
                    )
                    crud.update_ytvideo_old(db, self.youtube_id, video)
                    continue
                
                for video_old in videos_old:
                    if video_latest.id == video_old.id:
                        # YouTube動画タイトルが変更された時
                        if video_latest.title != video_old.title:
                            self.logger.info(f'Update YouTube video title. ID: {video_latest.id}, Title: {video_old.title} -> {video_latest.title}')
                            msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_title(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.url, video_latest.id, video_old.title, video_latest.title))
                            await msg.publish()
                            video_old.title = video_latest.title
                            
                        # YouTube動画概要が変更された時
                        elif video_latest.description != video_old.description:
                            self.logger.info(f'Update YouTube video description. ID: {video_latest.id}, Title: {video_latest.title}')
                            video_old.description = video_latest.description
                            
                        # YouTube動画再生回数が更新された時
                        elif video_latest.play_count > video_old.play_count:
                            self.logger.info(f'Update YouTube video play count. ID: {video_latest.id}, Title: {video_latest.title}, PlayCount: {video_old.play_count} -> {video_latest.play_count}')
                            if video_latest.play_count < 1000000:
                                if int(video_latest.play_count/100000) > int(video_old.play_count/100000):
                                    trigger = int(video_latest.play_count/100000)*100000
                                    if video_latest.status == 'live':
                                        msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_play_live(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.play_count, video_latest.updated_at))
                                    else:
                                        msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_play(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.play_count, video_latest.updated_at))
                                    await msg.publish()
                            elif video_latest.play_count < 10000000:
                                if int(video_latest.play_count/500000) > int(video_old.play_count/500000):
                                    trigger = int(video_latest.play_count/500000)*500000
                                    if video_latest.status == 'live':
                                        msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_play_live(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.play_count, video_latest.updated_at))
                                    else:
                                        msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_play(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.play_count, video_latest.updated_at))
                                    await msg.publish()
                            else:
                                if int(video_latest.play_count/1000000) > int(video_old.play_count/1000000):
                                    trigger = int(video_latest.play_count/1000000)*1000000
                                    if video_latest.status == 'live':
                                        msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_play_live(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.play_count, video_latest.updated_at))
                                    else:
                                        msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_play(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.play_count, video_latest.updated_at))
                                await msg.publish()
                            video_old.play_count = video_latest.play_count
                        
                        # YouTube動画高評価数が更新された時
                        elif video_latest.like_count > video_old.like_count:
                            self.logger.info(f'Update YouTube video like count. ID: {video_latest.id}, Title: {video_latest.title}, LikeCount: {video_old.like_count} -> {video_latest.like_count}')
                            if int(video_latest.like_count/10000) > int(video_old.like_count/10000):
                                trigger = int(video_latest.like_count/10000)*10000
                                if video_latest.status == 'live':
                                    msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_like_live(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.like_count, video_latest.updated_at))
                                else:
                                    msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_like(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.like_count, video_latest.updated_at))
                                await msg.publish()
                            video_old.like_count = video_latest.like_count

                        # YouTube動画コメント数が更新された時
                        elif video_latest.comment_count != video_old.comment_count:
                            self.logger.info(f'Update YouTube video comment count. ID: {video_latest.id}, Title: {video_latest.title}, CommentCount: {video_old.comment_count} -> {video_latest.comment_count}')
                            video_old.comment_count = video_latest.comment_count
                            
                        # YouTube動画ステータスが更新された時
                        elif video_latest.status != video_old.status:
                            self.logger.info(f'Update YouTube video status. ID: {video_latest.id}, Title: {video_latest.title}, Status: {video_old.status} -> {video_latest.status}')
                            if video_old.status == 'upcoming' or video_latest.status == 'live':
                                msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.ytvideo_notice_upcomingtolive(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, video_latest.ss_time, video_latest.as_time))
                            elif video_old.status == 'live' and video_latest.status == 'none':
                                msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_livetonone(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, video_latest.as_time, video_latest.ae_time))
                            await msg.publish()
                            video_old.status = video_latest.status
                            
                        # YouTube配信同時接続数が更新された時
                        elif video_latest.current_viewers != video_old.current_viewers:
                            if video_old.current_viewers == None:
                                self.logger.info(f'Update YouTube stream current viewers. ID: {video_latest.id}, Title: {video_latest.title}, CurrentViewers: {video_old.current_viewers} -> {video_latest.current_viewers}')
                                video_old.current_viewers = video_latest.current_viewers
                            elif video_latest.current_viewers == None:
                                self.logger.info(f'Update YouTube stream current viewers. ID: {video_latest.id}, Title: {video_latest.title}, MaxCurrentViewers: {video_old.current_viewers}')
                                video_old.current_viewers = video_latest.current_viewers
                            elif video_latest.status == 'live' and video_latest.current_viewers > video_old.current_viewers:
                                self.logger.info(f'Update YouTube stream max current viewers. ID: {video_latest.id}, Title: {video_latest.title}, MaxCurrentViewers: {video_old.current_viewers} -> {video_latest.current_viewers}')
                                if int(video_latest.current_viewers/25000) > int(video_old.current_viewers/25000):
                                    trigger = int(video_latest.current_viewers/25000)*25000
                                    msg = await notice_ch.send(embed=embed_msg.ytvideo_notice_currentviewers(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, trigger, video_latest.current_viewers, video_latest.updated_at))
                                    await msg.publish()
                                video_old.current_viewers = video_latest.current_viewers
                            
                        # YouTube動画配信開始予定時刻が更新された時
                        elif video_latest.ss_time != video_old.ss_time:
                            self.logger.info(f'Update YouTube video scheduled start time. ID: {video_latest.id}, Title: {video_latest.title}, ScheduledStartTime: {video_old.ss_time} -> {video_latest.ss_time}')
                            msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.ytvideo_notice_sstime(ch_latest.id, ch_latest.name, ch_latest.icon,  video_latest.title, video_latest.url, video_latest.id, video_old.ss_time, video_latest.ss_time))
                            await msg.publish()
                            video_old.ss_time = video_latest.ss_time
                            
                            
                        # YouTube動画配信開始時刻が更新された時
                        elif video_latest.as_time != video_old.as_time:
                            self.logger.info(f'Update YouTube video actuary start time. ID: {video_latest.id}, Title: {video_latest.title}, ActuaryStartTime: {video_old.as_time} -> {video_latest.as_time}')
                            video_old.as_time = video_latest.as_time
                            
                        # YouTube動画配信終了時刻が更新された時
                        elif video_latest.ae_time != video_old.ae_time:
                            self.logger.info(f'Update YouTube video actuary end time. ID: {video_latest.id}, Title: {video_latest.title}, ActuaryEndTime: {video_old.ae_time} -> {video_latest.ae_time}')
                            video_old.ae_time = video_latest.ae_time
                            
                        db.commit()
                        break
                    
                if video_latest.id not in [video.id for video in videos_old]:
                    # YouTube配信待機枠または動画が作成された時
                    self.logger.info(f'New YouTube video. ID: {video_latest.id}, Title: {video_latest.title}')
                    if video_latest.status == 'upcoming':
                        msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.ytvideo_notice_nonetoupcoming(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, video_latest.ss_time))
                    elif video_latest.status == 'live':
                        msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.ytvideo_notice_nonetolive(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, video_latest.as_time))
                    elif video_latest.status == 'none' and video_latest.ss_time ==  None and video_latest.as_time ==  None and video_latest.ae_time ==  None:
                        msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.ytvideo_notice_upload(ch_latest.id, ch_latest.name, ch_latest.icon, video_latest.title, video_latest.url, video_latest.id, video_latest.created_at))
                    await msg.publish()
                    
                    video = schemas.YouTubeVideo(
                        id=video_latest.id, 
                        title=video_latest.title,
                        thumbnails=video_latest.thumbnails,
                        description=video_latest.description,
                        url=video_latest.url,
                        play_count=video_latest.play_count,
                        like_count=video_latest.like_count,
                        comment_count=video_latest.comment_count,
                        status=video_latest.status,
                        current_viewers=video_latest.current_viewers,
                        ss_time=video_latest.ss_time,
                        as_time=video_latest.as_time,
                        ae_time=video_latest.ae_time,
                        created_at=video_latest.created_at,
                        updated_at=video_latest.updated_at,
                    )
                    crud.update_ytvideo_old(db, self.youtube_id, video)
        

    # Twitch Channel Notice
    @tasks.loop(seconds=5)
    async def tcch_notice(self):
        notice_ch = self.bot.get_channel(self.notice_chid)
        with SessionLocal() as db:
            ch_latest = crud.get_tcch(db, self.twitch_id)
            ch_old = crud.get_tcch_old(db, self.twitch_id)
            
            if not ch_latest:
                self.logger.error('Not found Twitch channel in DB.')
                return
            if not ch_old:
                self.logger.warn('Not found Twitch channel in Old DB.')
                crud.update_tcch_old(db, ch_latest)
                return
        

            # Twitchチャンネル名が変更された時
            if ch_latest.name != ch_old.name:
                self.logger.info(f'Update Twitch channel name. {ch_old.name} -> {ch_latest.name}')
                msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.tcch_notice_name(ch_latest.display_id, ch_old.name, ch_latest.name, ch_latest.icon))
                await msg.publish()
                ch_old.name = ch_latest.name
                
            # TwitchチャンネルディスプレイIDが変更された時
            elif ch_latest.display_id != ch_old.display_id:
                self.logger.info(f'Update Twitch channel display id. {ch_old.display_id} -> {ch_latest.display_id}')
                msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.tcch_notice_displayid(ch_latest.name, ch_old.display_id, ch_latest.display_id, ch_latest.icon))
                await msg.publish()
                ch_old.display_id = ch_latest.display_id
                
            # Twitchチャンネルアイコンが変更された時
            #if ch_latest.icon != ch_old.icon:
            #    self.logger.info(f'Update YouTube channel icon. {ch_old.icon} -> {ch_latest.icon}')
            #    msg = await notice_ch.send(embed=embed_msg.ytch_notice_icon(ch_latest.id, ch_latest.name, ch_latest.icon, ch_old.icon))
            #    await msg.publish()
            #    ch_old.icon = ch_latest.icon
            
            # Twitchチャンネル概要が変更された時
            #if ch_latest.description != ch_old.description:
            #    self.logger.info(f'Update YouTube channel description.')
            #    msg = await notice_ch.send(embed=embed_msg.ytch_notice_description(ch_latest.id, ch_latest.name, ch_latest.icon))
            #    await msg.publish()
            #    ch_old.description = ch_latest.description
                
            # Twitchチャンネルフォロワー数が更新された時
            elif ch_latest.subsc_count > ch_old.subsc_count:
                self.logger.info(f'Update Twitch channel subscriber count. {ch_old.subsc_count} -> {ch_latest.subsc_count}')
                if int(ch_latest.play_count/10000) > int(ch_old.play_count/10000):
                    msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.tcch_notice_subsc(ch_latest.display_id, ch_latest.name, ch_latest.icon, ch_latest.subsc_count, ch_latest.updated_at))
                    await msg.publish()
                ch_old.subsc_count = ch_latest.subsc_count
                
            # Twitchチャンネル総再生回数が更新された時
            elif ch_latest.play_count > ch_old.play_count:
                self.logger.info(f'Update Twitch channel total play count. {ch_old.play_count} -> {ch_latest.play_count}')
                if ch_latest.play_count < 100000000:
                    if int(ch_latest.play_count/100000) > int(ch_old.play_count/100000):
                        msg = await notice_ch.send(embed=embed_msg.tcch_notice_play(ch_latest.display_id, ch_latest.name, ch_latest.icon, ch_latest.play_count, ch_latest.updated_at))
                        await msg.publish()
                else:
                    #if int(ch_latest.play_count/20000000) > int(ch_old.play_count/20000000):
                    #    msg = await notice_ch.send(embed=embed_msg.tcch_notice_play(ch_latest.id, ch_latest.name, ch_latest.icon, ch_latest.play_count, ch_latest.updated_at))
                    #    await msg.publish()
                    pass
                ch_old.play_count = ch_latest.play_count
                
            db.commit()
    
    # Twitch Stream Notice
    @tasks.loop(seconds=5)
    async def tcstream_notice(self):
        notice_ch = self.bot.get_channel(self.notice_chid)
        with SessionLocal() as db:
            ch_latest = crud.get_tcch(db, self.twitch_id)
            streams_latest = crud.get_tcstreams_date(db)
            streams_old = crud.get_tcstreams_date_old(db)
            
            if streams_latest == []:
                self.logger.error('Not found Twitch streams in DB.')
                return
            
            
            for stream_latest in streams_latest:
                if streams_old == []:
                    self.logger.warn(f'Not found Twitch stream in Old DB.')
                    stream = schemas.TwitchStream(
                        id=stream_latest.id,
                        stream_id=stream_latest.stream_id,
                        title=stream_latest.title,
                        thumbnail=stream_latest.thumbnail,
                        description=stream_latest.description,
                        url=stream_latest.url,
                        type=stream_latest.type,
                        game_id=stream_latest.game_id,
                        game_name=stream_latest.game_name,
                        status=stream_latest.status,
                        current_viewers=stream_latest.current_viewers,
                        view_count=stream_latest.view_count,
                        as_time=stream_latest.as_time,
                        ae_time=stream_latest.ae_time,
                        created_at=stream_latest.created_at,
                        updated_at=stream_latest.updated_at,
                    )
                    crud.update_tcstream_old(db, self.twitch_id, stream)
                    continue
                
                for stream_old in streams_old:
                    if stream_latest.id == stream_old.id:
                        # Twitch動画タイトルが変更された時
                        if stream_latest.title != stream_old.title:
                            self.logger.info(f'Update Twitch stream title. ID: {stream_latest.id}, Title: {stream_old.title} -> {stream_latest.title}')
                            msg = await notice_ch.send(embed=embed_msg.tcstream_notice_title(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.url, stream_latest.thumbnail, stream_old.title, stream_latest.title))
                            await msg.publish()
                            stream_old.title = stream_latest.title
                            
                        # Twitch動画概要が変更された時
                        elif stream_latest.description != stream_old.description:
                            self.logger.info(f'Update Twitch stream description. ID: {stream_latest.id}, Title: {stream_latest.title}')
                            stream_old.description = stream_latest.description
                            
                        # Twitch配信ステータスが更新された時
                        elif stream_latest.status != stream_old.status:
                            self.logger.info(f'Update Twitch stream status. ID: {stream_latest.id}, Title: {stream_latest.title}, Status: {stream_old.status} -> {stream_latest.status}')
                            if stream_old.status == 'live' and stream_latest.status == 'none':
                                msg = await notice_ch.send(embed=embed_msg.tcstream_notice_livetonone(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, stream_latest.as_time, stream_latest.ae_time))
                                await msg.publish()
                            stream_old.status = stream_latest.status
                        
                        # Twitch配信同時接続数が更新された時
                        elif stream_latest.current_viewers != stream_old.current_viewers:
                            if stream_old.current_viewers == None:
                                self.logger.info(f'Update Twitch stream current viewers. ID: {stream_latest.id}, Title: {stream_latest.title}, CurrentViewers: {stream_latest.current_viewers}')
                                stream_old.current_viewers = stream_latest.current_viewers
                            elif stream_latest.current_viewers == None:
                                self.logger.info(f'Update Twitch stream current viewers. ID: {stream_latest.id}, Title: {stream_latest.title}, MaxCurrentViewers: {stream_latest.current_viewers}')
                                stream_old.current_viewers = stream_latest.current_viewers
                            elif stream_latest.status == 'live' and stream_latest.current_viewers > stream_old.current_viewers:
                                self.logger.info(f'Update Twitch stream max current viewers. ID: {stream_latest.id}, Title: {stream_latest.title}, MaxCurrentViewers: {stream_old.current_viewers} -> {stream_latest.current_viewers}')
                                if int(stream_latest.current_viewers/10000) > int(stream_old.current_viewers/10000):
                                    trigger = int(stream_latest.current_viewers/10000)*10000
                                    msg = await notice_ch.send(embed=embed_msg.tcstream_notice_currentviewers(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, trigger, stream_latest.current_viewers, stream_latest.updated_at))
                                    await msg.publish()
                                stream_old.current_viewers = stream_latest.current_viewers
                            
                        # Twitch配信再生回数が更新された時
                        elif stream_latest.view_count > stream_old.view_count:
                            self.logger.info(f'Update Twitch stream play count. ID: {stream_latest.id}, Title: {stream_latest.title}, PlayCount: {stream_old.view_count} -> {stream_latest.view_count}')
                            if stream_latest.view_count < 100000:
                                if int(stream_latest.view_count/10000) > int(stream_old.view_count/10000):
                                    trigger = int(stream_latest.view_count/10000)*10000
                                    if stream_latest.status == 'live':
                                        msg = await notice_ch.send(embed=embed_msg.tcstream_notice_play_live(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, trigger, stream_latest.view_count, stream_latest.updated_at))
                                    else:
                                        msg = await notice_ch.send(embed=embed_msg.tcstream_notice_play(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, trigger, stream_latest.view_count, stream_latest.updated_at))
                                    await msg.publish()
                            elif stream_latest.view_count < 1000000:
                                if int(stream_latest.view_count/50000) > int(stream_old.view_count/50000):
                                    trigger = int(stream_latest.view_count/50000)*50000
                                    if stream_latest.status == 'live':
                                        msg = await notice_ch.send(embed=embed_msg.tcstream_notice_play_live(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, trigger, stream_latest.view_count, stream_latest.updated_at))
                                    else:
                                        msg = await notice_ch.send(embed=embed_msg.tcstream_notice_play(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, trigger, stream_latest.view_count, stream_latest.updated_at))
                                    await msg.publish()
                            else:
                                if int(stream_latest.view_count/100000) > int(stream_old.view_count/100000):
                                    trigger = int(stream_latest.view_count/100000)*100000
                                    if stream_latest.status == 'live':
                                        msg = await notice_ch.send(embed=embed_msg.tcstream_notice_play_live(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, trigger, stream_latest.view_count, stream_latest.updated_at))
                                    else:
                                        msg = await notice_ch.send(embed=embed_msg.tcstream_notice_play(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, trigger, stream_latest.view_count, stream_latest.updated_at))
                                    await msg.publish()
                            
                            stream_old.view_count = stream_latest.view_count
                        
                        # Twitch配信終了時刻が更新された時
                        elif stream_latest.ae_time != stream_old.ae_time:
                            self.logger.info(f'Update Twitch stream actuary end time. ID: {stream_latest.id}, Title: {stream_latest.title}, ActuaryEndTime: {stream_old.ae_time} -> {stream_latest.ae_time}')
                            stream_old.ae_time = stream_latest.ae_time
                            
                        # Twitch配信game_id,game_nameが更新された時
                        elif stream_latest.game_id != stream_old.game_id:
                            self.logger.info(f'Update Twitch stream game_id and game_name. ID: {stream_latest.id}, Title: {stream_latest.title}, Game: {stream_old.game_name}({stream_old.game_id}) -> {stream_latest.game_name}({stream_old.game_id})')
                            stream_old.game_id = stream_latest.game_id
                            stream_old.game_name = stream_latest.game_name
                        
                        db.commit()
                        break
                
                if stream_latest.id not in [stream.id for stream in streams_old]:
                    # Twitch配信または動画が作成された時
                    self.logger.info(f'New Twitch stream. ID: {stream_latest.id}, Title: {stream_latest.title}')
                    if stream_latest.status == 'live':
                        msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.tcstream_notice_nonetolive(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, stream_latest.as_time))
                        await msg.publish()
                    elif stream_latest.type != 'archive':
                        msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.tcstream_notice_upload(ch_latest.display_id, ch_latest.name, ch_latest.icon, stream_latest.title, stream_latest.url, stream_latest.thumbnail, stream_latest.created_at))
                        await msg.publish()
                    
                    stream = schemas.TwitchStream(
                        id=stream_latest.id,
                        stream_id=stream_latest.stream_id,
                        title=stream_latest.title,
                        thumbnail=stream_latest.thumbnail,
                        description=stream_latest.description,
                        url=stream_latest.url,
                        type=stream_latest.type,
                        game_id=stream_latest.game_id,
                        game_name=stream_latest.game_name,
                        status=stream_latest.status,
                        current_viewers=stream_latest.current_viewers,
                        view_count=stream_latest.view_count,
                        as_time=stream_latest.as_time,
                        ae_time=stream_latest.ae_time,
                        created_at=stream_latest.created_at,
                        updated_at=stream_latest.updated_at,
                    )
                    crud.update_tcstream_old(db, self.twitch_id, stream)
    
    # Twitter Account Notice
    @tasks.loop(seconds=5)
    async def twac_notice(self):
        notice_ch = self.bot.get_channel(self.notice_chid)
        with SessionLocal() as db:
            twac_latest = crud.get_twac(db, self.twitter_id)
            twac_old = crud.get_twac_old(db, self.twitter_id)
            
            if not twac_latest:
                self.logger.error('Not found Twitter account in DB.')
                return
            if not twac_old:
                self.logger.warn('Not found Twitter account in Old DB.')
                crud.update_twac_old(db, twac_latest)
                return
            
            # Twitterアカウント名が変更された時
            if twac_latest.name != twac_old.name:
                self.logger.info(f'Update Twitter account name. Name: {twac_old.name} -> {twac_latest.name}')
                msg = await notice_ch.send(embed=embed_msg.twac_notice_name(twac_latest.display_id, twac_old.name, twac_latest.name, twac_latest.icon))
                await msg.publish()
                twac_old.name = twac_latest.name
            
            # Twitterアカウント表示IDが変更された時
            elif twac_latest.display_id != twac_old.display_id:
                self.logger.info(f'Update Twitter account display_id. ID: {twac_old.display_id} -> {twac_latest.display_id}')
                msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.twac_notice_displayid(twac_latest.name, twac_old.display_id, twac_latest.display_id, twac_latest.icon))
                await msg.publish()
                twac_old.display_name = twac_latest.display_name
                
            # Twitterアカウント説明が変更された時
            elif twac_latest.description != twac_old.description:
                self.logger.info('Update Twitter account description.')
                twac_old.description = twac_latest.description
            
            # Twitterアカウントフォロワー数が更新された時
            elif twac_latest.followers_count > twac_old.followers_count:
                self.logger.info(f'Update Twitter account followers_count. FollowersCount: {twac_old.followers_count} -> {twac_latest.followers_count}')
                if int(twac_latest.followers_count/10000) > int(twac_old.followers_count/10000):
                    msg = await notice_ch.send(embed=embed_msg.twac_notice_subsc(twac_latest.display_id, twac_latest.name, twac_latest.icon, twac_latest.followers_count, twac_latest.updated_at))
                    await msg.publish()
                twac_old.followers_count = twac_latest.followers_count
            
            # Twitterアカウントフォロー数が更新された時
            elif twac_latest.following_count > twac_old.following_count:
                self.logger.info(f'Update Twitter account following_count. FollowingCount: {twac_old.following_count} -> {twac_latest.following_count}')
                twac_old.following_count = twac_latest.following_count
            
            # Twitterアカウントツイート数が更新された時
            elif twac_latest.tweet_count > twac_old.tweet_count:
                self.logger.info(f'Update Twitter account tweet_count. TweetCount: {twac_old.tweet_count} -> {twac_latest.tweet_count}')
                if int(twac_latest.tweet_count/5000) > int(twac_old.tweet_count/5000):
                    msg = await notice_ch.send(embed=embed_msg.twac_notice_tweet(twac_latest.display_id, twac_latest.name, twac_latest.icon, twac_latest.tweet_count, twac_latest.updated_at))
                    await msg.publish()
                twac_old.tweet_count = twac_latest.tweet_count
                
            db.commit()
    
    # Twitter Space Notice
    @tasks.loop(seconds=5)
    async def twspace_notice(self):
        notice_ch = self.bot.get_channel(self.notice_chid)
        with SessionLocal() as db:
            twac_latest = crud.get_twac(db, self.twitch_id)
            spaces_latest = crud.get_twspaces_date(db)
            spaces_old = crud.get_twspaces_date_old(db)
            
            if spaces_latest == []:
                self.logger.error('Not found Twittr space in DB.')
                return
            
            
            for space_latest in spaces_latest:
                if spaces_old == []:
                    self.logger.warn(f'Not found Twitter space in Old DB.')
                    space = schemas.TwitterSpace(
                        id=space_latest.id,
                        title=space_latest.title,
                        url=space_latest.url,
                        status=space_latest.status,
                        audience_count=space_latest.audience_count,
                        ss_time=space_latest.ss_time,
                        as_time=space_latest.as_time,
                        ae_time=space_latest.ae_time,
                        created_at=space_latest.created_at,
                        updated_at=space_latest.updated_at,
                    )
                    crud.update_twspace_old(db, self.twitter_id, space)
                    continue
                
                for space_old in spaces_old:
                    if space_latest.id == space_old.id:
                        # Twitterスペースタイトルが変更された時
                        if space_latest.title != space_old.title:
                            self.logger.info(f'Update Twittr space audience_count title. ID: {space_latest.id}, Title: {space_old.title} -> {space_latest.title}')
                            msg = await notice_ch.send(embed=embed_msg.twspace_notice_title(twac_latest.display_id, twac_latest.name, twac_latest.icon, space_latest.url, space_old.title, space_latest.title))
                            await msg.publish()
                            space_old.title = space_latest.title
                            
                        # Twitterスペース開始予定時刻が変更された時
                        elif space_latest.ss_time != space_old.ss_time:
                            self.logger.info(f'Update Twittr space ss_time. ID: {space_latest.id}, ScheduledStartTime: {space_old.ss_time} -> {space_latest.ss_time}')
                            msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.twspace_notice_sstime(twac_latest.display_id, twac_latest.name, twac_latest.icon, space_latest.title, space_latest.url, space_old.ss_time, space_latest.as_time))
                            await msg.publish()
                            space_old.ss_time = space_latest.ss_time
                            
                        # Twitterスペースステータスが更新された時
                        elif space_latest.status != space_old.status:
                            self.logger.info(f'Update Twittr space audience_count status. ID: {space_latest.id}, Title: {space_latest.title}, Status: {space_old.status} -> {space_latest.status}')
                            if space_old.status == 'scheduled' and space_old.status == 'live':
                                msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.twspace_notice_stolive(twac_latest.display_id, twac_latest.name, twac_latest.icon, space_latest.title, space_latest.url, space_latest.ss_time, space_latest.as_time))
                                await msg.publish()
                            if space_old.status == 'live' and space_latest.status == 'none':
                                msg = await notice_ch.send(embed=embed_msg.twspace_notice_livetonone(twac_latest.display_id, twac_latest.name, twac_latest.icon, space_latest.title, space_latest.url, space_latest.as_time, space_latest.ae_time))
                                await msg.publish()
                            space_old.status = space_latest.status
                        
                        # Twitterスペース視聴者数が更新された時
                        elif space_latest.audience_count != space_old.audience_count:
                            if space_old.audience_count == None:
                                self.logger.info(f'Update Twittr space audience_count current viewers. ID: {space_latest.id}, Title: {space_latest.title}, CurrentViewers: {space_latest.audience_count}')
                                space_old.audience_count = space_latest.audience_count
                            elif space_latest.audience_count == None:
                                self.logger.info(f'Update Twittr space audience_count max current viewers. ID: {space_latest.id}, Title: {space_latest.title}, MaxCurrentViewers: {space_latest.audience_count}')
                                space_old.audience_count = space_latest.audience_count
                            elif space_latest.status == 'live' and space_latest.audience_count > space_old.audience_count:
                                self.logger.info(f'Update Twittr space audience_count max current viewers. ID: {space_latest.id}, Title: {space_latest.title}, MaxCurrentViewers: {space_old.audience_count} -> {space_latest.audience_count}')
                                if int(space_latest.audience_count/10000) > int(space_old.audience_count/10000):
                                    trigger = int(space_latest.audience_count/10000)*10000
                                    msg = await notice_ch.send(embed=embed_msg.twspace_notice_currentviewers(twac_latest.display_id, twac_latest.name, twac_latest.icon, space_latest.title, space_latest.url, trigger, space_latest.audience_count, space_latest.updated_at))
                                    await msg.publish()
                                space_old.audience_count = space_latest.audience_count
                        
                        db.commit()
                        break
                
                
                if space_latest.id not in [space.id for space in spaces_old]:
                    # Twitterスペースが作成された時
                    self.logger.info(f'New Twitter space. ID: {space_latest.id}, Title: {space_latest.title}')
                    if space_latest.status == 'live':
                        msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.twspace_notice_nonetolive(twac_latest.display_id, twac_latest.name, twac_latest.icon, space_latest.title, space_latest.url, space_latest.as_time))
                        await msg.publish()
                    elif space_latest.status == 'scheduled':
                        msg = await notice_ch.send(content=self.notice_role, embed=embed_msg.twspace_notice_nonetos(twac_latest.display_id, twac_latest.name, twac_latest.icon, space_latest.title, space_latest.url, space_latest.ss_time))
                        await msg.publish()

                    
                    space = schemas.TwitterSpace(
                        id=space_latest.id,
                        title=space_latest.title,
                        url=space_latest.url,
                        status=space_latest.status,
                        audience_count=space_latest.audience_count,
                        ss_time=space_latest.ss_time,
                        as_time=space_latest.as_time,
                        ae_time=space_latest.ae_time,
                        created_at=space_latest.created_at,
                        updated_at=space_latest.updated_at,
                    )
                    crud.update_twspace_old(db, self.twitter_id, space)

    
    @ytch_notice.before_loop
    @ytvideo_notice.before_loop
    @tcch_notice.before_loop
    @tcstream_notice.before_loop
    @twac_notice.before_loop
    @twspace_notice.before_loop
    async def wait_notification_tasks(self):
        await self.bot.wait_until_ready()
        self.logger.info('Notification tasks start waiting...')
        
def setup(bot):
    return bot.add_cog(Notification(bot))
