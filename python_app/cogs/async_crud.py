from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, asc, select
from sqlalchemy.sql.expression import delete
from cogs import models, schemas

# YouTube Channel
async def get_ytch(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.YouTubeChannelLatest.id,
        models.YouTubeChannelLatest.name,
        models.YouTubeChannelLatest.description,
        models.YouTubeChannelLatest.icon,
        models.YouTubeChannelLatest.status,
        models.YouTubeChannelLatest.play_count,
        models.YouTubeChannelLatest.subsc_count,
        models.YouTubeChannelLatest.video_count,
        models.YouTubeChannelLatest.updated_at
    ).where(models.YouTubeChannelLatest.id == id)))
    return result.first()

async def get_ytch_old(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.YouTubeChannelOld.id,
        models.YouTubeChannelOld.name,
        models.YouTubeChannelOld.description,
        models.YouTubeChannelOld.icon,
        models.YouTubeChannelOld.status,
        models.YouTubeChannelOld.play_count,
        models.YouTubeChannelOld.subsc_count,
        models.YouTubeChannelOld.video_count,
        models.YouTubeChannelOld.updated_at
    ).where(models.YouTubeChannelOld.id == id)))
    return result.first()

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
    result = await (db.execute(select(
        models.TwitterAccountLatest.id,
        models.TwitterAccountLatest.display_id,
        models.TwitterAccountLatest.name,
        models.TwitterAccountLatest.icon,
        models.TwitterAccountLatest.description,
        models.TwitterAccountLatest.status,
        models.TwitterAccountLatest.followers_count,
        models.TwitterAccountLatest.following_count,
        models.TwitterAccountLatest.tweet_count,
        models.TwitterAccountLatest.updated_at
    ).where(models.TwitterAccountLatest.id == id)))
    return result.first()

async def get_twac_old(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.TwitterAccountOld.id,
        models.TwitterAccountOld.display_id,
        models.TwitterAccountOld.name,
        models.TwitterAccountOld.icon,
        models.TwitterAccountOld.description,
        models.TwitterAccountOld.status,
        models.TwitterAccountOld.followers_count,
        models.TwitterAccountOld.following_count,
        models.TwitterAccountOld.tweet_count,
        models.TwitterAccountOld.updated_at
    ).where(models.TwitterAccountOld.id == id)))
    return result.first()

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
        await db.add(tw_db)
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
        await db.add(tw_db)
        await db.commit()
        await db.refresh(tw_db)
    return


# Twitch Channel
async def get_tcch(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.TwitchChannelLatest.id,
        models.TwitchChannelLatest.display_id,
        models.TwitchChannelLatest.name,
        models.TwitchChannelLatest.icon,
        models.TwitchChannelLatest.offline_img,
        models.TwitchChannelLatest.description,
        models.TwitchChannelLatest.status,
        models.TwitchChannelLatest.subsc_count,
        models.TwitchChannelLatest.play_count,
        models.TwitchChannelLatest.updated_at
    ).where(models.TwitchChannelLatest.id == id)))
    return result.first()

async def get_tcch_old(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.TwitchChannelOld.id,
        models.TwitchChannelOld.display_id,
        models.TwitchChannelOld.name,
        models.TwitchChannelOld.icon,
        models.TwitchChannelOld.offline_img,
        models.TwitchChannelOld.description,
        models.TwitchChannelOld.status,
        models.TwitchChannelOld.subsc_count,
        models.TwitchChannelOld.play_count,
        models.TwitchChannelOld.updated_at
    ).where(models.TwitchChannelOld.id == id)))
    return result.first()

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
        await db.add(ch_db)
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
        await db.add(ch_db)
        await db.commit()
        await db.refresh(ch_db)
    return


# YouTube Video
async def get_ytvideo(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.YouTubeVideoLatest.id,
        models.YouTubeVideoLatest.title,
        models.YouTubeVideoLatest.url,
        models.YouTubeVideoLatest.thumbnails,
        models.YouTubeVideoLatest.description,
        models.YouTubeVideoLatest.status,
        models.YouTubeVideoLatest.play_count,
        models.YouTubeVideoLatest.like_count,
        models.YouTubeVideoLatest.comment_count,
        models.YouTubeVideoLatest.current_viewers,
        models.YouTubeVideoLatest.ss_time,
        models.YouTubeVideoLatest.as_time,
        models.YouTubeVideoLatest.ae_time,
        models.YouTubeVideoLatest.created_at,
        models.YouTubeVideoLatest.updated_at
    ).where(models.YouTubeVideoLatest.id == id)))
    return result.first()

