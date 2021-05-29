import logging
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram.ext import CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

# настраиваем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)

#создаём апдейтер и диспетчер
updater = Updater(token='1795304763:AAE-bQVon0mMo51qJAZ2Sl5igKjY3uTX2X0')
dispatcher = updater.dispatcher

#функция для обработки команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Выберете язык/Choose you language")

    keyboard = [
        [
            InlineKeyboardButton("Ru", callback_data='Русский'),
            InlineKeyboardButton("En", callback_data='English'),
        ],
        [InlineKeyboardButton("Skip", callback_data='Skip')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    update.message.reply_text(callback_query.data.text)


#функция для обработки команды /hello
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Как тебя зовут?")

#функция эхо для команды /echo
def echo(update, context):
    help_text = f'''
    Привет, я не знаю команду {update.message.text}
    вот список команд, которые я знааю
    /start - команда для старта бота
    /hello - оманда для знакомства
    пока всё'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def help(update, context):
    help_text = f'''
    /bot : {context.bot.first_name}
    /link: {context.bot.link}
    /start - команда для старта бота
    /hello - команда для знакомства
    /help - отдаёт список команды
    пока всё'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    update.message.reply_text(text_caps)


def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Вы выбрали: {query.data}")

# список команд, обрабатываются последовательно
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(CallbackQueryHandler(button))

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

text_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(text_handler)



updater.start_polling()



