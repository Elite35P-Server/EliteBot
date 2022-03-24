import discord
from datetime import datetime as dt

def ytch_notice_name(id: str, old_name: str, new_name: str, icon: str):
    embed=discord.Embed(title="YouTubeのチャンネル名が変更されました", description=f"[[チャンネルを表示]](https://www.youtube.com/channel/{id})", color=0xff0000, timestamp=dt.utcnow())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="変更前", value=f"**{old_name}**", inline=True)
    embed.add_field(name="変更後", value=f"**{new_name}**", inline=True)
    embed.set_footer(text=new_name, icon_url=icon)
    return embed

def ytch_notice_icon(id: str, name: str, new_icon: str, old_icon: str):
    embed=discord.Embed(title="YouTubeのチャンネルアイコンが変更されました", description=f"[[チャンネルを表示]](https://www.youtube.com/channel/{id})", color=0xff0000, timestamp=dt.utcnow())
    embed.set_thumbnail(url=old_icon)
    embed.add_field(name="** **", value=f"**変更前(右)**", inline=False)
    embed.add_field(name="** **", value=f"**変更後(左)**", inline=False)
    embed.set_image(url=new_icon)
    embed.set_footer(text=name, icon_url=new_icon)
    return embed

def ytch_notice_description(id: str, name: str, icon: str):
    embed=discord.Embed(title="YouTubeのチャンネル概要が変更されました", description=f"[[チャンネルを表示]](https://www.youtube.com/channel/{id})", color=0xff0000, timestamp=dt.utcnow())
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=name, icon_url=icon)
    return embed