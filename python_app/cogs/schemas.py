from typing import List
from pydantic import BaseModel, Field
from datetime import datetime as dt


class YouTubeVideo(BaseModel):
    id: str = Field("X9zw0QF12Kc", title="YouTube Video ID")
    title: str = Field("サクラカゼ / さくらみこ【オリジナル曲】", title="YouTube Video Title")
    thumbnails: dict = Field({
          "default": {
            "url": "https://i.ytimg.com/vi/X9zw0QF12Kc/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/X9zw0QF12Kc/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/X9zw0QF12Kc/hqdefault.jpg",
            "width": 480,
            "height": 360
          },
          "standard": {
            "url": "https://i.ytimg.com/vi/X9zw0QF12Kc/sddefault.jpg",
            "width": 640,
            "height": 480
          },
          "maxres": {
            "url": "https://i.ytimg.com/vi/X9zw0QF12Kc/maxresdefault.jpg",
            "width": 1280,
            "height": 720
          }
        }, title="YouTube Video Thumbnail Img URL")
    description: str = Field("さくらみこ 2ndオリジナル楽曲『サクラカゼ』...", title="YouTube Video Description")
    url: str = Field("https://youtu.be/X9zw0QF12Kc", title="YouTube Video URL")
    play_count: int = Field(0, title="YouTube Video Play Count")
    like_count: int = Field(0, title="YouTube Video Like Count")
    comment_count: int = Field(0, title="YouTube Video Comment Count")
    status: str = Field("none", title="YouTube Stream Status")
    current_viewers: int = Field(None, title="YouTube Stream Current Viewers")
    ss_time: dt = Field(None,title="Scheduled Stream Start Time")
    as_time: dt = Field(None, title="Actuary Stream Start Time")
    ae_time: dt = Field(None,title="Actuary Stream End Time")
    created_at: dt = Field(dt.utcnow(), title="Video Create Time")
    updated_at: dt = Field(dt.utcnow(), title="Video Update Time")

    class Config:
        orm_mode = True

class TwitterSpace(BaseModel):
    id: str = Field('1zqKVBpgWkPKB', title="Twitter Space ID")
    title: str = Field(None, title="Twitter Space Title")
    url: str = Field('https://twitter.com/i/spaces/1zqKVBpgWkPKB', title="Twitter Space Title")
    status: str = Field("none", title="Twitter Space Status")
    audience_count: int = Field(None, title="Twitter Space Audience")
    ss_time: dt = Field(None, title="Scheduled Space Start Time")
    as_time: dt = Field(None, title="Actuary Space Start Time")
    ae_time: dt = Field(None, title="Actuary Space End Time")
    created_at: dt = Field(dt.utcnow(), title="Twitter Space Create Time")
    updated_at: dt = Field(dt.utcnow(), title="Twitter Space Update Time")

    class Config:
        orm_mode = True
        
class TwitterTweet(BaseModel):
    id: str = Field("1493437716750499843", title="Twitter Tweet ID")
    text: str = Field("にゃっはろ〜...", title="Twitter Tweet Text")
    hashtags: list = Field(['さくらみこ', 'みこなま'], title="Twitter Tweet Hashtags")
    lang: str = Field("ja", title="Twitter Tweet Language")
    possibly_sensitive: bool = Field(False, title="Twitter Tweet Possibly Sensitive")
    url: str = Field("https://twitter.com/35p_discord/status/1493437716750499843", title="Twitter Tweet URL")
    matching_rules: list = Field(['35P-Tweet1', 'collaboration'], title="Twitter Matching Rules")
    user_id: str = Field("979891380616019968", title="Twitter Account ID")
    display_id: str = Field("sakuramiko35", title="Twitter Account Display ID")
    name: str = Field("さくらみこ", title="Twitter Account Display Name")
    icon: str = Field("https://pbs.twimg.com/profile_images/979891380616019968/X9zw0QF1_normal.jpg", title="Twitter Account Icon URL")
    created_at: dt = Field(dt.utcnow(), title="Twitter Tweet Create Time")
    
    class Config:
        orm_mode = True

