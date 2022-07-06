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

        keys = tg.types.InlineKeyboardMarkup(row_width=2)
        button1 = tg.types.InlineKeyboardButton(text='PVP Stat', callback_data="pvp_user_stat_" + result[1])
        button2 = tg.types.InlineKeyboardButton(text='PVE Stat', callback_data="pve_user_stat_" + result[1])
        keys.add(button1, button2)

        bot.send_message(message.from_user.id, f'Account statistic of player {result[1]}\n\nUser level: {result[3]} lvl\nUser experience: {result[2]} exp.\nUser playtime: {round(result[14] / 36000, 1)} hrs\n\nUser ID: {result[0]}', reply_markup=keys)
    else:
        bot.send_message(message.from_user.id, f"User not found or site don't response\nCode: {result[1]}")

@bot.callback_query_handler(func=lambda callback: callback.data)
def userinfo_add_additionally_inforamtion(callback):
    callback_response = callback.data[:13]
    warface_username = callback.data[14:]

    # print("Starting GET " + callback.data)
    result = warface_request_user(warface_username)
    # print("Ending GET " + callback.data)
    
    if callback_response == 'pvp_user_stat':
        bot.send_message(callback.from_user.id, f'PVP Statistic of player {warface_username}\n\nFavorite class - {result[15]}\nAll kills - {result[4]}\nEnemy kills - {result[6]}\nFriendly kills - {result[5]}\nDeaths - {result[7]}\nK/D - {result[8]}\nGames - {result[19]}\nWins - {result[17]}\nLoses - {result[18]}')
    elif callback_response == 'pve_user_stat':
        bot.send_message(callback.from_user.id, f'PVE Statistic of player {warface_username}\n\nFavorite class - {result[16]}\nAll kills - {result[9]}\nEnemy kills - {result[11]}\nFriendly kills - {result[10]}\nDeaths - {result[12]}\nK/D - {result[13]}\nGames - {result[22]}\nWins - {result[20]}\nLoses - {result[21]}')

bot.polling(non_stop=True)
