from aiogram import types
from dispatcher import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from post_text import *
import shutil
from channels import *
from .callbacks import text_adder

class Post(StatesGroup):
    photo = State()
    audio = State()
    full_audio = State()
    music_name = State()
    post_name = State()
    have_text = State()
    music_text = State()

# ==========================================================================================
@dp.message_handler(commands=['start'],is_owner=True)
async def cmd_ping_bot(msg : types.Message):
    await msg.answer("\n°•°•--—————--•°•°\n👋Salom Amirxon ! \n🤖Botingizga xush kelibsiz ❕ \n°•°•--—————--•°•°\n")
    try:
        file = open("Post/post.txt")
        file.close()
        await msg.answer("❗️Sizda tugallanmagan post mavjud❗️")
    except:
        pass

# ==========================================================================================

@dp.message_handler(commands=['remove'],state='*',is_owner=True)
async def cmd_ping_bot(msg : types.Message,state : FSMContext):
    try:
        shutil.rmtree(r'Post')
        await msg.answer('Bekor qilindi ! ! !')
    except:
        await msg.answer("Sizda post yo'q")

# ==========================================================================================
@dp.message_handler(commands=['make_post'],state='*',is_owner=True)
async def cmd_ping_bot(msg : types.Message,state : FSMContext):
    try:
        shutil.rmtree(r'Post')
    except:
        pass
    await Post.photo.set()
    await msg.answer("Avval rasm yuboring ! ! !")
# ==========================================================================================
@dp.message_handler(content_types=['photo'],state=Post.photo)
async def photo_edit(msg : types.Message , state : FSMContext):

    photo_name = 'post'
    await msg.photo[-1].download(destination=f'Post/photos/{photo_name}.jpg')

    with open("Post/path.txt","a") as w:
        w.write(f'Post/photos/{photo_name}.jpg\n')
        w.close()

    await Post.audio.set()
    await msg.answer("Endi Musiqadan parcha yuboring ! ! !")

# ==========================================================================================
@dp.message_handler(content_types=['audio'],state=Post.audio)
async def photo_edit(msg : types.Message , state : FSMContext):

    if msg.audio.duration > 20:
        await msg.answer("Musiqa audiosining uzunligi maksimal 20 sekund bo'lishi kerak")
    else:

        audio_name = msg.audio.file_name
        await msg.audio.download(destination=f'Post/audios/audio_{audio_name}')

        with open("Post/path.txt","a") as w:
            w.write(f'Post/audios/audio_{audio_name}\n')
            w.close()


        await Post.full_audio.set()
        await msg.answer("Endi musiqaning o'zini yuboring ! ! !")
# ==========================================================================================
@dp.message_handler(content_types=['audio'],state=Post.full_audio)
async def photo_edit(msg : types.Message , state : FSMContext):

    music_name = msg.audio.file_name
    await msg.audio.download(destination=f'Post/musics/{music_name}')

    with open("Post/path.txt","a") as w:
        w.write(f'Post/musics/{music_name}\n')
        w.close()

    with open("Post/file_names.txt","a") as w:
        w.write(f'{music_name}')
        w.close()

    await Post.music_name.set()
    try:
        music_name = music_name.replace('.mp3','',1)
    except:
        pass
    await msg.answer(f"Musiqa uchun nom bering ! ! ! \nDefult : <code>{music_name}</code>")
# ==========================================================================================
@dp.message_handler(content_types=['text'],state=Post.music_name)
async def photo_edit(msg : types.Message , state : FSMContext):

    with open("Post/post.txt","a") as w:
        w.write(f'{msg.text}\n')
        w.close()

    await Post.post_name.set()
    await msg.answer('Postingizga nom bering ! ! ! \nDefult : <code>#TrendMusic</code>')
# ==========================================================================================
@dp.message_handler(content_types=['text'],state=Post.post_name)
async def photo_edit(msg : types.Message , state : FSMContext):
   
    with open("Post/post.txt","a") as w:
        w.write(msg.text)
        w.close()

    await msg.answer("Musiqaga text Kiritasizmi ? " , reply_markup=text_adder())

