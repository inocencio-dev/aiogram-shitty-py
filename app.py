from utils.set_bot_commands import set_default_commands
import random
import time
import threading
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook
from data import config

HEROKU_APP_NAME = config.HEROKU_APP_NAME
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{config.BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = config.PORT


async def on_startup(dispatcher):
    import filters
    import middlewares
    filters.setup(dispatcher)
    middlewares.setup(dispatcher)
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await dispatcher.bot.delete_webhook()


def thread_function():
    while True:
        try:
            randomic = random.randint(0,10)
            print(randomic)
            time.sleep(1200)
        except:
            pass

if __name__ == '__main__':
    from handlers import dp
    x1 = threading.Thread(target=thread_function, args=())
    x1.start()
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )