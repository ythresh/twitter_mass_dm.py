import requests as r
import tweepy, json, time, random, os
from threading import Thread


with open('config_self_twitter.json', 'r') as f:
    config = json.loads(f.read())
    api_key = config['api_key']
    api_secret = config['api_secret']
    access_token = config['access_token']
    access_secret = config['access_secret']
    bearer_user = config['bearer']
    bearer_api = config['bearer_api']

with open('message.txt', 'r') as f:
    msg = f.read()


def send(message, api_key, api_secret, acess_token, secret, bearear_api):
        with open('ids.txt', 'r') as f:
            auth = tweepy.OAuth1UserHandler(consumer_key=api_key, consumer_secret=api_secret, access_token=acess_token, access_token_secret=secret)
            api_sender = tweepy.API(auth)
            content = f.readlines()
            content = [x.rstrip('\n') for x in content]
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''

                                     
 _____ _____ _____ ____  _____ _____ 
|   __|   __|   | |    \|   __| __  |
|__   |   __| | | |  |  |   __|    -|
|_____|_____|_|___|____/|_____|__|__|
                                     



Discord - $L9 Akira.py#3301
Melhor loja - discord.gg/lownine       
''')
            for u in content:
                
                try:
                    print(api_sender.send_direct_message(recipient_id=u, text=message))
                    api2 = tweepy.Client(bearer_token=bearear_api)
                    user_ = api2.get_user(id=u)
                    print(f'[+] - DM ENVIADA COM SUCESSO PARA @{user_[0]}')

                except Exception as e:
                    if 'You cannot send messages to users who are not following you.' in str(e):
                        api2 = tweepy.Client(bearer_token=bearear_api)
                        user_ = api2.get_user(id=u)
                        print(f'[~] - DM BLOCK @{user_[0]}')
                        pass
                    elif '226' in str(e):
                        print('PAUSA PARA EVITAR RATE LIMIT')
                        time.sleep(600)
                        try:
                            (api_sender.send_direct_message(recipient_id=u, text=message))
                            api2 = tweepy.Client(bearer_token=bearear_api)
                            user_ = api2.get_user(id=u)
                            print(f'[+] - DM ENVIADA COM SUCESSO PARA @{user_[0]}')
                        except Exception as e:
                            if 'You cannot send messages to users who are not following you.' in str(e):
                                api2 = tweepy.Client(bearer_token=bearear_api)
                                user_ = api2.get_user(id=u)
                                print(f'DM BLOCK @{user_[0]}')
                                pass
                            pass
                    elif '420' in str(e):
                        print('[!] - Em rate limit.')
                        exit()



def scrappar(username, token1, token2):
    h = {
    'Host': 'twitter.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'authorization': token1,
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-client-language': 'en',
    'x-twitter-active-user': 'yes',
    'content-type': 'application/x-www-form-urlencoded',
    'x-csrf-token': '66c2c9c47018f23ad0bda642eb3645acd4e4333af5e0e647e99fb59ae76389af407426e2f3ca7ae1cb704efac93a942b06ea516dfe1c6a23c50f2d4c7cea832f6eeb87ad72a547abf5c9dc709bf9e5fc',
    'Origin': 'https://twitter.com',
    'Referer': 'https://twitter.com/home',
    'Cookie': 'guest_id_marketing=v1%3A166145103892301611; guest_id_ads=v1%3A166145103892301611; personalization_id="v1_ue6WXpfQfn2OqLGTCsbNcg=="; guest_id=v1%3A166145103892301611; ct0=66c2c9c47018f23ad0bda642eb3645acd4e4333af5e0e647e99fb59ae76389af407426e2f3ca7ae1cb704efac93a942b06ea516dfe1c6a23c50f2d4c7cea832f6eeb87ad72a547abf5c9dc709bf9e5fc; gt=1562865063413039107; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAMMM9aCAToMY3NyZl9p%250AZCIlOTUyNDUyZjdmZGViMTA2NzhiZTEzZTJiZTNlZTdhN2Q6B2lkIiU0ODky%250AYzM5Y2RlZmZkZjdiYjU2OTBmYmUwZjA4ZGJkMg%253D%253D--313888e0b93fb914fa3e9638505a77b548fe9ad6; _ga=GA1.2.97740880.1661451091; _gid=GA1.2.2065820486.1661451091; kdt=v2qP4CDPYNMbXc2dMME2bLOunwUjg1zKyB7JHyjA; twid=u%3D1492941110045519874; auth_token=a6c5e59ccb5fc1587683c676ead8d6145e1ed94d; att=1-mm1vljgM8d39aILUGN6VdLFqe87KkznKgq9lxQq1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
    }
    f = open('ids.txt', 'a')
    api = tweepy.Client(bearer_token=token2)
    user_ = api.get_user(username=username)
    user = (api.get_users_followers(id=user_[0].id, max_results=1000))
    users = user[0]
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'''  
                                   
 _____                             
