#https://habr.com/ru/articles/442800/
#://rutube.ru/video/ed83aaedc8b3d893aea81f5382855b6a/


import telebot
from telebot.types import BotCommand

bot = telebot.TeleBot('5672869540:AAGK4b7wy0KzfwuGzk3phXL-95J8x35CxQI')



# Функция для обработки команды /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.text == '/start':
        bot.reply_to(message, f'Привет, я твой бот!')
    elif message.text == '/help':
        bot.reply_to(message, f'Связаться с техподдержкой https://t.me/Snax_44')


def set_commands():
    commands = [
        BotCommand(command= '/start', description= 'Главное меню'),
        BotCommand(command= '/help', description= 'Техподдержка')
    ]
    try:
        bot.set_my_commands(commands)
        print("Команды успешно установлены.")
    except Exception as e:
        print(f"Ошибка при установке команд: {e}")
# Функция для обработки текстовых сообщений
@bot.message_handler(content_types=['text'])
def user_message(message):
    user_text = message.text.lower()
    bot.reply_to(message, f'{user_text}')



# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)