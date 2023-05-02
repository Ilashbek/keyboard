from aiogram.types import CallbackQuery

from loader import dp
from keyboards.inline.inlayn_tugmalar import inlinekeymenu,back,backe
from aiogram import types
import requests





# Admin tugmasi uchun handler
@dp.callback_query_handler(text="Admin")
async def select_admin(call:CallbackQuery):
    text=f"👨🏻‍💻Bot Yaratuvchisi\n"
    text+=f"Qahramonov Ilashbek\n"
    text+=f"teligram: @ollohningbirbandasi\n"
    await call.message.answer(text,reply_markup=back)



# usd uzs tugmasi uchun handler
@dp.callback_query_handler(text="usduzs")
async def select_admin(call: CallbackQuery):


    url = "https://v6.exchangerate-api.com/v6/93ac7ff21eb264e8147741b8/latest/USD"

    request = requests.get(url)
    reponse = request.json()

    data = reponse["time_last_update_utc"]
    usd = reponse["base_code"]
    som = reponse["conversion_rates"]["UZS"]
    text = f"<b>Sana:{data}\n</b>"
    text += f"<b>1</b>🇺🇸{usd}=<b>{som}</b>so'm🇺🇿"
    await call.message.edit_reply_markup()
    await call.message.answer(text,reply_markup=back)


# rubl uzs tugmasi uchun handler
@dp.callback_query_handler(text="rubuzs")
async def select_admin(call: CallbackQuery):


    url = "https://v6.exchangerate-api.com/v6/93ac7ff21eb264e8147741b8/latest/RUB"

    request = requests.get(url)
    reponse = request.json()

    data = reponse["time_last_update_utc"]
    usd = reponse["base_code"]
    som = reponse["conversion_rates"]["UZS"]
    text = f"<b>Sana:{data}\n</b>"
    text += f"<b>1</b>🇷🇺{usd}=<b>{som}</b>so'm🇺🇿"
    await call.message.edit_reply_markup()
    await call.message.answer(text,reply_markup=back)



# euro uzs tugmasi uchun handler
@dp.callback_query_handler(text="eurouzs")
async def select_admin(call: CallbackQuery):


    url = "https://v6.exchangerate-api.com/v6/93ac7ff21eb264e8147741b8/latest/EUR"

    request = requests.get(url)
    reponse = request.json()

    data = reponse["time_last_update_utc"]
    usd = reponse["base_code"]
    som = reponse["conversion_rates"]["UZS"]
    text = f"<b>Sana:{data}\n</b>"
    text += f"<b>1</b>🇪🇺{usd}=<b>{som}</b>so'm🇺🇿"
    await call.message.edit_reply_markup()
    await call.message.answer(text,reply_markup=back)


@dp.callback_query_handler(text="valyuta")
async def select_admin(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer("Tanlang",reply_markup=inlinekeymenu)


def response(x):
    try:
        url = f"https://v6.exchangerate-api.com/v6/93ac7ff21eb264e8147741b8/latest/{x}"

        request = requests.get(url)
        reponse = request.json()

        data = reponse["time_last_update_utc"]
        x_code = reponse["base_code"]
        som = reponse["conversion_rates"]["UZS"]
        text = f"<b>Sana:{data}\n</b>"
        text += f"<b>1</b>{x_code}=<b>{som}</b>so'm🇺🇿"
        return text
    except:
        text=f"Siz notug'ri pul birligini kiritdingiz\n"
        text+=f"ruyhatdan tanlang👇"
        return text


@dp.callback_query_handler(text="mone")
async def select_admin(call: CallbackQuery):
    valyutalari=f"USD - AQSH dollari\n"
    valyutalari+=f"EUR - Yevro\n"
    valyutalari+=f"GBP - Buyuk Britaniya funti \n"
    valyutalari+=f"JPY - Yaponiya iyenasi\n"
    valyutalari+=f"CHF - Shveytsariya franki\n"
    valyutalari+=f"CNY - Xitoy yuani\n"
    valyutalari+=f"AUD - Avstraliya dollari\n"
    valyutalari+=f"CAD - Kanada dollari\n"
    valyutalari+=f"DKK - Daniya kronasi\n"
    valyutalari+=f"HKD - Hong Kong dollari\n"
    valyutalari+=f"IDR - Indoneziya rupiyasi\n"
    valyutalari+=f"INR - Indiya rupiyasi\n"
    valyutalari+=f"ILS - Isroil yangi shekeli\n"
    valyutalari+=f"KRW - Koreya chong woni\n"
    valyutalari=f"MYR - Malayziya ringgiti \n"
    valyutalari+=f"MXN - Meksika pesosi\n"
    valyutalari+=f"NOK - Norvegiya kronasi\n"
    valyutalari+=f"KZT - Qozog'iston tengesi\n"
    valyutalari+=f"QAR - Qatar riyoli\n"
    valyutalari+=f"RUB - Rossiya rubli\n"
    valyutalari+=f"SAR - Saudiya Arabistoni riyoli\n"
    valyutalari+=f"SGD - Singapur dollari\n"
    valyutalari+=f"HRK - Xorvatiya kunasi\n"
    valyutalari+=f"CZK - Chex kronasi\n"
    valyutalari+=f"ESP - Esoniya pesetasi\n"
    valyutalari+=f"JOD - Iordaniya dinori\n"
    valyutalari+=f"KES - Keniya shillingi\n"
    valyutalari+=f"CUP - Kuba pesosi\n"
    valyutalari+=f"MAD - Marokash dirhami\n"
    valyutalari+=f"NLG - Niderlandiya guldeni\n"
    valyutalari+=f"PKR - Pakistan rupiyasi\n"
    valyutalari+=f"PAB - Panama balboasi\n"
    valyutalari+=f"PEN - Peru soli\n"
    valyutalari+=f"PLN - Polsha zlotiyi\n"
    valyutalari+=f"RON - Ruminiya leyi\n"
    valyutalari+=f"SDG - Sudan funti\n"
    await call.message.answer(valyutalari,f"Ushbu bulimdan uzingizga kerakli valyuta kodini yuboring",reply_markup=backe)












