from xmlrpc.client import DateTime
import discord
from datetime import datetime as dt

def ytch_notice_name(id: str, old_name: str, new_name: str, icon: str):
    embed=discord.Embed(title=new_name, url=f"https://www.youtube.com/channel/{id}", description="**YouTubeのチャンネル名が変更されました**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_image(url=icon)
    embed.add_field(name="変更前", value=f"**{old_name}**", inline=True)
    embed.add_field(name="変更後", value=f"**{new_name}**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytch_notice_subsc(id: str, name: str, icon: str, subsc: int, updated_at: DateTime):
    embed=discord.Embed(title=name, url=f"https://www.youtube.com/channel/{id}", description=f"**YouTubeチャンネル登録者数が{subsc/10000:.0f}万人を突破しました!**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_image(url=icon)
    embed.add_field(name="達成日時", value=f"**<t:{int(updated_at.timestamp())}:F>(<t:{int(updated_at.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytch_notice_play(id: str, name: str, icon: str, play_count: int, updated_at: DateTime):
    embed=discord.Embed(title=name, url=f"https://www.youtube.com/channel/{id}", description=f"**YouTubeチャンネル総再生回数が{round(play_count, -6):,}回を突破しました!**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_image(url=icon)
    embed.add_field(name="達成日時", value=f"**<t:{int(updated_at.timestamp())}:F>(<t:{int(updated_at.timestamp())}:R>)**", inline=True)
    embed.add_field(name="現在の総再生回数", value=f"**{play_count:,}回**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytch_notice_video(id: str, name: str, icon: str, video_count: int, updated_at: DateTime):
    embed=discord.Embed(title=name, url=f"https://www.youtube.com/channel/{id}", description=f"**YouTubeチャンネル総動画本数が{round(video_count, -2):,}本を突破しました!**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_image(url=icon)
    embed.add_field(name="達成日時", value=f"**<t:{int(updated_at.timestamp())}:F>(<t:{int(updated_at.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_title(id: str, name: str, icon: str, url: str, video_id: str, old_title: str, new_title: str):
    embed=discord.Embed(title=new_title, url=url, description="**動画/配信タイトルが変更されました**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="変更前", value=f"**{old_title}**", inline=True)
    embed.add_field(name="変更後", value=f"**{new_title}**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_sstime(id: str, name: str, icon: str, title: str, url: str, video_id: str, old_sstime: DateTime, new_sstime: DateTime):
    embed=discord.Embed(title=title, url=url, description="**配信開始/プレミア公開予定時刻が変更されました**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="変更前", value=f"**<t:{int(old_sstime.timestamp())}:F>(<t:{int(old_sstime.timestamp())}:R>)**", inline=True)
    embed.add_field(name="変更後", value=f"**<t:{int(new_sstime.timestamp())}:F>(<t:{int(new_sstime.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_nonetoupcoming(id: str, name: str, icon: str, title: str, url: str, video_id: str, sstime: DateTime):
    embed=discord.Embed(title=title, url=url, description="**配信/プレミア公開枠が作成されました**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="開始予定日時", value=f"**<t:{int(sstime.timestamp())}:F>(<t:{int(sstime.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_upcomingtolive(id: str, name: str, icon: str, title: str, url: str, video_id: str, sstime: DateTime, astime: DateTime):
    embed=discord.Embed(title=title, url=url, description="**配信/プレミア公開が開始されました!**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="開始予定日時", value=f"**<t:{int(sstime.timestamp())}:F>(<t:{int(sstime.timestamp())}:R>)**", inline=True)
    embed.add_field(name="開始日時", value=f"**<t:{int(astime.timestamp())}:F>(<t:{int(astime.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_nonetolive(id: str, name: str, icon: str, title: str, url: str, video_id: str, astime: DateTime):
    embed=discord.Embed(title=title, url=url, description="**ゲリラ配信が開始されました!**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="開始日時", value=f"**<t:{int(astime.timestamp())}:F>(<t:{int(astime.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_upcomingtonone(id: str, name: str, icon: str, title: str, url: str, video_id: str, sstime: DateTime, astime: DateTime):
    embed=discord.Embed(title=title, url=url, description="**配信/プレミア公開枠が削除されました**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="開始予定日時", value=f"**<t:{int(sstime.timestamp())}:F>(<t:{int(sstime.timestamp())}:R>)**", inline=True)
    embed.add_field(name="開始日時", value=f"**<t:{int(astime.timestamp())}:F>(<t:{int(astime.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_livetonone(id: str, name: str, icon: str, title: str, url: str, video_id: str, astime: DateTime, aetime: DateTime):
    embed=discord.Embed(title=title, url=url, description="**配信/プレミア公開が終了しました**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="開始日時", value=f"**<t:{int(astime.timestamp())}:F>(<t:{int(astime.timestamp())}:R>)**", inline=True)
    embed.add_field(name="終了日時", value=f"**<t:{int(aetime.timestamp())}:F>(<t:{int(aetime.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_upload(id: str, name: str, icon: str, title: str, url: str, video_id: str, createdat: DateTime):
    embed=discord.Embed(title=title, url=url, description="**動画が投稿されました!**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="投稿日時", value=f"**<t:{int(createdat.timestamp())}:F>(<t:{int(createdat.timestamp())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytvideo_notice_currentviewers(id: str, name: str, icon: str, title: str, url: str, video_id: str, trigger: int, current_viewers: int, updated_at: DateTime):
    embed=discord.Embed(title=title, url=url, description=f"**現在行われている配信の同時接続数(視聴者数)が{trigger/10000}万人を突破しました!**", color=0xff0000, timestamp=dt.utcnow())
    embed.set_author(name=name, url=f"https://www.youtube.com/channel/{id}", icon_url=icon)
    embed.set_image(url=f'https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg')
    embed.add_field(name="達成日時", value=f"**<t:{int(updated_at.timestamp())}:F>(<t:{int(updated_at.timestamp())}:R>)**", inline=True)
    embed.add_field(name="現在の同時接続数(視聴者数)", value=f"**{current_viewers:,}人**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed
