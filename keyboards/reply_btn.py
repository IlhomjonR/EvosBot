from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot_context import languages


async def start_command_btn(lang: str):
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.row(
        KeyboardButton(text=languages[lang]['buttons']['menu_text'])
        )
    btn.row(
        KeyboardButton(text=languages[lang]['buttons']['my_orders_text'])
        )
    btn.row(
        KeyboardButton(text=languages[lang]['buttons']['write_commit']),
        KeyboardButton(text=languages[lang]['buttons']['settings'])
        )

    return btn


async def settings_btn(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.row(
        KeyboardButton(text=languages[lang]['buttons']['edit_language_btn'])
    )
    return btn


async def choose_lang_btn():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.add(
        KeyboardButton(text="🇺🇿 UZ"),
        KeyboardButton(text="🇷🇺 RU"),
    )
    return btn


async def choose_lang_edit_btn():
    btn = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn.add(
        KeyboardButton(text="🇺🇿 UZ"),
        KeyboardButton(text="🇷🇺 RU"),
        KeyboardButton(text="⬅️ Назад"),
    )
    return btn


async def contact_command_btn(lang: str):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    btn.add(
        KeyboardButton(text=languages[lang]['buttons']['contact_text'], request_contact=True),
        KeyboardButton(text="⬅️ Назад")
    )

    return btn
