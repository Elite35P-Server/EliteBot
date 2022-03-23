from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, PickleType, JSON, Text
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from datetime import datetime as dt
from cogs.db import Base

class YouTubeChannelLatest(Base):
    __tablename__ = "yt_channel_latest"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    name = Column(String(256))
    icon = Column(String(135))
    description = Column(Text)
    subsc_count = Column(Integer)
    play_count = Column(Integer)
    video_count = Column(Integer)
    status = Column(String(8), default='none')
    videos = relationship('YouTubeVideoLatest', back_populates='yt_channel')
    #comments = relationship('YouTubeComment', back_populates='yt_channel')
    #live_comments = relationship('YouTubeLiveComment', back_populates='yt_channel')
    updated_at = Column(DateTime, default=dt.utcnow, nullable=True)


class TwitterAccountLatest(Base):
    __tablename__ = "tw_account_latest"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    display_id = Column(String(50))
    name = Column(String(50))
    icon = Column(String(135))
    description = Column(Text)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    tweet_count = Column(Integer)
    status = Column(String(9), default='none')
    space = relationship('TwitterSpaceLatest', back_populates='tw_account')
    tweet = relationship('TwitterTweetLatest', back_populates='tw_account')
    updated_at = Column(DateTime, default=dt.utcnow)


class TwitchChannelLatest(Base):
    __tablename__ = "tc_channel_latest"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    display_id = Column(String(35))
    name = Column(String(35))
    icon = Column(String(135))
    offline_img = Column(String(135))
    description = Column(String(512))
    subsc_count = Column(Integer)
    play_count = Column(Integer)
    status = Column(String(8), default='none')
    streams = relationship('TwitchStreamLatest', back_populates='tc_channel')
    updated_at = Column(DateTime, default=dt.utcnow)
    

class YouTubeVideoLatest(Base):
    __tablename__ = "yt_video_latest"

    ch_id = Column(String(35), ForeignKey('yt_channel_latest.id'))
    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    title = Column(String(135))
    thumbnails = Column(JSON(1024), default={})
    description = Column(String(8500))
    url = Column(String(35))
    play_count = Column(Integer)
    like_count = Column(Integer)
    comment_count = Column(Integer)
    #comments = relationship('YouTubeComment', back_populates='yt_video')
    #live_comments = relationship('YouTubeLiveComment', back_populates='yt_video')
    status = Column(String(8), default='none')
    current_viewers = Column(Integer, nullable=True)
    ss_time = Column(DateTime, nullable=True)
    as_time = Column(DateTime, nullable=True)
    ae_time = Column(DateTime, nullable=True)
    yt_channel = relationship('YouTubeChannelLatest', back_populates='videos')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)
    

class TwitterSpaceLatest(Base):
    __tablename__ = "tw_space_latest"

    tw_id = Column(String(35), ForeignKey('tw_account_latest.id'))
    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    title = Column(String(135))
    url = Column(String(135))
    status = Column(String(9), default='none')
    audience_count = Column(Integer, nullable=True)
    ss_time = Column(DateTime, nullable=True)
    as_time = Column(DateTime, nullable=True)
    ae_time = Column(DateTime, nullable=True)
    tw_account = relationship('TwitterAccountLatest', back_populates='space')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)
    

class TwitterTweetLatest(Base):
    __tablename__ = "tw_tweet_latest"

    user_id = Column(String(35), ForeignKey('tw_account_latest.id'))
    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    text = Column(Text)
    hashtags = Column(MutableList.as_mutable(PickleType), default=[])
    lang = Column(String(5))
    url = Column(String(256))
    possibly_sensitive = Column(Boolean, default=False)
    display_id = Column(String(50))
    name = Column(String(50))
    icon = Column(String(135))
    matching_rules = Column(MutableList.as_mutable(PickleType), default=[])
    tw_account = relationship('TwitterAccountLatest', back_populates='tweet')
    created_at = Column(DateTime, default=dt.utcnow)


class TwitchStreamLatest(Base):
    __tablename__ = "tc_stream_latest"

    ch_id = Column(String(35), ForeignKey('tc_channel_latest.id'))
    id = Column(String(36), primary_key=True, nullable=False, unique=True)
    stream_id = Column(String(36))
    title = Column(String(135))
    thumbnail = Column(String(256))
    description = Column(String(512))
    url = Column(String(135))
    type = Column(String(9))
    game_id = Column(String(35), nullable=True)
    game_name = Column(String(35), nullable=True)
    status = Column(String(8), default='none')
    current_viewers = Column(Integer, nullable=True)
    view_count = Column(Integer)
    as_time = Column(DateTime, nullable=True)
    ae_time = Column(DateTime, nullable=True)
    tc_channel = relationship('TwitchChannelLatest', back_populates='streams')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)
    
    
    
     
