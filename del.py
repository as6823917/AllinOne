import asyncio
from os import environ
from pyrogram import Client, filters, idle


GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"



@Client.on_message(filters.command('startdel') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@Client.on_message(filters.chat(GROUPS))
async def deletefun(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Client.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
