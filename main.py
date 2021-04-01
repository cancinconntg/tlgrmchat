from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from telethon.events import NewMessage
from userbot.events import register
from userbot import bot
from asyncio import sleep

import telebot

bot = telebot.TeleBot('1753134503:AAHPxfcMLv8ucVMJAoaIFkqn6z4uWvmwXdY')


@bot.message_handler(content_types=['cmd_call_admins'])
def cmd_call_admins(bot, update):
    users = telebot.get_participants(1001326131404)
print(users[0].first_name)

for user in users:
    if user.username is not None:
        print(user.username)
        telebot.send_message(1001326131404, "@{}".format(user.username))
        time.sleep(2)

bot.polling()
