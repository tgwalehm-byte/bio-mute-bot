import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.protection import router as protection_router
from handlers.owner import router as owner_router
from handlers.admin import router as admin_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


async def main():

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(protection_router)
    dp.include_router(owner_router)
    dp.include_router(admin_router)

    print("================================")
    print("       BIO MUTE BOT STARTED")
    print("================================")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())