import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5590048325:AAFi-S4eIlzUj47ER8MYDYGUehC-WzC-n2k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    if message.text == 'Hello':
      await message.answer('What do you want?')
    if message.text == 'Video':
      await bot.send_video(message.chat.id, open('videoplayback.mp4', 'rb'))
    else:
      await message.answer('lallalalalalalalaalalal')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)