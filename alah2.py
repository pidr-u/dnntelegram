from aiogram import Bot, Dispatcher, executor, types
import requests
import json
token = input("Привет, я скрипт,который создает деанон ботов! Введите токен бота, можно получить в @BotFather: ")
bot = Bot(token=token)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message):
    await message.reply('Привет, бот создан скриптом https://github.com/pidr-u/dnntelegram/upload!\nСкинь номер сюда и я отправлю информацию о нем!\nКанал: @zalupalaha. Бота писал @Allah6661(я) по всем вопросам сюда. номер писать без плюса, работет только с русскими номерами.')
@dp.message_handler(content_types=['text'])
async def text(message):
    if message.chat.type != "private":
        await bot.leave_chat()
    number = message.text
    url = f'https://htmlweb.ru/json/mnp/phone/{number}'
    try:
        json = requests.get(url).json()
        await message.reply(f'Город: {json["city"]}:\nОператор:{json["oper"]}:\nРегион:{json["region"]}')
    except:
        await message.reply('Неверный номер или произошла ошибка')
executor.start_polling(dp, skip_updates=True)
