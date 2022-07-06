from subprocess import call
from requests import request
import telebot as tg

from modules.warface_web import warface_request_user

with open('files/token', encoding='utf8') as file:
    file_str_lines = file.readlines()

    token = file_str_lines[0].replace('\n', '')
    bot = tg.TeleBot(token)

    file.close()

@bot.message_handler(commands=['start'], chat_types=['private'])
def start_function(message):
    bot.send_message(message.from_user.id, 'Warface informer - Noda')

@bot.message_handler(commands=['userinfo'], chat_types=['private'])
def userinfo_function(message):
    request = bot.send_message(message.from_user.id, 'Type your name: ')
    bot.register_next_step_handler(request, userinfo_report_function)

def userinfo_report_function(message):
    warface_username = message.text

    result = warface_request_user(warface_username)

    if result[0] != None:
        bot.send_message(message.from_user.id, f'Account statistic of player {result[1]}\n\nUser level: {result[3]} lvl\nUser experience: {result[2]} exp.\nUser playtime: {round(result[14] / 36000, 1)} hrs\n\nUser ID: {result[0]}\n\nPVP\nFavorite class - {result[15]}\nAll kills - {result[4]}\nEnemy kills - {result[6]}\nFriendly kills - {result[5]}\nDeaths - {result[7]}\nK/D - {result[8]}\nGames - {result[19]}\nWins - {result[17]}\nLoses - {result[18]}\n\nPVE\nFavorite class - {result[16]}\nAll kills - {result[9]}\nEnemy kills - {result[11]}\nFriendly kills - {result[10]}\nDeaths - {result[12]}\nK/D - {result[13]}\nGames - {result[22]}\nWins - {result[20]}\nLoses - {result[21]}')
    else:
        bot.send_message(message.from_user.id, f"User not found or site don't response\nCode: {result[1]}")

bot.polling(non_stop=True)
