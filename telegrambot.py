import telebot

bot = telebot.TeleBot('6837950576:AAGy5n2UbzqnLOFoRPnkk_M4YUU_8WvXI1o')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здраствуйте {message.from_user.first_name}, для того чтобы выбрать дату регистрации напишите команду /retur')

@bot.message_handler(commands=['retur'])
def tef(message):
    bot.send_message(message.chat.id, f'Вот вам дашборд с полным котологом наших услуг прошу вас с ним ознокомиться [https://0b0f-188-130-255-207.ngrok-free.app/], после чего напишите /tabl для примера записи анкеты')

@bot.message_handler(commands=['tabl'])
def tef(message):
    bot.send_message(message.chat.id, f'Вот пример написания анкеты(ФИО,Возраст,дата когда записываитесь)')

@bot.message_handler(content_types=['text'])
def message(message):
    bot.send_message(5263471764, f'К нам записаля, {message.text}')

bot.polling(none_stop=True)