async def get_ytvideo_old(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.YouTubeVideoOld.id,
        models.YouTubeVideoOld.title,
        models.YouTubeVideoOld.url,
        models.YouTubeVideoOld.thumbnails,
        models.YouTubeVideoOld.description,
        models.YouTubeVideoOld.status,
        models.YouTubeVideoOld.play_count,
        models.YouTubeVideoOld.like_count,
        models.YouTubeVideoOld.comment_count,
        models.YouTubeVideoOld.current_viewers,
        models.YouTubeVideoOld.ss_time,
        models.YouTubeVideoOld.as_time,
        models.YouTubeVideoOld.ae_time,
        models.YouTubeVideoOld.created_at,
        models.YouTubeVideoOld.updated_at
    ).where(models.YouTubeVideoOld.id == id)))
    return result.first()

async def get_ytvideos_date(db: AsyncSession):
    result = await (db.execute(select(
        models.YouTubeVideoLatest.id,
        models.YouTubeVideoLatest.title,
        models.YouTubeVideoLatest.url,
        models.YouTubeVideoLatest.thumbnails,
        models.YouTubeVideoLatest.description,
        models.YouTubeVideoLatest.status,
        models.YouTubeVideoLatest.play_count,
        models.YouTubeVideoLatest.like_count,
        models.YouTubeVideoLatest.comment_count,
        models.YouTubeVideoLatest.current_viewers,
        models.YouTubeVideoLatest.ss_time,
        models.YouTubeVideoLatest.as_time,
        models.YouTubeVideoLatest.ae_time,
        models.YouTubeVideoLatest.created_at,
        models.YouTubeVideoLatest.updated_at
    ).order_by(desc(models.YouTubeVideoLatest.created_at))))
    return result.all()

async def get_ytvideos_date_old(db: AsyncSession):
    result = await (db.execute(select(
        models.YouTubeVideoOld.id,
        models.YouTubeVideoOld.title,
        models.YouTubeVideoOld.url,
        models.YouTubeVideoOld.thumbnails,
        models.YouTubeVideoOld.description,
        models.YouTubeVideoOld.status,
        models.YouTubeVideoOld.play_count,
        models.YouTubeVideoOld.like_count,
        models.YouTubeVideoOld.comment_count,
        models.YouTubeVideoOld.current_viewers,
        models.YouTubeVideoOld.ss_time,
        models.YouTubeVideoOld.as_time,
        models.YouTubeVideoOld.ae_time,
        models.YouTubeVideoOld.created_at,
        models.YouTubeVideoOld.updated_at
    ).order_by(desc(models.YouTubeVideoOld.created_at))))
    return result.all()

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
        await db.add(video_db)
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
        await db.add(video_db)
        await db.commit()
        await db.refresh(video_db)
    return


# Twitter Space
async def get_twspace(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.TwitterSpaceLatest.id,
        models.TwitterSpaceLatest.title,
        models.TwitterSpaceLatest.url,
        models.TwitterSpaceLatest.status,
        models.TwitterSpaceLatest.audience_count,
        models.TwitterSpaceLatest.ss_time,
        models.TwitterSpaceLatest.as_time,
        models.TwitterSpaceLatest.ae_time,
        models.TwitterSpaceLatest.created_at,
        models.TwitterSpaceLatest.updated_at
    ).where(models.TwitterSpaceLatest.id == id)))
    return result.first()

async def get_twspace_old(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.TwitterSpaceOld.id,
        models.TwitterSpaceOld.title,
        models.TwitterSpaceOld.url,
        models.TwitterSpaceOld.status,
        models.TwitterSpaceOld.audience_count,
        models.TwitterSpaceOld.ss_time,
        models.TwitterSpaceOld.as_time,
        models.TwitterSpaceOld.ae_time,
        models.TwitterSpaceOld.created_at,
        models.TwitterSpaceOld.updated_at
    ).where(models.TwitterSpaceOld.id == id)))
    return result.first()

