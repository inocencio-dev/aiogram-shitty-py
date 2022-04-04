from utils.set_bot_commands import set_default_commands
import random
import time
import threading

async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)

def thread_function():
    while True:
        try:
            randomic = random.randint(0,10)
            print(randomic)
            time.sleep(1)
        except:
            pass


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    x1 = threading.Thread(target=thread_function, args=())
    x1.start()
    executor.start_polling(dp, on_startup=on_startup)