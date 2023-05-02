from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.inlayn_tugmalar import inlinekeymenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text="Assalomu alaykum\nValyuta Kurslari botiga Xush Kelibsiz"
    await message.answer(text,reply_markup=inlinekeymenu)
