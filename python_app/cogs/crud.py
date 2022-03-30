from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from sqlalchemy.sql.expression import delete
from cogs import models
from cogs import schemas


def get_ytch(db: Session, id: str):
    return db.query(models.YouTubeChannelLatest).filter(models.YouTubeChannelLatest.id == id).first()

def get_ytch_old(db: Session, id: str):
    return db.query(models.YouTubeChannelOld).filter(models.YouTubeChannelOld.id == id).first()

def get_twac(db: Session, id: str):
    return db.query(models.TwitterAccountLatest).filter(models.TwitterAccountLatest.id == id).first()

def get_twac_old(db: Session, id: str):
    return db.query(models.TwitterAccountOld).filter(models.TwitterAccountOld.id == id).first()

def get_tcch(db: Session, id: str):
    return db.query(models.TwitchChannelLatest).filter(models.TwitchChannelLatest.id == id).first()

def get_tcch_old(db: Session, id: str):
    return db.query(models.TwitchChannelOld).filter(models.TwitchChannelOld.id == id).first()

def get_ytvideo(db: Session, id: str):
    return db.query(models.YouTubeVideoLatest).filter(models.YouTubeVideoLatest.id == id).first()

def get_ytvideo_old(db: Session, id: str):
    return db.query(models.YouTubeVideoOld).filter(models.YouTubeVideoOld.id == id).first()

def get_ytvideos(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.YouTubeVideoLatest).offset(skip).limit(limit).all()

def get_ytvideos_date(db: Session):
    return db.query(models.YouTubeVideoLatest).order_by(desc(models.YouTubeVideoLatest.created_at)).all()

def get_ytvideos_date_old(db: Session):
    return db.query(models.YouTubeVideoOld).order_by(desc(models.YouTubeVideoOld.created_at)).all()

def get_ytvideos_date_byuser(db: Session, ch_id: str, skip: int = 0, limit: int = 5):
    return db.query(models.YouTubeVideoLatest).filter(models.YouTubeVideoLatest.ch_id == ch_id).order_by(desc(models.YouTubeVideoLatest.created_at)).offset(skip).limit(limit).all()

def get_ytvideos_sstime(db: Session):
    return db.query(models.YouTubeVideoLatest).order_by(desc(models.YouTubeVideoLatest.ss_time)).all()

def get_ytvideos_sstime_old(db: Session):
    return db.query(models.YouTubeVideoOld).order_by(desc(models.YouTubeVideoOld.ss_time)).all()


def get_ytvideos_playcount(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.YouTubeVideoLatest).order_by(desc(models.YouTubeVideoLatest.play_count)).offset(skip).limit(limit).all()

def get_ytvideos_likecount(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.YouTubeVideoLatest).order_by(desc(models.YouTubeVideoLatest.like_count)).offset(skip).limit(limit).all()

def get_ytvideos_commentcount(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.YouTubeVideoLatest).order_by(desc(models.YouTubeVideoLatest.comment_count)).offset(skip).limit(limit).all()

def get_ytvideos_status(db: Session, status: str):
    return db.query(models.YouTubeVideoLatest).filter(models.YouTubeVideoLatest.status == status).order_by(desc(models.YouTubeVideoLatest.ss_time)).all()

def get_twspace(db: Session, id: str):
    return db.query(models.TwitterSpaceLatest).filter(models.TwitterSpaceLatest.id == id).first()

def get_twspaces(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.TwitterSpaceLatest).offset(skip).limit(limit).all()

def get_twspaces_date(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.TwitterSpaceLatest).order_by(desc(models.TwitterSpaceLatest.created_at)).offset(skip).limit(limit).all()

def get_twspaces_sstime(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.TwitterSpaceLatest).order_by(desc(models.TwitterSpaceLatest.ss_time)).offset(skip).limit(limit).all()

def get_twspaces_status(db: Session, status: str, skip: int = 0, limit: int = 5):
    return db.query(models.TwitterSpaceLatest).filter(models.TwitterSpaceLatest.status == status).order_by(desc(models.TwitterSpaceLatest.created_at)).offset(skip).limit(limit).all()

def get_twte(db: Session, id: str):
    return db.query(models.TwitterTweetLatest).filter(models.TwitterTweetLatest.id == id).first()

def get_twtes(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.TwitterTweetLatest).offset(skip).limit(limit).all()

def get_twtes_date(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.TwitterTweetLatest).order_by(desc(models.TwitterTweetLatest.created_at)).offset(skip).limit(limit).all()

def get_twtes_date_byuser(db: Session, user_id: str, skip: int = 0, limit: int = 5):
    return db.query(models.TwitterTweetLatest).filter(models.TwitterTweetLatest.user_id == user_id).order_by(desc(models.TwitterTweetLatest.created_at)).offset(skip).limit(limit).all()

def get_tcstream(db: Session, id: str):
    return db.query(models.TwitchStreamLatest).filter(models.TwitchStreamLatest.id == id).first()

