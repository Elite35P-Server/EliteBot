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