class TwitchStream(BaseModel):
    id: str = Field('824387510', title="Twitch Video ID")
    stream_id: str = Field('824387510', title="Twitch Stream ID")
    title: str = Field('サクラカゼ / sakurakaze', title="Twitch Stream Title")
    thumbnail: str = Field('https://static-cdn.jtvnw.net/cf_vods/d2nvs31859zcd8/sakuramiko_hololive/824387510/f9931116-28a7-4155-a68c-7ace82f6880e/thumb/custom-61f20465-77bb-467b-942d-85474842501f-1920x1080.png', title="Twitch Stream Thumbnail Img URL")
    description: str = Field('SakuraMiko Original Song.', title="Twitch Stream Description")
    url: str = Field('https://www.twitch.tv/videos/824387510', title="Twitch Stream(Video) URL")
    type: str = Field('upload', title="Twitch Content Type")
    game_id: str = Field('', title="Twitch Game ID")
    game_name: str = Field('', title="Twitch Game Name")
    status: str = Field("none", title="Twitch Stream Status")
    current_viewers: int = Field(None, title="Twitch Stream Viewers")
    view_count: int = Field(0, title="Twitch Video View Count")
    as_time: dt = Field(None, title="Actuary Stream Start Time")
    ae_time: dt = Field(None, title="Actuary Stream End Time")
    created_at: dt = Field(dt.utcnow(), title="Twitch Stream Create Time")
    updated_at: dt = Field(dt.utcnow(), title="Twitch Stream Update Time")
    
    class Config:
        orm_mode = True

class YouTubeCh(BaseModel):
    id: str = Field("UC-hM6YJuNYVAmUWxeIr9FeA", title="YouTube Channel ID")
    name: str = Field("Miko Ch. さくらみこ", title="YouTube Channel Name")
    icon: str = Field("https://yt3.ggpht.com/ytc/AKedOLQlZnbXr-RooUQezemDKu7alJrZcEMy8_5P07ILug=s240-c-k-c0x00ffffff-no-rj", title="YouTube Channel Icon URL")
    description: str = Field("にゃっはろ～！ホロライブ所属のエリート巫女アイドル さくらみこ (Sakura Miko)だにぇ🐱🌸...", title="YouTube Channel Description")
    subsc_count: int = Field(1350000, title="YouTube Channel Subscriber Count")
    play_count: int = Field(135000, title="YouTube Channel Total Play Count")
    video_count: int = Field(135000, title="YouTube Channel Total Video Count")
    status: str = Field("none", title="YouTube Channel Video Status")
    videos: List[YouTubeVideo] = []
    updated_at: dt = Field(dt.utcnow(), title="YouTube Channel Update Time")
    
    class Config:
        orm_mode = True
        
class Twitter(BaseModel):
    id: str = Field("979891380616019968", title="Twitter Account ID")
    display_id: str = Field("sakuramiko35", title="Twitter Account Display ID")
    name: str = Field("さくらみこ🌸", title="Twitter Account Name")
    icon: str = Field("https://pbs.twimg.com/profile_images/1476204822332583944/6fTtp7Cm.jpg", title="Twitter Account Icon URL")
    description: str = Field("にゃっはろ〜！ホロライブプロダクション所属 エリート巫女さくらみこだにぇ🐱", title="Twitter Account Description")
    followers_count: int = Field(35000, title="Twitter Account Followers Count")
    following_count: int = Field(35000, title="Twitter Account Follow Count")
    tweet_count: int = Field(350000, title="Twitter Account Tweets Count")
    status: str = Field("none", title="Twitter Account Space Status")
    space: List[TwitterSpace] = []
    tweet: List[TwitterTweet] = []
    updated_at: dt = Field(dt.utcnow(), title="Twitter Account Update Time")
    
    class Config:
        orm_mode = True
        
class TwitchCh(BaseModel):
    id: str = Field("557359020", title="Twitch Channel ID")
    display_id: str = Field("sakuramiko_hololive", title="Twitch Channel Display ID")
    name: str = Field("さくらみこ", title="Twitch Channel Name")
    icon: str= Field("https://static-cdn.jtvnw.net/jtv_user_pictures/bde8f8f1-1615-4df0-8745-dd5719e9ea92-profile_image-300x300.png", title="Twitch Channel Icon URL")
    offline_img: str = Field("https://static-cdn.jtvnw.net/jtv_user_pictures/b7cef80f-4b0a-44e2-bd58-9b5262b9b1c9-channel_offline_image-1920x1080.png", title="Twitch Channel OfflineImg URL")
    description: str = Field("Nyahello~! This is Elite Miko, I am super Elite！", title="Twitch Channel Description")
    subsc_count: int = Field(350000, title="Twitch Channel Subscriber Count")
    play_count: int = Field(350000, title="Twitch Channel Total Play Count")
    status: str = Field("none", title="Twitch Channel Stream Status")
    streams: List[TwitchStream] = []
    updated_at: dt = Field(dt.utcnow(), title="Twitch Channel Update Time")

    class Config:
        orm_mode = True