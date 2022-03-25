import discord
import time
from datetime import datetime as dt

def ytch_notice_name(id: str, old_name: str, new_name: str, icon: str):
    embed=discord.Embed(title=new_name, url=f"https://www.youtube.com/channel/{id}", description="YouTubeのチャンネル名が変更されました", color=0xff0000, timestamp=dt.now())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="変更前", value=f"**{old_name}**", inline=True)
    embed.add_field(name="変更後", value=f"**{new_name}**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytch_notice_subsc(id: str, name: str, icon: str, subsc: int):
    embed=discord.Embed(title=name, url=f"https://www.youtube.com/channel/{id}", description=f"**YouTubeチャンネル登録者数が{subsc/10000:.0f}万人を突破しました!**", color=0xff0000, timestamp=dt.now())
    embed.set_image(url=icon)
    embed.add_field(name="達成日時", value=f"**<t:{int(time.time())}:F>(<t:{int(time.time())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytch_notice_play(id: str, name: str, icon: str, play_count: int):
    embed=discord.Embed(title=name, url=f"https://www.youtube.com/channel/{id}", description=f"**YouTubeチャンネル総再生回数が{round(play_count, -6):,}回を突破しました!**", color=0xff0000, timestamp=dt.now())
    embed.set_image(url=icon)
    embed.add_field(name="達成日時", value=f"**<t:{int(time.time())}:F>(<t:{int(time.time())}:R>)**", inline=True)
    embed.add_field(name="現在の総再生回数", value=f"**{play_count:,}回**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed

def ytch_notice_video(id: str, name: str, icon: str, video_count: int):
    embed=discord.Embed(title=name, url=f"https://www.youtube.com/channel/{id}", description=f"**YouTubeチャンネル総動画本数が{round(video_count, -2):,}本を突破しました!**", color=0xff0000, timestamp=dt.now())
    embed.set_image(url=icon)
    embed.add_field(name="達成日時", value=f"**<t:{int(time.time())}:F>(<t:{int(time.time())}:R>)**", inline=True)
    embed.set_footer(text="EliteBot v2", icon_url="https://media.discordapp.net/attachments/788107610943520861/939782491303211018/IMG_6360.png")
    return embed