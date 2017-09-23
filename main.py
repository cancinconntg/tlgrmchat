import telebot

bot = telebot.TeleBot('442140691:AAHTw0blVdBKwrqoImAS-oLw2yd0lv4cd9s')


@bot.message_handler(content_types=['new_chat_members'])
def ban_new_chat_members(message):
    new_chat_members = message.new_chat_members
    chat = message.chat
    for new_member in new_chat_members:
        bot.restrict_chat_member(chat.id, new_member.id, can_send_messages=False)
        print('Заблокирован пользователь: {}'.format(new_member.first_name))
    bot.delete_message(chat.id, message.message_id)

@bot.message_handler(content_types=['text'])
def ban_spam_member(message):
    if message.from_user.username != 'andrey_reznik':
        chat_member = message.from_user
        chat = message.chat
        bot.restrict_chat_member(chat.id, chat_member.id, can_send_messages=False)
        print('Заблокирован пользователь: {}'.format(chat_member.first_name))
        bot.delete_message(chat.id, message.message_id)

bot.polling()
