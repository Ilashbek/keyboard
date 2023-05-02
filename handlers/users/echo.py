from aiogram import types
from keyboards.inline.inlayn_tugmalar import backe
from loader import dp
from handlers.users.monkeyhandlers import response


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(response(message.text.upper()),reply_markup=backe)
