from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, asc, select
from sqlalchemy.sql.expression import delete
from cogs import models, schemas
from logging import getLogger, config
from main import log_config

config.dictConfig(log_config)
logger = getLogger('async_crud')

# YouTube Channel
async def get_ytch(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.YouTubeChannelLatest).where(models.YouTubeChannelLatest.id == id)))
        ytch_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if ytch_db:
        return ytch_db[0]
    else:
        return ytch_db

async def get_ytch_old(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.YouTubeChannelOld).where(models.YouTubeChannelOld.id == id)))
        ytch_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if ytch_db:
        return ytch_db[0]
    else:
        return ytch_db

async def update_ytch(db: AsyncSession, ch: schemas.YouTubeCh):
    ch_db = await get_ytch(db, id=ch.id)
    if ch_db:
        if ch_db.name!=ch.name or ch_db.icon!=ch.icon or ch_db.description!=ch.description or ch_db.subsc_count!=ch.subsc_count or ch_db.play_count!=ch.play_count or ch_db.video_count!=ch.video_count or ch_db.status!= ch.status:
            ch_db.name = ch.name
            ch_db.icon = ch.icon
            ch_db.description = ch.description
            ch_db.subsc_count = ch.subsc_count
            ch_db.play_count = ch.play_count
            ch_db.video_count = ch.video_count
            ch_db.status = ch.status
            ch_db.updated_at = ch.updated_at
            await db.commit()
            await db.refresh(ch_db)
            
    else:
        ch_db = models.YouTubeChannelLatest(
            id=ch.id,
            name=ch.name,
            icon=ch.icon,
            description=ch.description,
            subsc_count=ch.subsc_count,
            play_count=ch.play_count,
            video_count=ch.video_count,
            status=ch.status,
            updated_at=ch.updated_at
        )
        db.add(ch_db)
        await db.commit()
        await db.refresh(ch_db)
    return

async def update_ytch_old(db: AsyncSession, ch: schemas.YouTubeCh):
    ch_db = await get_ytch_old(db, id=ch.id)
    if ch_db:
        if ch_db.name!=ch.name or ch_db.icon!=ch.icon or ch_db.description!=ch.description or ch_db.subsc_count!=ch.subsc_count or ch_db.play_count!=ch.play_count or ch_db.video_count!=ch.video_count or ch_db.status!= ch.status:
            ch_db.name = ch.name
            ch_db.icon = ch.icon
            ch_db.description = ch.description
            ch_db.subsc_count = ch.subsc_count
            ch_db.play_count = ch.play_count
            ch_db.video_count = ch.video_count
            ch_db.status = ch.status
            ch_db.updated_at = ch.updated_at
            await db.commit()
            await db.refresh(ch_db)
            
    else:
        ch_db = models.YouTubeChannelOld(
            id=ch.id,
            name=ch.name,
            icon=ch.icon,
            description=ch.description,
            subsc_count=ch.subsc_count,
            play_count=ch.play_count,
            video_count=ch.video_count,
            status=ch.status,
            updated_at=ch.updated_at
        )
        db.add(ch_db)
        await db.commit()
        await db.refresh(ch_db)
    return


#Twitter Account
async def get_twac(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitterAccountLatest).where(models.TwitterAccountLatest.id == id)))
        twac_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if twac_db:
        return twac_db[0]
    else:
        return twac_db

async def get_twac_old(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitterAccountOld).where(models.TwitterAccountOld.id == id)))
        twac_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if twac_db:
        return twac_db[0]
    else:
        return twac_db

async def update_twac(db: AsyncSession, tw: schemas.Twitter):
    tw_db = await get_twac(db, id=tw.id)
    if tw_db:
        if tw_db.display_id!=tw.display_id or tw_db.name!=tw.name or tw_db.icon!=tw.icon or tw_db.description!=tw.description or tw_db.followers_count!=tw.followers_count or tw_db.following_count!=tw.following_count or tw_db.status!=tw.status or tw_db.tweet_count!=tw.tweet_count:
            tw.display_id = tw.display_id
            tw_db.name = tw.name
            tw_db.icon = tw.icon
            tw_db.description = tw.description
            tw_db.followers_count = tw.followers_count
            tw_db.following_count = tw.following_count
            tw_db.tweet_count = tw.tweet_count
            tw_db.status = tw.status
            tw_db.updated_at = tw.updated_at
            await db.commit()
            await db.refresh(tw_db)
            
    else:
        tw_db = models.TwitterAccountLatest(id=tw.id,
                                      display_id=tw.display_id,
                                      name=tw.name,
                                      icon=tw.icon,
                                      description=tw.description,
                                      followers_count=tw.followers_count,
                                      following_count=tw.following_count,
                                      tweet_count=tw.tweet_count,
                                      status=tw.status,
                                      updated_at=tw.updated_at)
        db.add(tw_db)
        await db.commit()
        await db.refresh(tw_db)
    return

