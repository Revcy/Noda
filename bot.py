import telebot as tg
import requests 

with open('token.txt', encoding='utf8') as file:
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
    parameters = {
        'name': message.text,
    }

    api = requests.get('http://api.warface.ru/user/stat/', params=parameters)

    wfinfo = api.json()
    
    if api:
        wf_user_id = wfinfo['user_id']
        wf_nickname = wfinfo['nickname']
        wf_exp = wfinfo['experience']
        wf_rank = wfinfo['rank_id']
        wf_pvp_all_kills = wfinfo['kill']
        wf_pvp_friendly_kills = wfinfo['friendly_kills']
        wf_pvp_enemy_kills = wfinfo['kills']
        wf_pvp_death = wfinfo['death']
        wf_pvp_frags_kd = wfinfo['pvp']
        wf_pve_all_kills = wfinfo['pve_kill']
        wf_pve_friendly_kills = wfinfo['pve_friendly_kills']
        wf_pve_enemy_kills = wfinfo['pve_kills']
        wf_pve_death = wfinfo['pve_death']
        wf_pve_frags_kd = wfinfo['pve']
        wf_playtime_seconds = wfinfo['playtime']
        wf_favorite_pvp_class = wfinfo['favoritPVP']
        wf_favorite_pve_class = wfinfo['favoritPVE']
        wf_pve_wins = wfinfo['pve_wins']
        wf_pve_lose = wfinfo['pve_lost']
        wf_pve_all = wfinfo['pve_all']
        wf_pvp_wins = wfinfo['pvp_wins']
        wf_pvp_lose = wfinfo['pvp_lost']
        wf_pvp_all = wfinfo['pvp_all']

        result = f'Username: {wf_nickname}\nUser ID: {wf_user_id}\n\nUser level: {wf_rank}\nUser experience: {wf_exp} exp\nUser playtime: {round(wf_playtime_seconds / 36000, 1)} hours\n\nPVP Information:\n\nAll kills - {wf_pvp_all_kills}\nEnemy kills - {wf_pvp_enemy_kills}\nFriendly kills - {wf_pvp_friendly_kills}\nDeaths - {wf_pvp_death}\nK/D - {wf_pvp_frags_kd}\nFavorite class - {wf_favorite_pvp_class}\nGames - {wf_pvp_all}\nWins - {wf_pvp_wins}\nLoses - {wf_pvp_lose}\n\nPVE Information:\n\nAll kills - {wf_pve_all_kills}\nEnemy kills - {wf_pve_enemy_kills}\nFriendly kills - {wf_pve_friendly_kills}\nDeaths - {wf_pve_death}\nK/D - {wf_pve_frags_kd}\nFavorite class - {wf_favorite_pve_class}\nGames - {wf_pve_all}\nWins - {wf_pve_wins}\nLoses - {wf_pve_lose}'
    else:
        wf_error_code = wfinfo['code']

        result = f"User not found or site don't response \nCode: {wf_error_code}"

    bot.send_message(message.from_user.id, result)

bot.polling(non_stop=True)