import sys
import time
from colorama import init, Fore, Style
import os
import webbrowser


ascii_art = [
    Fore.MAGENTA + "  ██░ ██  ▓█████▒██   ██▒  ██████   ██░ ██   ██▓ ▓█████  ██▓   ▓█████▄ ",
    Fore.MAGENTA + "▒▓██░ ██  ▓█   ▀▒▒ █ █ ▒░▒██    ▒ ▒▓██░ ██ ▒▓██▒ ▓█   ▀ ▓██▒   ▒██▀ ██▌",
    Fore.MAGENTA + "░▒██▀▀██  ▒███  ░░  █   ░░ ▓██▄   ░▒██▀▀██ ▒▒██▒ ▒███   ▒██░   ░██   █▌",
    Fore.MAGENTA + " ░▓█ ░██  ▒▓█  ▄ ░ █ █ ▒   ▒   ██▒ ░▓█ ░██ ░░██░ ▒▓█  ▄ ▒██░   ░▓█▄   ▌",
    Fore.MAGENTA + " ░▓█▒░██▓▒░▒████▒██▒ ▒██▒▒██████▒▒ ░▓█▒░██▓░░██░▒░▒████▒░██████░▒████▓ ",
    Fore.MAGENTA + "  ▒ ░░▒░▒░░░ ▒░ ▒▒ ░ ░▓ ░▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒ ░▓  ░░░ ▒░ ░░ ▒░▓   ▒▒▓  ▒ ",
    Fore.MAGENTA + "  ▒ ░▒░ ░░ ░ ░  ░░   ░▒ ░░ ░▒  ░    ▒ ░▒░ ░░ ▒ ░░ ░ ░  ░░ ░ ▒   ░ ▒  ▒ ",
    Fore.MAGENTA + "  ░  ░░ ░    ░   ░    ░  ░  ░  ░    ░  ░░ ░░ ▒ ░    ░     ░ ░   ░ ░  ░ ",
    Fore.MAGENTA + "  ░  ░  ░░   ░   ░    ░        ░    ░  ░  ░  ░  ░   ░  ░    ░     ░    ",
    "",
    Fore.MAGENTA + "                 Boost Tools V.2.1 | 2qz_                     ",
    Fore.MAGENTA + "                This Tool made By   HexSheild               ",
]
def open_discord_link():
    url = "https://discord.gg/l-v"
    webbrowser.open(url)

if __name__ == "__main__":
    open_discord_link()


def print_ascii_art():
    for line in ascii_art:
        print(line)


print_ascii_art()

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()

def clear():
  
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        clear()  
        print_ascii_art() 
        print(Fore.MAGENTA + "           HEX SHIELD bst V.2.1")
        print(Fore.BLUE + "____________________________________________")
        print(Fore.MAGENTA + "1 | Stock Tokens")
        print(Fore.MAGENTA + "2 | NickName")
        print(Fore.MAGENTA + "3 | Boost Server")
        print(Fore.BLUE + "____________________________________________")
        print(Fore.MAGENTA + "4 | Close Tool" + Style.RESET_ALL)

        choice = input(Fore.BLUE + "Write 1,2,3,4 To Open Tool`s | ")

        if choice == '1':
            os.system('python python/code3.py')
        elif choice == '3':
            os.system('python python/code1.py')
        elif choice == '2':
            os.system('python python/code2.py')
        elif choice == '4':
            break
        else:
            print(Fore.RED + "Write 1,2,3,4 To Open Tool`s  Only!!! " + Fore.RESET)
            time.sleep(2)  

if __name__ == "__main__":
    main()
