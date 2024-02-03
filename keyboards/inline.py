from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

x_o = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=' ', callback_data="1"),
            InlineKeyboardButton(text=' ', callback_data="2"),
            InlineKeyboardButton(text=' ', callback_data="3")
        ],
        [
            InlineKeyboardButton(text=' ', callback_data="4"),
            InlineKeyboardButton(text=' ', callback_data="5"),
            InlineKeyboardButton(text=' ', callback_data="6")
        ],
        [
            InlineKeyboardButton(text=' ', callback_data="7"),
            InlineKeyboardButton(text=' ', callback_data="8"),
            InlineKeyboardButton(text=' ', callback_data="9")
        ],

    ]
)
