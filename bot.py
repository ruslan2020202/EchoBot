import asyncio

from aiogram import Bot, Dispatcher, types, filters
from config import token_api

bot = Bot(token_api)
dp = Dispatcher()


@dp.message(filters.CommandStart())
async def cdm_start(message: types.Message):
    await message.answer('Привет')


if __name__ == '__main__':
    asyncio.run(dp.start_polling(bot))
