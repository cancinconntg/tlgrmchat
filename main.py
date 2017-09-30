import telebot

bot = telebot.TeleBot('442140691:AAHTw0blVdBKwrqoImAS-oLw2yd0lv4cd9s')


@bot.message_handler(content_types=['new_chat_members'])
def ban_new_chat_members(message):
    new_chat_members = message.new_chat_members
    chat = message.chat
    for new_member in new_chat_members:
        print(new_member)
        if new_member.username != 'styr2245':
            try:
                bot.restrict_chat_member(chat.id, new_member.id, can_send_messages=False)
                print('Заблокирован пользователь: {}'.format(new_member.first_name))
            except Exception:
                pass
    bot.delete_message(chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def ban_spam_member(message):
    if message.from_user.username != 'styr2245':
        chat_member = message.from_user
        chat = message.chat
        try:
            bot.restrict_chat_member(chat.id, chat_member.id, can_send_messages=False)
            print('Заблокирован пользователь: {}'.format(chat_member.first_name))
        except Exception:
            pass
        bot.delete_message(chat.id, message.message_id)


@bot.message_handler(content_types=['left_chat_member'])
def delete_left_user_message(message):
    chat = message.chat
    bot.delete_message(chat.id, message.message_id)


bot.polling()
