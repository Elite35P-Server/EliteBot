import discord
import json
import os
import time
import aiohttp
from cogs import db
from logging import getLogger, config

with open('./log_config.json', 'r') as f:
    log_config = json.load(f)
config.dictConfig(log_config)
logger = getLogger('main')

bot = discord.Bot()

@bot.event
async def on_ready():
    await db.setup()
    # Bot起動時にターミナルに通知を出す
    logger.info('-'*30)
    logger.info('EliteBot is ready.')
    logger.info('-'*30)
    timestamp = int(time.time())
    bot_chid = int(os.environ.get('BOT_CHID'))
    await bot.change_presence(activity=discord.Game(name="にゃっはろ～!! みこちはえりーとだにぇ!!"))
    bot_ch = bot.get_channel(bot_chid)
    await bot_ch.send(f"<t:{timestamp}:F>\nEliteBotが起動しました")
    check_api = await bot_ch.send("MikoAPIへの接続を確認中...")
    logger.info('Checking API connection...')
    async with aiohttp.ClientSession() as session:
        async with session.get(os.environ.get('API_URL')) as resp:
            if resp.status == 200:
                await check_api.edit("MikoAPIへの接続に成功しました")
                logger.info('API connection success.')
            else:
                await check_api.edit(f"MikoAPIへの接続に失敗しました ({resp.status})")
                logger.error('API connection failed.', resp.text)
                
    bot.load_extension('cogs.api_tasks')
    bot.load_extension('cogs.notification')
    bot.load_extension('cogs.commands')



if __name__ == '__main__':
    bot.run(os.environ.get('BOT_TOKEN'))