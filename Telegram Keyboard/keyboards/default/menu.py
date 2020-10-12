from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Starter Spot"),
        ],
       [
            KeyboardButton(text="Closer Spot"),
        ],
         [
            KeyboardButton(text="Closer Margin"),
        ],
         [
            KeyboardButton(text="Starter Margin"),
        ],
    ],
    resize_keyboard=False
)
