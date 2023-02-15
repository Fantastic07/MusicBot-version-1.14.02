from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def text_adder():

    cheker = InlineKeyboardMarkup(
    inline_keyboard=[
         [InlineKeyboardButton('✅HA',callback_data='yes'),InlineKeyboardButton("❌YO'Q",callback_data='nope')]
    
    ])
    return cheker