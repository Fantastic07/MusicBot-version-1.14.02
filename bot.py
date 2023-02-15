from aiogram import executor
from dispatcher import dp
import handlers
from handlers.set_command import set_default_commands

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True , on_startup=on_startup)  

