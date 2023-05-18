from aiogram import Bot, Dispatcher, executor
import handlers



API_TOKEN = '5940664174:AAEX6wiHCnS1qjZZCmbThtg_PEazi4lntjk'

# создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# регистрируем функции
dp.register_message_handler(handlers.start, commands=["start"])
dp.register_message_handler(handlers.echo)

# запускаем программу
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


# указание skip_updates=True
# пропустит команды,
# которые отправили
# до старта бота