async def update_twac_old(db: AsyncSession, tw: schemas.Twitter):
    tw_db = await get_twac_old(db, id=tw.id)
    if tw_db:
        if tw_db.display_id!=tw.display_id or tw_db.name!=tw.name or tw_db.icon!=tw.icon or tw_db.description!=tw.description or tw_db.followers_count!=tw.followers_count or tw_db.following_count!=tw.following_count or tw_db.status!=tw.status or tw_db.tweet_count!=tw.tweet_count:
            tw.display_id = tw.display_id
            tw_db.name = tw.name
            tw_db.icon = tw.icon
            tw_db.description = tw.description
            tw_db.followers_count = tw.followers_count
            tw_db.following_count = tw.following_count
            tw_db.tweet_count = tw.tweet_count
            tw_db.status = tw.status
            tw_db.updated_at = tw.updated_at
            await db.commit()
            await db.refresh(tw_db)
            
    else:
        tw_db = models.TwitterAccountOld(id=tw.id,
                                      display_id=tw.display_id,
                                      name=tw.name,
                                      icon=tw.icon,
                                      description=tw.description,
                                      followers_count=tw.followers_count,
                                      following_count=tw.following_count,
                                      tweet_count=tw.tweet_count,
                                      status=tw.status,
                                      updated_at=tw.updated_at)
        db.add(tw_db)
        await db.commit()
        await db.refresh(tw_db)
    return


# Twitch Channel
async def get_tcch(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitchChannelLatest).where(models.TwitchChannelLatest.id == id)))
        tcch_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if tcch_db:
        return tcch_db[0]
    else:
        return tcch_db

async def get_tcch_old(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitchChannelOld).where(models.TwitchChannelOld.id == id)))
        tcch_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if tcch_db:
        return tcch_db[0]
    else:
        return tcch_db

async def update_tcch(db: AsyncSession, ch: schemas.TwitchCh):
    ch_db = await get_tcch(db, id=ch.id)
    if ch_db:
        if ch_db.display_id!=ch.display_id or ch_db.name!=ch.name or ch_db.icon!=ch.icon or ch_db.offline_img!=ch.offline_img or ch_db.description!=ch.description or ch_db.subsc_count!=ch.subsc_count or ch_db.play_count!=ch.play_count or ch_db.status!= ch.status:
            ch_db.display_id = ch.display_id
            ch_db.name = ch.name
            ch_db.icon = ch.icon
            ch_db.offline_img = ch.offline_img
            ch_db.description = ch.description
            ch_db.subsc_count = ch.subsc_count
            ch_db.play_count = ch.play_count
            ch_db.status = ch.status
            ch_db.updated_at = ch.updated_at
            await db.commit()
            await db.refresh(ch_db)
            
    else:
        ch_db = models.TwitchChannelLatest(id=ch.id,
                                     display_id=ch.display_id,
                                     name=ch.name,
                                     icon=ch.icon,
                                     offline_img=ch.offline_img,
                                     description=ch.description,
                                     subsc_count=ch.subsc_count,
                                     play_count=ch.play_count,
                                     status=ch.status,
                                     updated_at=ch.updated_at)
        db.add(ch_db)
        await db.commit()
        await db.refresh(ch_db)
    return

async def update_tcch_old(db: AsyncSession, ch: schemas.TwitchCh):
    ch_db = await get_tcch_old(db, id=ch.id)
    if ch_db:
        if ch_db.display_id!=ch.display_id or ch_db.name!=ch.name or ch_db.icon!=ch.icon or ch_db.offline_img!=ch.offline_img or ch_db.description!=ch.description or ch_db.subsc_count!=ch.subsc_count or ch_db.play_count!=ch.play_count or ch_db.status!= ch.status:
            ch_db.display_id = ch.display_id
            ch_db.name = ch.name
            ch_db.icon = ch.icon
            ch_db.offline_img = ch.offline_img
            ch_db.description = ch.description
            ch_db.subsc_count = ch.subsc_count
            ch_db.play_count = ch.play_count
            ch_db.status = ch.status
            ch_db.updated_at = ch.updated_at
            await db.commit()
            await db.refresh(ch_db)
            
    else:
        ch_db = models.TwitchChannelOld(id=ch.id,
                                     display_id=ch.display_id,
                                     name=ch.name,
                                     icon=ch.icon,
                                     offline_img=ch.offline_img,
                                     description=ch.description,
                                     subsc_count=ch.subsc_count,
                                     play_count=ch.play_count,
                                     status=ch.status,
                                     updated_at=ch.updated_at)
        db.add(ch_db)
        await db.commit()
        await db.refresh(ch_db)
    return