async def get_twspaces_date(db: AsyncSession):
    result = await (db.execute(select(
        models.TwitterSpaceLatest.id,
        models.TwitterSpaceLatest.title,
        models.TwitterSpaceLatest.url,
        models.TwitterSpaceLatest.status,
        models.TwitterSpaceLatest.audience_count,
        models.TwitterSpaceLatest.ss_time,
        models.TwitterSpaceLatest.as_time,
        models.TwitterSpaceLatest.ae_time,
        models.TwitterSpaceLatest.created_at,
        models.TwitterSpaceLatest.updated_at
    ).order_by(desc(models.TwitterSpaceLatest.created_at))))
    return result.all()

async def get_twspaces_date_old(db: AsyncSession):
    result = await (db.execute(select(
        models.TwitterSpaceOld.id,
        models.TwitterSpaceOld.title,
        models.TwitterSpaceOld.url,
        models.TwitterSpaceOld.status,
        models.TwitterSpaceOld.audience_count,
        models.TwitterSpaceOld.ss_time,
        models.TwitterSpaceOld.as_time,
        models.TwitterSpaceOld.ae_time,
        models.TwitterSpaceOld.created_at,
        models.TwitterSpaceOld.updated_at
    ).order_by(desc(models.TwitterSpaceOld.created_at))))
    return result.all()

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
        await db.add(space_db)
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
        await db.add(space_db)
        await db.commit()
        await db.refresh(space_db)
    return


# Twitch Stream
async def get_tcstream(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.TwitchStreamLatest.id,
        models.TwitchStreamLatest.title,
        models.TwitchStreamLatest.url,
        models.TwitchStreamLatest.thumbnail,
        models.TwitchStreamLatest.description,
        models.TwitchStreamLatest.status,
        models.TwitchStreamLatest.view_count,
        models.TwitchStreamLatest.current_viewers,
        models.TwitchStreamLatest.as_time,
        models.TwitchStreamLatest.ae_time,
        models.TwitchStreamLatest.created_at,
        models.TwitchStreamLatest.updated_at
    ).where(models.TwitchStreamLatest.id == id)))
    return result.first()

async def get_tcstream_old(db: AsyncSession, id: str):
    result = await (db.execute(select(
        models.TwitchStreamOld.id,
        models.TwitchStreamOld.title,
        models.TwitchStreamOld.url,
        models.TwitchStreamOld.thumbnail,
        models.TwitchStreamOld.description,
        models.TwitchStreamOld.status,
        models.TwitchStreamOld.view_count,
        models.TwitchStreamOld.current_viewers,
        models.TwitchStreamOld.as_time,
        models.TwitchStreamOld.ae_time,
        models.TwitchStreamOld.created_at,
        models.TwitchStreamOld.updated_at
    ).where(models.TwitchStreamOld.id == id)))
    return result.first()

async def get_tcstreams_date(db: AsyncSession):
    result = await (db.execute(select(
        models.TwitchStreamLatest.id,
        models.TwitchStreamLatest.title,
        models.TwitchStreamLatest.url,
        models.TwitchStreamLatest.thumbnail,
        models.TwitchStreamLatest.description,
        models.TwitchStreamLatest.status,
        models.TwitchStreamLatest.view_count,
        models.TwitchStreamLatest.current_viewers,
        models.TwitchStreamLatest.as_time,
        models.TwitchStreamLatest.ae_time,
        models.TwitchStreamLatest.created_at,
        models.TwitchStreamLatest.updated_at
    ).order_by(desc(models.TwitchStreamLatest.created_at))))
    return result.all()

async def get_tcstreams_date_old(db: AsyncSession):
    result = await (db.execute(select(
        models.TwitchStreamOld.id,
        models.TwitchStreamOld.title,
        models.TwitchStreamOld.url,
        models.TwitchStreamOld.thumbnail,
        models.TwitchStreamOld.description,
        models.TwitchStreamOld.status,
        models.TwitchStreamOld.view_count,
        models.TwitchStreamOld.current_viewers,
        models.TwitchStreamOld.as_time,
        models.TwitchStreamOld.ae_time,
        models.TwitchStreamOld.created_at,
        models.TwitchStreamOld.updated_at
    ).order_by(desc(models.TwitchStreamOld.created_at))))
    return result.all()

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
        await db.add(stream_db)
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
        await db.add(stream_db)
        await db.commit()
        await db.refresh(stream_db)
    return