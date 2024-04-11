import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from handlers import other_handlers, user_handlers


config = load_config()                    # Указать путь до ".env", если файл не в корне проекта
bot_token = config.tg_bot.token           # Сохраняем токен в переменную bot_token


# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())