# YouTube Video
async def get_ytvideo(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.YouTubeVideoLatest).where(models.YouTubeVideoLatest.id == id)))
        ytvideo_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if ytvideo_db:
        return ytvideo_db[0]
    else:
        return ytvideo_db

async def get_ytvideo_old(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.YouTubeVideoOld).where(models.YouTubeVideoOld.id == id)))
        ytvideo_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if ytvideo_db:
        return ytvideo_db[0]
    else:
        return ytvideo_db

async def get_ytvideos_date(db: AsyncSession):
    try:
        result = await (db.execute(select(models.YouTubeVideoLatest).order_by(desc(models.YouTubeVideoLatest.created_at))))
        ytvideos_db = result.all()
    except Exception as e:
        logger.error(e)
        return []
    if ytvideos_db:
        return ytvideos_db[0]
    else:
        return ytvideos_db

async def get_ytvideos_date_old(db: AsyncSession):
    try:
        result = await (db.execute(select(models.YouTubeVideoOld).order_by(desc(models.YouTubeVideoOld.created_at))))
        ytvideos_db = result.all()
    except Exception as e:
        logger.error(e)
        return []
    if ytvideos_db:
        return ytvideos_db[0]
    else:
        return ytvideos_db

async def update_ytvideo(db: AsyncSession, ch_id: str, video: schemas.YouTubeVideo):
    video_db = await get_ytvideo(db, id=video.id)
    if video_db:
        if video_db.title!=video.title or video_db.description!=video.description or video_db.play_count!=video.play_count or video_db.like_count!=video.like_count or video_db.comment_count!=video.comment_count or video_db.current_viewers!=video.current_viewers or video_db.status!=video.status or video_db.ss_time!=video.ss_time or video_db.as_time!=video.as_time or video_db.ae_time!=video.ae_time:
            video_db.title = video.title
            video_db.thumbnails = video.thumbnails
            video_db.url = video.url
            video_db.description = video.description
            video_db.play_count = video.play_count
            video_db.like_count = video.like_count
            video_db.comment_count = video.comment_count
            video_db.status = video.status
            video_db.current_viewers = video.current_viewers
            video_db.ss_time = video.ss_time
            video_db.as_time = video.as_time
            video_db.ae_time = video.ae_time
            video_db.updated_at = video.updated_at
            await db.commit()
            await db.refresh(video_db)
            
    else:
        video_db = models.YouTubeVideoLatest(
            ch_id=ch_id,
            id=video.id,
            title=video.title,
            thumbnails=video.thumbnails,
            url=video.url,
            description=video.description,
            play_count=video.play_count,
            like_count=video.like_count,
            comment_count=video.comment_count,
            status=video.status,
            current_viewers=video.current_viewers,
            ss_time=video.ss_time,
            as_time=video.as_time,
            ae_time=video.ae_time,
            created_at=video.created_at,
            updated_at=video.updated_at
        )
        db.add(video_db)
        await db.commit()
        await db.refresh(video_db)
    return

async def update_ytvideo_old(db: AsyncSession, ch_id: str, video: schemas.YouTubeVideo):
    video_db = await get_ytvideo_old(db, id=video.id)
    if video_db:
        if video_db.title!=video.title or video_db.description!=video.description or video_db.play_count!=video.play_count or video_db.like_count!=video.like_count or video_db.comment_count!=video.comment_count or video_db.current_viewers!=video.current_viewers or video_db.status!=video.status or video_db.ss_time!=video.ss_time or video_db.as_time!=video.as_time or video_db.ae_time!=video.ae_time:
            video_db.title = video.title
            video_db.thumbnails = video.thumbnails
            video_db.url = video.url
            video_db.description = video.description
            video_db.play_count = video.play_count
            video_db.like_count = video.like_count
            video_db.comment_count = video.comment_count
            video_db.status = video.status
            video_db.current_viewers = video.current_viewers
            video_db.ss_time = video.ss_time
            video_db.as_time = video.as_time
            video_db.ae_time = video.ae_time
            video_db.updated_at = video.updated_at
            await db.commit()
            await db.refresh(video_db)
            
    else:
        video_db = models.YouTubeVideoOld(
            ch_id=ch_id,
            id=video.id,
            title=video.title,
            thumbnails=video.thumbnails,
            url=video.url,
            description=video.description,
            play_count=video.play_count,
            like_count=video.like_count,
            comment_count=video.comment_count,
            status=video.status,
            current_viewers=video.current_viewers,
            ss_time=video.ss_time,
            as_time=video.as_time,
            ae_time=video.ae_time,
            created_at=video.created_at,
            updated_at=video.updated_at
        )
        db.add(video_db)
        await db.commit()
        await db.refresh(video_db)
    return


