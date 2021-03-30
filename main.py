from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import NewMessage
from asyncio import sleep 

import telebot

bot = telebot.TeleBot('1673894668:AAFGDY8zeBKDFhGs2jUzZBL8-NySaoy204g')


@bot.message_handler(content_types=['cmd_call_admins'])
def cmd_call_admins(bot, update):
    users = telebot.get_participants(1001472566181)
print(users[0].first_name)

for user in users:
    if user.username is not None:
        print(user.username)
        telebot.send_message(1001472566181, "@{}".format(user.username))
        time.sleep(2)

bot.polling()
