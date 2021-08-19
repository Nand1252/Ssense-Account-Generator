import requests
import names
import random
import string
import os
import time
from easy_password_generator import PassGen
from discord_webhook import DiscordWebhook, DiscordEmbed
from threading import Thread
from colorama import init, Fore
init()

clear = lambda: os.system('clear')
clear()

print(Fore.BLUE + '''
   _____ _____                                                         _      _____            
  / ____/ ____|                         /\                            | |    / ____|           
 | (___| (___   ___ _ __  ___  ___     /  \   ___ ___ ___  _   _ _ __ | |_  | |  __  ___ _ __  
  \___ \\___ \ / _ \ '_ \/ __|/ _ \   / /\ \ / __/ __/ _ \| | | | '_ \| __| | | |_ |/ _ \ '_  \ 
  ____) |___) |  __/ | | \__ \  __/  / ____ \ (_| (_| (_) | |_| | | | | |_  | |__| |  __/ | | |
 |_____/_____/ \___|_| |_|___/\___| /_/    \_\___\___\___/ \__,_|_| |_|\__|  \_____|\___|_| |_|

''')

accounts_number =int(input(Fore.BLUE + "How many accounts would like to create: "))

webhook = DiscordWebhook(url='Your Discord webhook here', username="SSense Account Gen")

def main(accounts_number):
    randomname = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
    Email = randomname + "@" + "cooldudesavage.xyz"
    pwo = PassGen()
    Password = pwo.generate()

    url = 'https://www.ssense.com/en-us/account/register'

    headers = {
        "authority": "www.ssense.com",
        "path": "/en-us/account/register",
        "scheme": "https",
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "115",
        "content-type": "application/x-www-form-urlencoded; charset=utf-8",
        "origin": "https://www.ssense.com",
        "referer": "https://www.ssense.com/en-us/account/login",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    data = {
        "email": Email,
        "password": Password,
        "confirmpassword": Password,
        "gender": "no-thanks",
        "source": "SSENSE_EN_SIGNUP",
    }

    time.sleep(1.5)
    
    response = requests.post(url, headers=headers, data=data)

    def webhook_send():
        embed = DiscordEmbed(title='Account Successfully Created', color='1eff00')
        embed.set_thumbnail(url='https://i.pinimg.com/originals/7b/85/f7/7b85f7112270f8f9fc2517095d8881ec.png')
        embed.set_footer(text='SSense Account Gen')
        embed.set_timestamp()
        embed.add_embed_field(name='Email', value=Email)
        embed.add_embed_field(name='Password', value=Password)

        webhook.add_embed(embed)
        webhook_response = webhook.execute()

    if response.status_code == 200:
        print(Fore.GREEN + "Account Successfully Generated!!")
        webhook_send()

    if response.status_code > 400:
        print(Fore.RED + "Error")

    f = open("Your filepath here", "a")
    f.write("\n" + Email + ":" + Password)
    f.close()

for i in range(accounts_number):
    t = Thread(target=main, args=(i,))
    time.sleep(1.5)
    t.start()