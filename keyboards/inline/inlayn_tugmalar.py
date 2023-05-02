from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

inlinekeymenu=InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="🇺🇸USD  🇺🇿UZS",callback_data="usduzs"),
        ],
        [
            InlineKeyboardButton(text="🇪🇺EURO  🇺🇿UZS", callback_data="eurouzs"),
        ],

        [
            InlineKeyboardButton(text="🇷🇺RuB  🇺🇿UZS", callback_data="rubuzs"),
        ],

        [
            InlineKeyboardButton(text="👨🏻‍💻Admin", callback_data="Admin"),
            InlineKeyboardButton(text="💸Valyutalar codlari", callback_data="moneylist"),
        ],

    ]
)

back=InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="💸Valyuta kurslari",callback_data="valyuta"),
        ],


    ],
)


backe=InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="💸Valyutalar codi va nomi", callback_data="mone"),
        ],


    ],
)