# ==========================================================================================

@dp.callback_query_handler(text_contains = "yes" , state="*")
async def qosh(call: types.CallbackQuery):
    await Post.music_text.set()
    await call.message.edit_text('Text kiriting ! ! !')

@dp.callback_query_handler(text_contains = "nope" , state='*')
async def qosh(call: types.CallbackQuery , state : FSMContext):
    
    await state.finish()
    await call.message.edit_text('Tayyor ! ! !')

# ==========================================================================================

@dp.message_handler(content_types=['text'],state=Post.music_text)
async def photo_edit(msg : types.Message , state : FSMContext):

    if len(msg.text) < 100:
        await msg.answer("Bu Musiqa texti bo'la olmaydi ! ! ! Text dagi belgilar soni 100 dan kam ! ! !")
        pass

    else:
        with open("Post/music_text.txt","a") as w:
            w.write(msg.text)
            w.close()

            await state.finish()
            await msg.answer("Tayyor ! ! !")

@dp.message_handler(commands=['view_post'],is_owner=True)
async def sending(msg:types.Message):

    try:
        post_text = "<a href='http://t.me/musica1_10'>📄текст в комментариях</a>"

        file = open("Post/post.txt")
        content = file.readlines()
        file.close()

        file = open("Post/path.txt")
        paths = file.readlines()
        file.close()

        photopath = paths[0].replace('\n','',1)
        audiopath = paths[1].replace('\n','',1)
        musicpath = paths[2].replace('\n','',1)

        a = await msg.answer_photo(photo=open(f'{photopath}' ,'rb') , caption=photo(music2_name=content[0],post2_name=content[1]))
        
        await msg.answer_audio(audio=open(f'{audiopath}' ,'rb') , caption=audio_caption)

        try:
            file = open("Post/music_text.txt")
            text_cheak = file.readlines()
            file.close()

            the_text = ' '.join(text_cheak)

            b = await a.reply_audio(audio=open(f'{musicpath}' ,'rb') , caption=music(music2_name=content[0] , text_is=post_text))
            await b.reply(the_text)    
        except:
            await a.reply_audio(audio=open(f'{musicpath}' ,'rb') , caption=music(music2_name=content[0]))
    except:
        await msg.answer("Sizda post yo'q ! ! !")

@dp.message_handler(commands=['send_post'],is_owner=True)
async def sending(msg:types.Message):

    try:  
        for channel in BASE_CHANNELS:

            post_text = "<a href='http://t.me/musica1_10'>📄текст в комментариях</a>"

            file = open("Post/post.txt")
            content = file.readlines()
            file.close()

            file = open("Post/path.txt")
            paths = file.readlines()
            file.close()

            photopath = paths[0].replace('\n','',1)
            audiopath = paths[1].replace('\n','',1)
            musicpath = paths[2].replace('\n','',1)

            a = await dp.bot.send_photo(photo=open(f'{photopath}' ,'rb') , caption=photo(music2_name=content[0],post2_name=content[1]),chat_id=channel)
            
            await dp.bot.send_audio(audio=open(f'{audiopath}' ,'rb') , caption=audio_caption ,chat_id=channel)

            try:
                file = open("Post/music_text.txt")
                text_cheak = file.readlines()
                file.close()
                await a.reply_audio(audio=open(f'{musicpath}' ,'rb') , caption=music(music2_name=content[0] , text_is=post_text))    
            except:
                await a.reply_audio(audio=open(f'{musicpath}' ,'rb') , caption=music(music2_name=content[0]))

            await msg.answer("Sizning ushbu po'stingiz kanalingizga yuborilganidan so'ng ba'zadan o'chirib yuboriladi ! ! !")
    except:
        await msg.answer("Sizda post yo'q ! ! !")

@dp.message_handler(is_owner=True)
async def aler(msg : types.Message):
    await msg.answer("Iltimos kerakli buyruqlardan foydalaning ! ! !")



   


   