# Twitter Space
async def get_twspace(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitterSpaceLatest).where(models.TwitterSpaceLatest.id == id)))
        twspace_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if twspace_db:
        return twspace_db[0]
    else:
        return twspace_db

async def get_twspace_old(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitterSpaceOld).where(models.TwitterSpaceOld.id == id)))
        twspace_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if twspace_db:
        return twspace_db[0]
    else:
        return twspace_db

async def get_twspaces_date(db: AsyncSession):
    try:
        result = await (db.execute(select(models.TwitterSpaceLatest).order_by(desc(models.TwitterSpaceLatest.created_at))))
        twspaces_db = result.all()
    except Exception as e:
        logger.error(e)
        return []
    if twspaces_db:
        return twspaces_db[0]
    else:
        return twspaces_db

async def get_twspaces_date_old(db: AsyncSession):
    try:
        result = await (db.execute(select(models.TwitterSpaceOld).order_by(desc(models.TwitterSpaceOld.created_at))))
        twspaces_db = result.all()
    except Exception as e:
        logger.error(e)
        return []
    if twspaces_db:
        return twspaces_db[0]
    else:
        return twspaces_db

async def update_twspace(db: AsyncSession, tw_id: str, space: schemas.TwitterSpace):
    space_db = await get_twspace(db, id=space.id)
    if space_db:
        if space_db.title!=space.title or space_db.audience_count!=space.audience_count or space_db.status!=space.status or space_db.ss_time!=space.ss_time or space_db.as_time!=space.as_time or space_db.ae_time!=space.ae_time:
            space_db.title = space.title
            space_db.url = space.url
            space_db.status = space.status
            space_db.audience_count = space.audience_count
            space_db.ss_time = space.ss_time
            space_db.as_time = space.as_time
            space_db.ae_time = space.ae_time
            space_db.updated_at = space.updated_at
            await db.commit()
            await db.refresh(space_db)
            
    else:
        space_db = models.TwitterSpaceLatest(
            tw_id=tw_id,
            id=space.id,
            title=space.title,
            url=space.url,
            status=space.status,
            audience_count=space.audience_count,
            ss_time=space.ss_time,
            as_time=space.as_time,
            ae_time=space.ae_time,
            created_at=space.created_at,
            updated_at=space.updated_at
        )
        db.add(space_db)
        await db.commit()
        await db.refresh(space_db)
    return

async def update_twspace_old(db: AsyncSession, tw_id: str, space: schemas.TwitterSpace):
    space_db = await get_twspace_old(db, id=space.id)
    if space_db:
        if space_db.title!=space.title or space_db.audience_count!=space.audience_count or space_db.status!=space.status or space_db.ss_time!=space.ss_time or space_db.as_time!=space.as_time or space_db.ae_time!=space.ae_time:
            space_db.title = space.title
            space_db.url = space.url
            space_db.status = space.status
            space_db.audience_count = space.audience_count
            space_db.ss_time = space.ss_time
            space_db.as_time = space.as_time
            space_db.ae_time = space.ae_time
            space_db.updated_at = space.updated_at
            await db.commit()
            await db.refresh(space_db)
            
    else:
        space_db = models.TwitterSpaceOld(
            tw_id=tw_id,
            id=space.id,
            title=space.title,
            url=space.url,
            status=space.status,
            audience_count=space.audience_count,
            ss_time=space.ss_time,
            as_time=space.as_time,
            ae_time=space.ae_time,
            created_at=space.created_at,
            updated_at=space.updated_at
        )
        db.add(space_db)
        await db.commit()
        await db.refresh(space_db)
    return


# Twitch Stream
async def get_tcstream(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitchStreamLatest).where(models.TwitchStreamLatest.id == id)))
        tcstream_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if tcstream_db:
        return tcstream_db[0]
    else:
        return tcstream_db

async def get_tcstream_old(db: AsyncSession, id: str):
    try:
        result = await (db.execute(select(models.TwitchStreamOld).where(models.TwitchStreamOld.id == id)))
        tcstream_db = result.first()
    except Exception as e:
        logger.error(e)
        return None
    if tcstream_db:
        return tcstream_db[0]
    else:
        return tcstream_db

