from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_kb = InlineKeyboardBuilder()
inline_kb.button(text='«1»', callback_data='«1»')
inline_kb.button(text='«2»', callback_data='«2»')
inline_kb.button(text='«3»', callback_data='«3»')
inline_kb.button(text='«4»', callback_data='«4»')
inline_kb.button(text='«5»', callback_data='«5»')
inline_kb.button(text='«6»', callback_data='«6»')
inline_kb.button(text='«7»', callback_data='«7»')
inline_kb.adjust(2)

b = InlineKeyboardBuilder()
b.button(text='Безопастность', callback_data='Безопастность')
b.button(text='Качество', callback_data='Качество')
b.button(text='Производительность', callback_data='Производительность')
b.button(text='Эргономика', callback_data='Эргономика')
b.adjust(2)

# inline_kb_2 = InlineKeyboardBuilder()
# inline_kb.button(text='Безопастность', callback_data='«ЮМЭК»')
# inline_kb.button(text='Качество', callback_data='«МЗВА-ЧЭМЗ»')
# inline_kb.button(text='Производительность', callback_data='«ИНСТА»')
# inline_kb.button(text='Эргономика', callback_data='«Энерготрансизолятор»')
# inline_kb.adjust(2)