class YouTubeChannelOld(Base):
    __tablename__ = "yt_channel_old"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    name = Column(String(256))
    icon = Column(String(135))
    description = Column(Text)
    subsc_count = Column(Integer)
    play_count = Column(Integer)
    video_count = Column(Integer)
    status = Column(String(8), default='none')
    videos = relationship('YouTubeVideoOld', back_populates='yt_channel')
    #comments = relationship('YouTubeComment', back_populates='yt_channel')
    #live_comments = relationship('YouTubeLiveComment', back_populates='yt_channel')
    updated_at = Column(DateTime, default=dt.utcnow, nullable=True)


class TwitterAccountOld(Base):
    __tablename__ = "tw_account_old"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    display_id = Column(String(50))
    name = Column(String(50))
    icon = Column(String(135))
    description = Column(Text)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    tweet_count = Column(Integer)
    status = Column(String(9), default='none')
    space = relationship('TwitterSpaceOld', back_populates='tw_account')
    tweet = relationship('TwitterTweetOld', back_populates='tw_account')
    updated_at = Column(DateTime, default=dt.utcnow)


class TwitchChannelOld(Base):
    __tablename__ = "tc_channel_old"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    display_id = Column(String(35))
    name = Column(String(35))
    icon = Column(String(135))
    offline_img = Column(String(135))
    description = Column(String(512))
    subsc_count = Column(Integer)
    play_count = Column(Integer)
    status = Column(String(8), default='none')
    streams = relationship('TwitchStreamOld', back_populates='tc_channel')
    updated_at = Column(DateTime, default=dt.utcnow)
    

class YouTubeVideoOld(Base):
    __tablename__ = "yt_video_old"

    ch_id = Column(String(35), ForeignKey('yt_channel_old.id'))
    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    title = Column(String(135))
    thumbnails = Column(JSON(1024), default={})
    description = Column(String(8500))
    url = Column(String(35))
    play_count = Column(Integer)
    like_count = Column(Integer)
    comment_count = Column(Integer)
    #comments = relationship('YouTubeComment', back_populates='yt_video')
    #live_comments = relationship('YouTubeLiveComment', back_populates='yt_video')
    status = Column(String(8), default='none')
    current_viewers = Column(Integer, nullable=True)
    ss_time = Column(DateTime, nullable=True)
    as_time = Column(DateTime, nullable=True)
    ae_time = Column(DateTime, nullable=True)
    yt_channel = relationship('YouTubeChannelOld', back_populates='videos')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)
    

class TwitterSpaceOld(Base):
    __tablename__ = "tw_space_old"

    tw_id = Column(String(35), ForeignKey('tw_account_old.id'))
    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    title = Column(String(135))
    url = Column(String(135))
    status = Column(String(9), default='none')
    audience_count = Column(Integer, nullable=True)
    ss_time = Column(DateTime, nullable=True)
    as_time = Column(DateTime, nullable=True)
    ae_time = Column(DateTime, nullable=True)
    tw_account = relationship('TwitterAccountOld', back_populates='space')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)
    

class TwitterTweetOld(Base):
    __tablename__ = "tw_tweet_old"

    user_id = Column(String(35), ForeignKey('tw_account_old.id'))
    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    text = Column(Text)
    hashtags = Column(MutableList.as_mutable(PickleType), default=[])
    lang = Column(String(5))
    url = Column(String(256))
    possibly_sensitive = Column(Boolean, default=False)
    display_id = Column(String(50))
    name = Column(String(50))
    icon = Column(String(135))
    matching_rules = Column(MutableList.as_mutable(PickleType), default=[])
    tw_account = relationship('TwitterAccountOld', back_populates='tweet')
    created_at = Column(DateTime, default=dt.utcnow)


class TwitchStreamOld(Base):
    __tablename__ = "tc_stream_old"

    ch_id = Column(String(35), ForeignKey('tc_channel_old.id'))
    id = Column(String(36), primary_key=True, nullable=False, unique=True)
    stream_id = Column(String(36))
    title = Column(String(135))
    thumbnail = Column(String(256))
    description = Column(String(512))
    url = Column(String(135))
    type = Column(String(9))
    game_id = Column(String(35), nullable=True)
    game_name = Column(String(35), nullable=True)
    status = Column(String(8), default='none')
    current_viewers = Column(Integer, nullable=True)
    view_count = Column(Integer)
    as_time = Column(DateTime, nullable=True)
    ae_time = Column(DateTime, nullable=True)
    tc_channel = relationship('TwitchChannelOld', back_populates='streams')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)