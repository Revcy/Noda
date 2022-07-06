import requests 

def warface_request_user(username):
    parameters = {
        'name': username,
    }

    api = requests.get('http://api.warface.ru/user/stat/', params=parameters)

    wfinfo = api.json()
    
    if api:
        wf_user_id = wfinfo['user_id']                          # 0
        wf_nickname = wfinfo['nickname']                        # 1
        wf_exp = wfinfo['experience']                           # 2
        wf_rank = wfinfo['rank_id']                             # 3
        wf_pvp_all_kills = wfinfo['kill']                       # 4
        wf_pvp_friendly_kills = wfinfo['friendly_kills']        # 5
        wf_pvp_enemy_kills = wfinfo['kills']                    # 6
        wf_pvp_death = wfinfo['death']                          # 7
        wf_pvp_frags_kd = wfinfo['pvp']                         # 8
        wf_pve_all_kills = wfinfo['pve_kill']                   # 9
        wf_pve_friendly_kills = wfinfo['pve_friendly_kills']    # 10
        wf_pve_enemy_kills = wfinfo['pve_kills']                # 11
        wf_pve_death = wfinfo['pve_death']                      # 12
        wf_pve_frags_kd = wfinfo['pve']                         # 13
        wf_playtime_seconds = wfinfo['playtime']                # 14
        wf_favorite_pvp_class = wfinfo['favoritPVP']            # 15
        wf_favorite_pve_class = wfinfo['favoritPVE']            # 16
        wf_pvp_wins = wfinfo['pvp_wins']                        # 17
        wf_pvp_lose = wfinfo['pvp_lost']                        # 18
        wf_pvp_all = wfinfo['pvp_all']                          # 19
        wf_pve_wins = wfinfo['pve_wins']                        # 20
        wf_pve_lose = wfinfo['pve_lost']                        # 21
        wf_pve_all = wfinfo['pve_all']                          # 22

        result = [wf_user_id, wf_nickname, wf_exp, wf_rank, wf_pvp_all_kills, wf_pvp_friendly_kills, wf_pvp_enemy_kills, wf_pvp_death, wf_pvp_frags_kd, wf_pve_all_kills, wf_pve_friendly_kills, wf_pve_enemy_kills, wf_pve_death, wf_pve_frags_kd, wf_playtime_seconds, wf_favorite_pvp_class, wf_favorite_pve_class, wf_pvp_wins, wf_pvp_lose, wf_pvp_all, wf_pve_wins, wf_pve_lose, wf_pve_all]

        # result = f'Username: {wf_nickname}\nUser ID: {wf_user_id}\n\nUser level: {wf_rank}\nUser experience: {wf_exp} exp\nUser playtime: {round(wf_playtime_seconds / 36000, 1)} hours\n\nPVP Information:\n\nAll kills - {wf_pvp_all_kills}\nEnemy kills - {wf_pvp_enemy_kills}\nFriendly kills - {wf_pvp_friendly_kills}\nDeaths - {wf_pvp_death}\nK/D - {wf_pvp_frags_kd}\nFavorite class - {wf_favorite_pvp_class}\nGames - {wf_pvp_all}\nWins - {wf_pvp_wins}\nLoses - {wf_pvp_lose}\n\nPVE Information:\n\nAll kills - {wf_pve_all_kills}\nEnemy kills - {wf_pve_enemy_kills}\nFriendly kills - {wf_pve_friendly_kills}\nDeaths - {wf_pve_death}\nK/D - {wf_pve_frags_kd}\nFavorite class - {wf_favorite_pve_class}\nGames - {wf_pve_all}\nWins - {wf_pve_wins}\nLoses - {wf_pve_lose}'
    else:
        wf_error_code = wfinfo['code']

        result = [None, wf_error_code]

        # result = f"User not found or site don't response \nCode: {wf_error_code}"

    return result
