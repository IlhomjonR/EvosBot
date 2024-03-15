from loader import dp
from aiogram.types import Message, CallbackQuery
from db.database import add_user, set_lang, get_user_lang
from keyboards.reply_btn import start_command_btn, choose_lang_btn, choose_lang_edit_btn, settings_btn, contact_command_btn
from state import UserStates
from aiogram.dispatcher.storage import FSMContext
from bot_context import languages


@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    have_lang = await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    if have_lang:
        btn = await choose_lang_btn()
        await message.answer(f"Tilni tanlang\n\nВыберите язык:", reply_markup=btn)
        await UserStates.choose_lang.set()
    else:
        lang = await get_user_lang(user_id=message.from_user.id)
        btn = await start_command_btn(lang)
        await message.answer(languages[lang]['start_command_text'], reply_markup=btn)


@dp.message_handler(state=UserStates.choose_lang)
async def choose_lang_state(message: Message, state: FSMContext):
    text = message.text

    if text == '🇺🇿 UZ':
        lang = "uz"
    else:
        lang = "ru"

    await set_lang(
        user_id=message.from_user.id,
        lang=lang
    )
    await start_command(message)
    await state.finish()


@dp.message_handler(text=['⚙️ Sozlamalar', '⚙️ Настройки'])
async def settings_command(message: Message):
    lang = await get_user_lang(user_id=message.from_user.id)
    btn = await settings_btn(lang)
    await message.answer(f'''Выберите действие:''', reply_markup=btn)


@dp.message_handler(text=['Изменить язык', "Tilni o'zgartirish"])
async def change_lang_command(message: Message):
    btn = await choose_lang_edit_btn()
    await message.answer(f'''Выберите язык:''', reply_markup=btn)


@dp.message_handler(text="⬅️ Назад")
async def back_command(message: Message):
    await start_command(message)


@dp.message_handler(text=['🇺🇿 UZ','🇷🇺 RU'])
async def update_language(message: Message):
    text = message.text

    if text == '🇺🇿 UZ':
        lang = "uz"
    else:
        lang = "ru"

    await set_lang(
        user_id=message.from_user.id,
        lang=lang

    )
    await message.answer("Til o'zgardi✅")
    await start_command(message)


@dp.message_handler(text=['🇷🇺 RU'])
async def update_language(message: Message):
    text = message.text

    if text == '🇺🇿 UZ':
        lang = "uz"
    else:
        lang = "ru"

    await set_lang(
        user_id=message.from_user.id,
        lang=lang

    )
    await message.answer("Язык изменился✅")
    await start_command(message)


@dp.message_handler(text=['✍️ Оставить комментарий'])
async def write_comment(message: Message):
    lang = await get_user_lang(user_id=message.from_user.id)
    btn = await contact_command_btn(lang)
    await message.answer("Поделитесь контактом для дальнейшего связи с Вами", reply_markup=btn)


@dp.message_handler(text=['✍️ Izoh qoldiring'])
async def write_comment(message: Message):
    lang = await get_user_lang(user_id=message.from_user.id)
    btn = await contact_command_btn(lang)
    await message.answer("Siz bilan keyingi muloqot uchun kontaktingizni baham ko'ring", reply_markup=btn)