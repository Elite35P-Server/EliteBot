from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, asc, select
from sqlalchemy.sql.expression import delete
import models, schemas


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
    ).filter(models.YouTubeChannelLatest.id == id)))
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
    ).filter(models.YouTubeChannelOld.id == id)))
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
            #await db.refresh(video_db)
            
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
            #await db.refresh(video_db)
            
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