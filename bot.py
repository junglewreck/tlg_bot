# # -*- coding: utf-8 -*-
# import config
# import telebot
# import telegram
#
# bot = telebot.TeleBot(config.token)
#
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#     bot.send_message(message.chat.id, 'nu zdarova, epta')
#     bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
#
# if __name__ == '__main__':
#      bot.polling(none_stop=True)
import random, glob
import os
import subprocess
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from kinopoisk.movie import Movie
import logging
from imdbpie import Imdb

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO, PSW, GIVE_MEME, GIVE_FILM, VIBOR = range(8)

# def start(bot, update):
#     reply_keyboard = [['Boy', 'Girl', 'Other']]
#
#     update.message.reply_text(
#         'Hi! My name is Professor Bot. I will hold a conversation with you. '
#         'Send /cancel to stop talking to me.\n\n'
#         'Are you a boy or a girl?',
#         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
#
#     return GENDER

def start(bot, update):
    update.message.reply_text("/shot for GAS or /imdb for film")
    logger.info(update.message.text)
    return VIBOR

def vibor(bot, update):
    user = update.message.from_user
    logger.info(update.message.text)
    # if update.message.text == "/meme":
    #     chat_id = update.message.chat_id
    #     logger.info(chat_id)
    #     meme=random.choice(os.listdir("img/"))
    #     bot.send_photo(chat_id=chat_id, photo=open("img/"+meme, 'rb'))
    if update.message.text == "/shot":
	update.message.reply_text("please wait...")
        transfer = subprocess.call('./transfer.sh', shell=True)
        chat_id = update.message.chat_id
        logger.info(chat_id)
        bot.send_photo(chat_id=chat_id, photo=open("shot1.jpg", 'rb'))
    # elif update.message.text == "/imdb":
    #     imdb = Imdb()
    #     film =  imdb.top_250()
    #     rnd = (random.randint(0,249))
    #     full = film[rnd]
    #     title = film[rnd].get('title')
    #
    #     update.message.reply_text("please wait...")
    #     movie_list = Movie.objects.search(title)
    #     aidi =  movie_list[0].id
    #     movie_kinopoisk = Movie(id=aidi)
    #     movie_kinopoisk.get_content('main_page')
    #     title_kinopoisk = movie_kinopoisk.title
    #     year_kinopoisk = movie_kinopoisk.year
    #     description = movie_kinopoisk.plot
    #     # year_kinopoisk = str(year_kinopoisk)
    #     # print title_kinopoisk
    #
    #     poster_full = film[rnd].get('image')
    #     poster_img = poster_full.get('url')
    #
    #     # update.message.reply_text(title + "/" + title_kinopoisk + "(" + str(movie_kinopoisk.year) + ")" )
    #     update.message.reply_text("%s/%s(%s) \n %s" % (title, title_kinopoisk, year_kinopoisk, description))
    #     update.message.reply_text(poster_img)
    else:
        update.message.reply_text('Bye!')
        return ConversationHandler.END

# def intro(bot, update):
#     update.message.reply_text('Password Please')
#     user = update.message.from_user
#     logger.info(update.message.text)
#     return gender
#

# tries = 0
# def psw_check(bot, update):
#     user = update.message.from_user
#     chat_id = update.message.chat_id
#     logger.info(tries)
#     if tries > 4:
#         update.message.reply_text('fuck u, bye')
#         return ConversationHandler.END
#     elif update.message.text == '6200433':
#         update.message.reply_text('u r wlcm, write /meme, to take meme or /imdb to take film')
#         return GIVE_FILM
#     else:
#         update.message.reply_text('the psw is incorrect')
#         global tries
#         tries += 1


def give_meme(bot, update):
    user = update.message.from_user
    chat_id = update.message.chat_id
    logger.info(chat_id)
    meme=random.choice(os.listdir("img/"))
    bot.send_photo(chat_id=chat_id, photo=open("img/"+meme, 'rb'))

def give_film(bot, update):
    user = update.message.from_user
    chat_id = update.message.chat_id
    logger.info(chat_id)
    update.message.reply_text(title)
    update.message.reply_text(poster_img)

def gender(bot, update):
    user = update.message.from_user
    logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('I see! Please send me a photo of yourself, '
                              'so I know what you look like, or send /skip if you don\'t want to.',
                              reply_markup=ReplyKeyboardRemove())

    return PHOTO


def photo(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text('Gorgeous! Now, send me your location please, '
                              'or send /skip if you don\'t want to.')

    return LOCATION


def skip_photo(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text('I bet you look great! Now, send me your location please, '
                              'or send /skip.')

    return LOCATION


def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    update.message.reply_text('Maybe I can visit you sometime! '
                              'At last, tell me something about yourself.')

    return BIO


def skip_location(bot, update):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text('You seem a bit paranoid! '
                              'At last, tell me something about yourself.')

    return BIO


def bio(bot, update):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you! I hope we can talk again some day.')

    return ConversationHandler.END


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("194467749:AAE6-m8o0b22TJwdiRFYrUM0kkQdhOlmLjw")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(

        entry_points = [CommandHandler('start', start)],
        states={
            GENDER: [RegexHandler('^(Boy|Girl|Other)$', gender)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location)],

            BIO: [MessageHandler(Filters.text, bio)],

            # PSW: [MessageHandler(Filters.text, psw_check)],
            # GIVE_MEME: [MessageHandler(Filters.text, give_meme)]
            GIVE_MEME: [CommandHandler('meme', give_meme)],
            GIVE_FILM: [CommandHandler('imdb', give_film)],
            VIBOR: [MessageHandler('', vibor)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