async def get_tcstreams_date(db: AsyncSession):
    try:
        result = await (db.execute(select(models.TwitchStreamLatest).order_by(desc(models.TwitchStreamLatest.created_at))))
        tcstreams_db = result.all()
    except Exception as e:
        logger.error(e)
        return []
    if tcstreams_db:
        return tcstreams_db[0]
    else:
        return tcstreams_db

async def get_tcstreams_date_old(db: AsyncSession):
    try:
        result = await (db.execute(select(models.TwitchStreamOld).order_by(desc(models.TwitchStreamOld.created_at))))
        tcstreams_db = result.all()
    except Exception as e:
        logger.error(e)
        return []
    if tcstreams_db:
        return tcstreams_db[0]
    else:
        return tcstreams_db

async def update_tcstream(db: AsyncSession, ch_id: str, stream: schemas.TwitchStream):
    stream_db = await get_tcstream(db, id=stream.id)
    if stream_db:
        if stream_db.title!=stream.title or stream_db.description!=stream.description or stream_db.thumbnail!=stream.thumbnail or stream_db.view_count!=stream.view_count or stream_db.current_viewers!=stream.current_viewers or stream_db.status!=stream.status or stream_db.as_time!=stream.as_time or stream_db.ae_time!=stream.ae_time:
            stream_db.stream_id = stream.stream_id
            stream_db.title = stream.title
            stream_db.thumbnail = stream.thumbnail
            stream_db.description = stream.description
            stream_db.url = stream.url
            stream_db.view_count = stream.view_count
            stream_db.status = stream.status
            stream_db.type = stream.type
            stream_db.game_id = stream.game_id
            stream_db.game_name = stream.game_name
            stream_db.current_viewers = stream.current_viewers
            stream_db.as_time = stream.as_time
            stream_db.ae_time = stream.ae_time
            stream_db.updated_at = stream.updated_at
            await db.commit()
            await db.refresh(stream_db)
            
    else:
        stream_db = models.TwitchStreamLatest(
            ch_id=ch_id,
            id=stream.id,
            stream_id=stream.stream_id,
            title=stream.title,
            description=stream.description,
            thumbnail=stream.thumbnail,
            url=stream.url,
            status=stream.status,
            type=stream.type,
            game_id=stream.game_id,
            game_name=stream.game_name,
            current_viewers=stream.current_viewers,
            view_count=stream.view_count,
            as_time=stream.as_time,
            ae_time=stream.ae_time,
            created_at=stream.created_at,
            updated_at=stream.updated_at
        )
        db.add(stream_db)
        await db.commit()
        await db.refresh(stream_db)
    return

async def update_tcstream_old(db: AsyncSession, ch_id: str, stream: schemas.TwitchStream):
    stream_db = await get_tcstream_old(db, id=stream.id)
    if stream_db:
        if stream_db.title!=stream.title or stream_db.description!=stream.description or stream_db.thumbnail!=stream.thumbnail or stream_db.view_count!=stream.view_count or stream_db.current_viewers!=stream.current_viewers or stream_db.status!=stream.status or stream_db.as_time!=stream.as_time or stream_db.ae_time!=stream.ae_time:
            stream_db.stream_id = stream.stream_id
            stream_db.title = stream.title
            stream_db.thumbnail = stream.thumbnail
            stream_db.description = stream.description
            stream_db.url = stream.url
            stream_db.view_count = stream.view_count
            stream_db.status = stream.status
            stream_db.type = stream.type
            stream_db.game_id = stream.game_id
            stream_db.game_name = stream.game_name
            stream_db.current_viewers = stream.current_viewers
            stream_db.as_time = stream.as_time
            stream_db.ae_time = stream.ae_time
            stream_db.updated_at = stream.updated_at
            await db.commit()
            await db.refresh(stream_db)
            
    else:
        stream_db = models.TwitchStreamOld(
            ch_id=ch_id,
            id=stream.id,
            stream_id=stream.stream_id,
            title=stream.title,
            description=stream.description,
            thumbnail=stream.thumbnail,
            url=stream.url,
            status=stream.status,
            type=stream.type,
            game_id=stream.game_id,
            game_name=stream.game_name,
            current_viewers=stream.current_viewers,
            view_count=stream.view_count,
            as_time=stream.as_time,
            ae_time=stream.ae_time,
            created_at=stream.created_at,
            updated_at=stream.updated_at
        )
        db.add(stream_db)
        await db.commit()
        await db.refresh(stream_db)
    return