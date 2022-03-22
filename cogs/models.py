from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, PickleType, JSON, Text
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship
from datetime import datetime as dt
from cogs.db import Base

class YouTubeChannel(Base):
    __tablename__ = "yt_channel"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    name = Column(String(256))
    icon = Column(String(135))
    description = Column(Text)
    subsc_count = Column(Integer)
    play_count = Column(Integer)
    video_count = Column(Integer)
    status = Column(String(8), default='none')
    videos = relationship('YouTubeVideo', back_populates='yt_channel')
    #comments = relationship('YouTubeComment', back_populates='yt_channel')
    #live_comments = relationship('YouTubeLiveComment', back_populates='yt_channel')
    updated_at = Column(DateTime, default=dt.utcnow, nullable=True)


class TwitterAccount(Base):
    __tablename__ = "tw_account"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    display_id = Column(String(50))
    name = Column(String(50))
    icon = Column(String(135))
    description = Column(Text)
    followers_count = Column(Integer)
    following_count = Column(Integer)
    tweet_count = Column(Integer)
    status = Column(String(9), default='none')
    space = relationship('TwitterSpace', back_populates='tw_account')
    tweet = relationship('TwitterTweet', back_populates='tw_account')
    updated_at = Column(DateTime, default=dt.utcnow)


class TwitchChannel(Base):
    __tablename__ = "tc_channel"

    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    display_id = Column(String(35))
    name = Column(String(35))
    icon = Column(String(135))
    offline_img = Column(String(135))
    description = Column(String(512))
    subsc_count = Column(Integer)
    play_count = Column(Integer)
    status = Column(String(8), default='none')
    streams = relationship('TwitchStream', back_populates='tc_channel')
    updated_at = Column(DateTime, default=dt.utcnow)
    

class YouTubeVideo(Base):
    __tablename__ = "yt_video"

    ch_id = Column(String(35), ForeignKey('yt_channel.id'))
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
    yt_channel = relationship('YouTubeChannel', back_populates='videos')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)
    

class TwitterSpace(Base):
    __tablename__ = "tw_space"

    tw_id = Column(String(35), ForeignKey('tw_account.id'))
    id = Column(String(35), primary_key=True, nullable=False, unique=True)
    title = Column(String(135))
    url = Column(String(135))
    status = Column(String(9), default='none')
    audience_count = Column(Integer, nullable=True)
    ss_time = Column(DateTime, nullable=True)
    as_time = Column(DateTime, nullable=True)
    ae_time = Column(DateTime, nullable=True)
    tw_account = relationship('TwitterAccount', back_populates='space')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)
    

class TwitterTweet(Base):
    __tablename__ = "tw_tweet"

    user_id = Column(String(35), ForeignKey('tw_account.id'))
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
    tw_account = relationship('TwitterAccount', back_populates='tweet')
    created_at = Column(DateTime, default=dt.utcnow)


class TwitchStream(Base):
    __tablename__ = "tc_stream"

    ch_id = Column(String(35), ForeignKey('tc_channel.id'))
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
    tc_channel = relationship('TwitchChannel', back_populates='streams')
    created_at = Column(DateTime, default=dt.utcnow)
    updated_at = Column(DateTime, default=dt.utcnow)