from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить проблему')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

ispravit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Исправить')
        ],
        [
            KeyboardButton(text='Отправить')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Нажми на меня'
)