|   __|___ ___ ___ ___ ___ ___ ___ 
|__   |  _|  _| .'| . | . | -_|  _|
|_____|___|_| |__,|  _|  _|___|_|  
                  |_| |_|          

Discord - $L9 Akira.py#3301
Melhor loja - discord.gg/lownine

INICIANDO EM SCRAPPING NO USUARIO {username}
''')
    for u in users:
        id = u.id
        req1 = r.get(f'https://twitter.com/i/api/1.1/dm/user_updates.json', headers=h)
        if req1.status_code == 200:
            cursos_get = json.loads(req1.text)
            try:
                cursor = (cursos_get['user_inbox']['cursor'])
                req2 = r.get(f'https://twitter.com/i/api/1.1/dm/user_updates.json?cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&include_ext_collab_control=true&dm_users=true&include_groups=true&include_inbox_timelines=true&include_ext_media_color=true&supports_reactions=true&active_conversation_id={id}-1492941110045519874&nsfw_filtering_enabled=false&cursor={cursor}&include_ext_edit_control=true&ext=mediaColor,altText,mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe', headers=h)
                if '"read_only":true' in req2.text:
                    print(f'[~] - DM BLOQUEADA, NAO IRA PRA LISTA - @{u.username}')
                    time.sleep(int(0.5))
                    pass
                elif '"read_only":false' in req2.text:
                    print(f'[+] - USUARIO ADICIONADO NA LISTA - @{u.username} ')
                    f.write(f'{id}\n')
                elif req2.text == '{"errors":[{"message":"Rate limit exceeded","code":88}]}':
                    print('[~] - RATE LIMIT, VOLTANDO EM 10 MINUTOS')
                    time.sleep(300)
                    pass
            except:
                pass
        elif req1.status_code == 429:
            print('[~] - RATE LIMIT, VOLTANDO EM 10 MINUTOS')
            time.sleep(600)
            pass
os.system('cls' if os.name == 'nt' else 'clear')
print('''
  ___  _    _            ___  ___               _________  ___  _____ _____  _____ _     
 / _ \| |  (_)           |  \/  |               |  _  \  \/  | |_   _|  _  ||  _  | |    
/ /_\ \ | ___ _ __ __ _  | .  . | __ _ ___ ___  | | | | .  . |   | | | | | || | | | |    
|  _  | |/ / | '__/ _` | | |\/| |/ _` / __/ __| | | | | |\/| |   | | | | | || | | | |    
| | | |   <| | | | (_| | | |  | | (_| \__ \__ \ | |/ /| |  | |   | | \ \_/ /\ \_/ / |____
\_| |_/_|\_\_|_|  \__,_| \_|  |_/\__,_|___/___/ |___/ \_|  |_/   \_/  \___/  \___/\_____/
                                                                                         
                                                                                                                                                                                                                                                              
Made by - $L9 Akira#3301
Best Store - discord.gg/lownine

''')

modo = int(input('MODOS :\n[+] - 1 - SCRAPPER\n[*] - 2 - SENDER\n[$] - 3 - SENDER + SCRAPPER\n#INSIRA UM MODO - '))
with open('alvos.txt', 'r') as f:
    content = f.readlines()
    content = [x.rstrip('\n') for x in content] 
    if modo == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        for lines in content:
            scrappar(username=lines, token1=bearer_user, token2=bearer_api)
    elif modo == 3:
        for lines in content:
            scrappar(username=lines, token1=bearer_user, token2=bearer_api)
        send(message=msg, api_key=api_key, api_secret=api_secret, acess_token=access_token, secret=access_secret, bearear_api=bearer_api)
    elif modo == 2:
        send(message=msg, api_key=api_key, api_secret=api_secret, acess_token=access_token, secret=access_secret, bearear_api=bearer_api)