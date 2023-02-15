from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Bo'tni ishga tushirish"),
            types.BotCommand("make_post", "Po'st yaratish"),
            types.BotCommand("remove", "1.State dan chiqish 2.Fayllarni o'chirish"),
            types.BotCommand("view_post", "Po'stni ko'rish"),
            types.BotCommand("send_post", "Po'stni kanalga yuborish")
        ]
    )
