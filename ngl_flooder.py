import requests 
import os 
from pystyle import *
import time
import random
import sys


C = '\x1b[38;5;51m'
G = '\033[32m'
W = '\033[0m'
P = '\033[38;5;92m'
R = '\x1b[38;5;196m'

url = "https://ngl.link/api/submit"
headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "ngl.link",
        "Origin": "https://ngl.link",
    }
def banner():
  os.system('cls' if os.name == 'nt' else 'clear')
  print(Center.XCenter("""
\n
          ⣠⣴⣶⣾⣿⣿⣾⣷⣦⣤⣿⣶⣶⣤⣄⣀⢤⡀⠀⠀⠀⠀⢰⣴⣶⣷⣴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⣀⣀⣤⣤⣶⣶⣶⣦⣤⠤
        ⠠⠔⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠂⠀⠀
         ⠀⠀⠘⠋⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⢻⣿⣿⣿⣿⡏⠀⠀⠀⢀⣤⣾⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀⠀⠘⠀⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀
       ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠛⠟⠋⣿⣿⡿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠋⠙⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⠀⠸⠋⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⠋⠛⠇⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⢀⣿⣿⠁⠀⠈⢻⣿⣿⣿⣿⣿⡿⠋⠈⣿⣿⡏⠃⠀⠘⣿⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡏⠀⠀⠀⠈⣿⣿⣿⣿⣿⠀⠀⠀⠸⣿⣇⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⣼⣿⣿⣿⣿⣿⡄⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⢠⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""))
 


## payload
def generate_random_device_id():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(30))

def generate_random_username():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(8))

def send_moai_spam(username):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    games = random.choice(games)
    
    
    
    question = '🗿🗿🗿🗿🗿🗿🗿🗿'
    random_device_id = generate_random_device_id()
    random_generated_username = generate_random_username()
    
    data = {
        "username": username,
        "question": question,
        "deviceId": random_device_id,
        "gameSlug": games
    }
    
    response = requests.post(url, data=data, headers=headers)
    
    return username, random_generated_username
    
def send_exploit(username):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    games = random.choice(games)
    
    url = "https://ngl.link/api/submit"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "ngl.link",
        "Origin": "https://ngl.link",
    }
    
    question = 'fuck_you'
    random_device_id = generate_random_device_id()
    random_generated_username = generate_random_username()
    
    data = {
        "username": username,
        "question": question,
        "deviceId": random_device_id,
        "gameSlug": games
    }
    
    response = requests.post(url, data=data, headers=headers)
    
    return username, random_generated_username



def spam_heart(username):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    games = random.choice(games)
    
    url = "https://ngl.link/api/submit"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "ngl.link",
        "Origin": "https://ngl.link",
    }
    
    question = "♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️♥️💗💗💗💗💗💗💗💗💗💗💗💗💗💗💕💕💕💕💕💕"
    random_device_id = generate_random_device_id()
    random_generated_username = generate_random_username()
    
    data = {
        "username": username,
        "question": question,
        "deviceId": random_device_id,
        "gameSlug": games
    }
    
    response = requests.post(url, data=data, headers=headers)
    
    return username, random_generated_username
def spam_fuck(username):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    games = random.choice(games)
    
    url = "https://ngl.link/api/submit"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "ngl.link",
        "Origin": "https://ngl.link",
    }
    
    question = ('''
⠀⠀⠀⠀ ⠀⠀⠀⢀⡤⠤⣄⠀⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀  
 ⠀⠀⠀⢀⡾⠋⠻⡇⠀⠀⢸⣧⣀⡀⠀⠀⠀⠀ 
 ⠀⠀⢀⣾⠁⠀⠀⡇⠀⠀⢸⠁⠀⢹⣀⠀⠀⠀ 
 ⢀⡴⠋⡟⠀⠀⢠⡇⠀⠀⢸⠀⠀⠀⡇⠉⢆⠀ 
 ⡎⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠈⣆ 
 ⢷⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸ 
 ⠀⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾ 
 ⠀⠀⠈⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁ 
 ⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⠀⠀ 
 ⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀ 
 ⠀⠀⠀⠀⠀⠛⠒⠒⠒⠒⠒⠒⠒⠚⠃⠀⠀⠀''')
    random_device_id = generate_random_device_id()
    random_generated_username = generate_random_username()
    
    data = {
        "username": username,
        "question": question,
        "deviceId": random_device_id,
        "gameSlug": games
    }
    
    response = requests.post(url, data=data, headers=headers)
    
    return username, random_generated_username


def send_custom_spam(username, question):
    games = ['', 'confessions', '3words', 'wfriendship', 'rizzme', 'tbh', 'shipme', 'yourcrush', 'cancelled', 'dealbreaker']
    games = random.choice(games)
    
    url = "https://ngl.link/api/submit"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "ngl.link",
        "Origin": "https://ngl.link",
    }
    
    random_device_id = generate_random_device_id()
    random_generated_username = generate_random_username()
    
    data = {
        "username": username,
        "question": question,
        "deviceId": random_device_id,
        "gameSlug": games
    }
    
    response = requests.post(url, data=data, headers=headers)
    return username, random_generated_username



## requests

def deleter():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    print(Center.XCenter(C + "                 INBOX DELETER" + W))
    input_username = input("\n\t" + C + "Username" + W + ": ")
    if input_username is None or input_username.strip() == "":
        print("\n\t" + R + "Error" + W+ ": Please specify a username")
        time.sleep(2)
    print("\n")
    print(Center.XCenter(C + f"               Starting inbox deleter exploit for {input_username}" + W))
    print("\n")
    while True:
        try:
            username, random_username = send_exploit(input_username)
            print("  ["+ C + "+" + W + "]"+W+f" inbox deleter exploit successfully sent to {username}")
            
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    main()

def send_fuck():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    print(Center.XCenter(C + "                 SPAM FUCK" + W))
    input_username = input("\n\t" + C + "Username" + W + ": ")
    if input_username is None or input_username.strip() == "":
        print("\n\t" + R + "Error" + W+ ": Please specify a username")
        time.sleep(2)
    print("\n")
    print(Center.XCenter(C + f"               Starting spam fuck for {input_username}" + W))
    print("\n")
    while True:
        try:
            username, random_username = spam_fuck(input_username)
            print("  ["+ C + "+" + W + "]"+W+f" successfully sent to {username}")
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    main()
def send_heart():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    print(Center.XCenter(C + "                 HEART SPAM" + W))
    input_username = input("\n\t" + C + "Username" + W + ": ")
    if input_username is None or input_username.strip() == "":
        print("\n\t" + R + "Error" + W+ ": Please specify a username")
        time.sleep(2)
    print("\n")
    print(Center.XCenter(C + f"               Starting heart spam for {input_username}" + W))
    print("\n")
    while True:
        try:
            username, random_username = spam_heart(input_username)
            print("  ["+ C + "+" + W + "]"+W+f" successfully sent to {username}")
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    main()

def spam_moai():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    print(Center.XCenter(C + "                 MOAI SPAM" + W))
    input_username = input("\n\t" + C + "Username" + W + ": ")
    if input_username is None or input_username.strip() == "":
        print("\n\t" + R + "Error" + W+ ": Please specify a username")
        time.sleep(2)
        
        
        spam_cus_ques()
    print("\n")
    print(Center.XCenter(C + f"               Starting moai spam for {input_username}" + W))
    print("\n")
    while True:
        try:
            username, random_username = send_moai_spam(input_username)
            print("  ["+ C + "+" + W + "]"+W+f" successfully sent to {username}")
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    main()

def spam_cus_ques():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    
    print(Center.XCenter(C + "                 CUSTOM SPAM" + W))
    input_username = input("\n\t" + C + "Username" + W + ": ")
    if input_username is None or input_username.strip() == "":
        print("\n\t" + R + "Error" + W+ ": Please specify a username")
        time.sleep(2)
        
        
        spam_cus_ques()
    input_question = input("\t" + C + "Question" + W + ": ")
    if input_question is None or input_question.strip() == "":
        print("\n\t" + R + "Error" + W+ ": Please specify a question")
        time.sleep(2)
        
        
        spam_cus_ques()
    print("\n")
    print(Center.XCenter(C + f"               Starting custom spam for {input_username} with question {input_question}" + W))
    print("\n")
    while True:
        try:
            username, random_username = send_custom_spam(input_username, input_question)
            print("  ["+ C + "+" + W + "]"+W+f" successfully sent to {username}")
            
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
    main()
def main():
    banner()
    print(Center.XCenter(C + "              NGL FLOODER"))
    print(Center.XCenter(C + "                 Made by 0xsh1n" + W))
    print("\n\n")
    print(Center.XCenter("  ╔═════════════════╦════════════════╗"))
    print(Center.XCenter("  ║ 1. CUSTOM SPAM  ║ 2. SPAM HEARTS ║"))
    print(Center.XCenter("  ╠═════════════════╬════════════════╣"))
    print(Center.XCenter("  ║ 3. SPAM FUCK    ║ 4. SPAM MOAI   ║"))
    print(Center.XCenter("  ╠═════════════════╬════════════════╣"))
    print(Center.XCenter("                  ║ 5. DELETE INBOX ║ 6. \x1b[38;5;196mEXIT\033[97m        ║"))
    print(Center.XCenter("  ╚═════════════════╩════════════════╝"))
    choice = input("\n                   ~~> ")
    
    

    if choice == '1':
        spam_cus_ques()
    if choice == '2':
        send_heart()
    if choice == '3':
        send_fuck()
    if choice == '4':
        spam_moai()
    if choice == '5':
        deleter()
    if choice == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()
        
    else:
        print("\n" + R + "  Error" + W + ": Invalid choice. Please enter a valid option.")
        time.sleep(2)
        main()
    
        

if __name__ == "__main__":
    main()
    