import discord
import os
import time
import aiohttp

try:
    from dotenv import load_dotenv
    from os.path import join, dirname

    load_dotenv(verbose=True)
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
except:
    pass


bot = discord.Bot()

#Load extensions
#bot.load_extension('cogs.api_tasks')


@bot.event
async def on_ready():
    # Bot起動時にターミナルに通知を出す
    print('-'*20)
    print('ログインしました')
    print('-'*20)
    timestamp = int(time.time())
    bot_chid = int(os.environ.get("BOT_CHID"))
    await bot.change_presence(activity=discord.Game(name='Nyahello!!'))
    bot_ch = bot.get_channel(bot_chid)
    await bot_ch.send(f"<t:{timestamp}:F>\nEliteBotが起動しました")
    check_api = await bot_ch.send("MikoAPIへの接続を確認中...")
    async with aiohttp.ClientSession() as session:
        async with session.get(os.environ.get("API_URL")) as res:
            if res.status == 200:
                await check_api.edit("MikoAPIへの接続に成功しました")
            else:
                await check_api.edit("MikoAPIへの接続に失敗しました")


if __name__ == "__main__":
    bot.run(os.environ.get("BOT_TOKEN"))