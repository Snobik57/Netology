import telebot


bot = telebot.TeleBot(input('Enter bot telegram token: '))


@bot.message_handler(commands=['start', 'help'])
def start(message, red=False):
    mes = bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Just do it!'
                                            f'\nВведите ваш ID Вконтакте')
    bot.register_next_step_handler(mes, user_get_vk_id)


def user_get_vk_id(message):
    id_vk = int(message.text)
    chat_id = int(message.chat.id)

    mes = bot.send_message(chat_id, 'Введите название группы, из которой вы хотите получать посты')
    bot.register_next_step_handler(mes, user_get_name_group)


def user_get_name_group(message):
    chat_id = int(message.chat.id)
    name_group = message.text

    mes = bot.send_message(chat_id, 'Я готов к работе. Давайте начнем!')