def get_tcstream_old(db: Session, id: str):
    return db.query(models.TwitchStreamOld).filter(models.TwitchStreamOld.id == id).first()

def get_tcstreams(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.TwitchStreamLatest).offset(skip).limit(limit).all()

def get_tcstreams_date(db: Session):
    return db.query(models.TwitchStreamLatest).order_by(desc(models.TwitchStreamLatest.created_at)).all()

def get_tcstreams_date_old(db: Session):
    return db.query(models.TwitchStreamOld).order_by(desc(models.TwitchStreamOld.created_at)).all()

def get_tcstreams_status(db: Session, status: str, skip: int = 0, limit: int = 5):
    return db.query(models.TwitchStreamLatest).filter(models.TwitchStreamLatest.status == status).order_by(desc(models.TwitchStreamLatest.created_at)).offset(skip).limit(limit).all()

def update_ytch(db: Session, ch: schemas.YouTubeCh):
    ch_db = get_ytch(db, id=ch.id)
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
            db.commit()
            
    else:
        ch_db = models.YouTubeChannelLatest(id=ch.id,
                                      name=ch.name,
                                      icon=ch.icon,
                                      description=ch.description,
                                      subsc_count=ch.subsc_count,
                                      play_count=ch.play_count,
                                      video_count=ch.video_count,
                                      status=ch.status,
                                      updated_at=ch.updated_at)
        db.add(ch_db)
        db.commit()
        db.refresh(ch_db)

    return ch_db.updated_at

def update_ytch_old(db: Session, ch: schemas.YouTubeCh):
    ch_db = get_ytch_old(db, id=ch.id)
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
            db.commit()
            
    else:
        ch_db = models.YouTubeChannelOld(id=ch.id,
                                      name=ch.name,
                                      icon=ch.icon,
                                      description=ch.description,
                                      subsc_count=ch.subsc_count,
                                      play_count=ch.play_count,
                                      video_count=ch.video_count,
                                      status=ch.status,
                                      updated_at=ch.updated_at)
        db.add(ch_db)
        db.commit()
        db.refresh(ch_db)

    return ch_db.updated_at

def update_twac(db: Session, tw: schemas.Twitter):
    tw_db = get_twac(db, id=tw.id)
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
            db.commit()
            
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
        db.commit()
        db.refresh(tw_db)

    return tw_db.updated_at

def update_twac_old(db: Session, tw: schemas.Twitter):
    tw_db = get_twac_old(db, id=tw.id)
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
            db.commit()
            
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
        db.commit()
        db.refresh(tw_db)

    return tw_db.updated_at

def create_twte(db: Session, te: schemas.TwitterTweet):
    te_db = models.TwitterTweetLatest(
        id=te.id,
        user_id=te.user_id,
        display_id=te.display_id,
        name=te.name,
        icon=te.icon,
        text=te.text,
        hashtags=te.hashtags,
        lang=te.lang,
        possibly_sensitive=te.possibly_sensitive,
        url=te.url,
        matching_rules=te.matching_rules,
        created_at=te.created_at,
    )
    db.add(te_db)
    db.commit()
    db.refresh(te_db)

    return te_db.created_at


def update_tcch(db: Session, ch: schemas.TwitchCh):
    ch_db = get_tcch(db, id=ch.id)
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
            db.commit()
            
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
        db.commit()
        db.refresh(ch_db)

    return ch_db.updated_at

def update_tcch_old(db: Session, ch: schemas.TwitchCh):
    ch_db = get_tcch_old(db, id=ch.id)
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
            db.commit()
            
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
        db.commit()
        db.refresh(ch_db)

    return ch_db.updated_at

def update_ytvideo(db: Session, ch_id: str, video: schemas.YouTubeVideo):
    video_db = get_ytvideo(db, id=video.id)
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
            db.commit()
            
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
        db.commit()
        db.refresh(video_db)

    return video_db.updated_at

def update_ytvideo_old(db: Session, ch_id: str, video: schemas.YouTubeVideo):
    video_db = get_ytvideo_old(db, id=video.id)
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
            db.commit()
            
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
        db.commit()
        db.refresh(video_db)

    return video_db.updated_at


def update_twspace(db: Session, tw_id: str, space: schemas.TwitterSpace):
    space_db = get_twspace(db, id=space.id)
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
            db.commit()
            
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
        db.commit()
        db.refresh(space_db)

    return space_db.updated_at

def update_tcstream(db: Session, ch_id: str, stream: schemas.TwitchStream):
    stream_db = get_tcstream(db, id=stream.id)
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
            db.commit()
            db.refresh(stream_db)
            
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
        db.commit()
        db.refresh(stream_db)

    return stream_db.updated_at

def update_tcstream_old(db: Session, ch_id: str, stream: schemas.TwitchStream):
    stream_db = get_tcstream_old(db, id=stream.id)
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
            db.commit()
            db.refresh(stream_db)
            
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
        db.commit()
        db.refresh(stream_db)

    return stream_db.updated_at