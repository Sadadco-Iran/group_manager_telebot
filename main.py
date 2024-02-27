import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import *
import datetime
bot = telebot.TeleBot(token)

admin = [6380845241]

@bot.message_handler(func=lambda m:m.text.startswith('سکوت '))
def restrictt(m):
    if int(m.from_user.id) in admin:
        shok = int(m.text.split()[-1])
        date = datetime.datetime.now() + datetime.timedelta(minutes=shok)
        until = int(date.timestamp())


        bot.reply_to(m, f"""
                {m.reply_to_message.from_user.first_name} با موفقیت {shok} دقیقه سکوت شد
                """)
        bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id,
                                 until_date=until,
                                 can_add_web_page_previews=False,
                                 can_change_info=False,
                                 can_send_messages=False,
                                 can_invite_users=False,
                                 can_pin_messages=False,
                                 can_send_media_messages=False,
                                 can_send_polls=False,
                                 can_send_other_messages=False


    )

@bot.message_handler(func=lambda m:m.text.startswith('پاکسازی '))
def koll(message):
    if int(message.from_user.id) in admin:
        ted = int(message.text.split()[-1])


    if 0 < int(ted) <= 1000:
        bot.send_message(message.chat.id, "لطفا صبور باشید", reply_to_message_id=message.id, parse_mode='HTML')
        for i in range(message.id - int(ted), message.id + 1):
            try:
                bot.delete_message(message.chat.id, i)
            except:
                pass
        bot.send_message(message.chat.id, "» تعداد %d پیام با موفقیت پاکسازی شد" % int(ted), parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, " تعداد باید بین 1 تا 1000 باشد.", reply_to_message_id=message.id, parse_mode='HTML')




@bot.message_handler(func=lambda m:True)
def text_tp(m):
    if int(m.from_user.id) in admin:
        if m.text == "پین":
            pin(m)
        elif m.text == "افزودن ادمین":
            promote(m)
        elif m.text == "حذف ادمین":
            demote(m)
        elif m.text == "بن":
            ban(m)
        elif m.text == "حذف بن":
            unban(m)
        elif m.text == "بن داعم":
            banPer(m)
        elif m.text == "حذف سکوت":
            unrestrict(m)





#############################

def pin(m):
        bot.pin_chat_message(m.chat.id, m.reply_to_message.id)
        bot.reply_to(m, "پیام مورد نظر با موفقیت پین شد")

def promote(m):
    bot.reply_to(m, f"""
        {m.reply_to_message.from_user.first_name} با موفقیت ادمین شد
        """)
    bot.promote_chat_member(m.chat.id,m.reply_to_message.json['from']['id'],
    can_change_info=True,
    can_delete_messages=True,
    can_edit_messages=True,
    can_invite_users=True,
    can_manage_chat=True,
    can_manage_topics=False,
    can_manage_video_chats=True,
    can_manage_voice_chats=True,
    can_pin_messages=True,
    can_post_messages=True,
    can_promote_members=True,
    can_restrict_members=True
                            )

def demote(m):
    bot.reply_to(m, f"""
    {m.reply_to_message.from_user.first_name} با موفقیت از ادمینی حذف شد
    """)
    bot.promote_chat_member(m.chat.id, m.reply_to_message.json['from']['id'],
       can_change_info=False,
       can_delete_messages=False,
       can_edit_messages=False,
       can_invite_users=False,
       can_manage_chat=False,
       can_manage_topics=False,
       can_manage_video_chats=False,
       can_manage_voice_chats=False,
       can_pin_messages=False,
       can_post_messages=False,
       can_promote_members=False,
       can_restrict_members=False

)
def mmd(m):
    bot.delete_message(chat_id=m.chat.id,message_id=m.reply_to_message.message_id)
def ban(m):
    bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
    bot.reply_to(m,f"{m.reply_to_message.from_user.id} با موفقیت بن شد")



def unban(m):
    bot.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
    bot.reply_to(m, f"{m.reply_to_message.from_user.id} با موفقیت حذف بن شد")


def banPer(m):
    bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id, revoke_messages=True)
    bot.reply_to(m,f"{m.reply_to_message.from_user.id} با موفقیت بن داعم  شد")


def restrict(m):

    date = datetime.datetime.now() + datetime.timedelta(minutes=10)
    until = int(date.timestamp())

    bot.reply_to(m, f"""
        {m.reply_to_message.from_user.first_name} با موفقیت سکوت شد
        """)
    bot.restrict_chat_member(m.chat.id,m.reply_to_message.from_user.id,
    until_date=until,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_send_messages=False,
    can_invite_users=False,
    can_pin_messages=False,
    can_send_media_messages=False,
    can_send_polls=False,
    can_send_other_messages=False


    )


def unrestrict(m):
    bot.reply_to(m, f"""
            {m.reply_to_message.from_user.first_name} با موفقیت حذف سکوت شد
            """)
    bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id,
    until_date=False,
    can_add_web_page_previews=True,
    can_change_info=True,
    can_send_messages=True,
    can_invite_users=True,
    can_pin_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_send_other_messages=True


 )






bot.infinity_polling(timeout=100)