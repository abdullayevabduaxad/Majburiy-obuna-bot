import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    not_subscribed_channels = []
    try:
        for channel in CHANNELS:
            status = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            logging.info(f"User status in {channel}: {status.status}")
            if status.status not in ['member', 'administrator', 'creator']:
                not_subscribed_channels.append(channel)

        if not_subscribed_channels:
            await prompt_user_to_subscribe(message, not_subscribed_channels)  # To'g'ri parametr bilan chaqiramiz
        else:
            await message.answer("Siz barcha kanallarga obuna bo'lgansiz, botdan foydalanishingiz mumkin.")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        await prompt_user_to_subscribe(message, not_subscribed_channels)


async def prompt_user_to_subscribe(message: types.Message, not_subscribed_channels):
    markup = InlineKeyboardMarkup()
    for channel in not_subscribed_channels:
        markup.add(InlineKeyboardButton(f"Obuna bo'lish", url=f"https://t.me/{channel[1:]}"))
    markup.add(InlineKeyboardButton("✅ Tekshirish", callback_data="check_subscription"))
    await message.answer("Kechirasiz botimizdan foydalanishdan oldin ushbu kanallarga a'zo bo'lishingiz kerak.", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == 'check_subscription')
async def check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    not_subscribed_channels = []
    try:
        for channel in CHANNELS:
            status = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            logging.info(f"User status in {channel}: {status.status}")
            if status.status not in ['member', 'administrator', 'creator']:
                not_subscribed_channels.append(channel)

        if not_subscribed_channels:
            await bot.answer_callback_query(callback_query.id,
                                            "Siz hali barcha kanallarga obuna bo'lmadingiz.")
        else:
            await bot.answer_callback_query(callback_query.id, "Muvaffaqiyatli tekshirildi!")
            await bot.send_message(user_id, "Siz barcha kanallarga obuna bo'ldingiz, botdan foydalanishingiz mumkin.")
            await bot.delete_message(callback_query.message.chat.id,
                                     callback_query.message.message_id)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        await bot.answer_callback_query(callback_query.id,
                                        "Obunani tekshirishda muammo! Iltimos, qayta urinib ko'ring.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
