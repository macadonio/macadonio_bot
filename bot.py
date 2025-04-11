""" Project TG_macadonio_bot """
import  telebot, random, config c
from translate import Translator
from telebot import types
transl = Translator(from_lang='en', to_lang='ru')
bot = telebot.TeleBot("6732940033:AAFvPegFwtEs_IOIrj3e7Pf8Lh7iQCIPmd4")

@bot.message_handler(commands=["start"])
def buttom(message):
    markup_inline = types.InlineKeyboardMarkup()
    time_1 = types.InlineKeyboardButton(text='Present Simple', callback_data="1")
    time_2 = types.InlineKeyboardButton(text='Present Continius', callback_data="2")
    time_3 = types.InlineKeyboardButton(text='Present Perfect', callback_data="3")
    time_4 = types.InlineKeyboardButton(text='Present Perfect Continius', callback_data="4")
    time_5 = types.InlineKeyboardButton(text='Past Simple', callback_data="5")
    time_6 = types.InlineKeyboardButton(text='Past Continues', callback_data="6")
    time_7 = types.InlineKeyboardButton(text='Past Perfect', callback_data="7")
    time_8 = types.InlineKeyboardButton(text='Past Perfect Continius', callback_data="8")
    time_9 = types.InlineKeyboardButton(text='Future simple', callback_data="9")
    time_10 = types.InlineKeyboardButton(text='Future Continues', callback_data="10")
    time_11 = types.InlineKeyboardButton(text='Future Perfect', callback_data="11")
    time_12 = types.InlineKeyboardButton(text='Future Perfect Continius', callback_data="12")
    markup_inline.add(time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8, time_9,time_10, time_11, time_12)
    bot.send_message(message.chat.id, 'Здравствуйте, я macadonio_bot выберите задание чтобы продолжить ', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda callback: callback.data)
def callback_inline(call):
    if call.data == "1":
        works = open("Present Simple.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "2":
        works = open("Present Continues.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "3":
        works = open("Present Perfect.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "4":
        works = open("Present Perfect Continues.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "5":
        works = open("Past Simple.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "6":
        works = open("Past Continius.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "7":
        works = open("Past Perfect.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "8":
        works = open("Past Perfect Continues.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "9":
        works = open("Future Simple.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "10":
        works = open("Future Continues.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "11":
        works = open("Future Perfect.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    elif call.data == "12":
        works = open("Future Perfect Continues.txt", encoding="utf-8")
        lines = works.readlines()
        bot.send_message(call.message.chat.id, random.choice(lines))
        works.close()
    else:
        ()
@bot.message_handler(content_types  = ['text'])
def tr (message):
    translator= Translator(from_lang='en', to_lang='ru')
    translation = translator.translate(message.text)
    bot.send_message(message.chat.id, translation)

bot.polling(none_stop=True)
