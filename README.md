# Telegrambot
Данный телеграмм-бот предназначен для записи клината на игру страйкбол.
Бот помогает оптимизировать процесс записи на игру.
Клиенту он предоставляет расписание игры, а сотруднику анкету клиента.

ЗАПУСК НА ЛОКАЛЬНОЙ МАШИНЕ

Чтобы запустить бота на локальной машине, необходимо вставить id бота в телеграмм,
а затем запустить код бота в среде предназначенной для Python.
Ссылка на бота [https://t.me/airsoft_training_ground_bot]

КАК ПОЛЬЗОВАТЬСЯ БОТОМ

1. При запуске бота необходимо написать команду /start
2. После необходимо написат команду /retur
3. Перейдя по ссылке и ознакомившись с расписанием, необходимо ввести команду /tabl/
4. После чего клиенту приходит пример анкеты
5. После нужно написать анкету по примеру который отправляет бот и нажать "Enter"

КОД ,бота

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
   

КОНТАКТНАЯ ИНФОРМАЦИЯ

telegram f'[@klaymis]'
Email f'[primerpochty2000@gmail.com]'