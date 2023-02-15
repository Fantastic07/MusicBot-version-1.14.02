from aiogram import types
from dispatcher import dp
import shutil

# Group events goes here ...
# In order to read group messages, bot group privacy must be disabled
# @dp.message_handler(content_types=["new_chat_members", "left_chat_member"])
# async def on_user_join_or_left(message: types.Message):
#     """
#     Removes "user joined" and "user left" messages.
#     By the way, bots do not receive left_chat_member updates when the group has more than 50 members (otherwise use https://core.telegram.org/bots/api#chatmemberupdated)
#     :param message: Service message "User joined group
#     """
#     print(message)
#     await message.answer(f'salom {message.from_user.first_name} sizga botimiz habar yubordi')
#     print(message.new_chat_members[0].id)
#     await dp.bot.send_message(chat_id=message.new_chat_members[0].id, text=" Siz bu bo'tga oldin start bosmagansiz ! ")

@dp.message_handler(content_types=['audio'])
async def a(msg:types.Message):
    try:
        file = open("Post/file_names.txt")
        music_file_name = file.readlines()
        file.close()

        file = open("Post/music_text.txt")
        text = file.readlines()
        file.close()

        text_music = ' '.join(text)

        if msg.audio.file_name == music_file_name[0]:
            await msg.reply(text_music)
            try:
                shutil.rmtree(r'Post')
            except:
                pass 
    except:
        pass     
        