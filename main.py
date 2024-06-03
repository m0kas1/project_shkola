import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from handlers import bot_messages
from utils import StepsForm
import os
from environs import Env
# from aiogram.client.session.aiohttp import AiohttpSession
#
# session = AiohttpSession(proxy='http://proxy.server:3128')

env = Env()
env.read_env()
bot_token = env('BOT_TOKEN')

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    # bot = Bot(token=bot_token, session=session)
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.message.register(bot_messages.get_start, Command(commands='form'))
    dp.message.register(bot_messages.get_FIO, StepsForm.GET_FIO)
    dp.message.register(bot_messages.get_CHEH, StepsForm.GET_CHEH)
    dp.message.register(bot_messages.get_PODRASDELENIE, StepsForm.GET_PODRASDELENIE)
    dp.message.register(bot_messages.get_ULUCHENIE, StepsForm.GET_ULUCHENIE)
    dp.message.register(bot_messages.get_PREDLOSHENIE, StepsForm.GET_PREDLOSHENIE)
    dp.message.register(bot_messages.get_PROBLEMA, StepsForm.GET_PROBLEMA)
    dp.message.register(bot_messages.get_PHOTO_1, StepsForm.GET_PHOTO_1)
    dp.message.register(bot_messages.get_RESHENIE, StepsForm.GET_RESHENIE)
    dp.message.register(bot_messages.get_PHOTO_2, StepsForm.GET_PHOTO_2)
    dp.message.register(bot_messages.get_VIBER, StepsForm.GET_vibor)
    dp.include_routers(bot_messages.router)
    #dp.include_routers(other_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())