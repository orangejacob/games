from termcolor import cprint

from commands import CommandInterpreter
from models.map import Map
from models.player import Player

"""
             Welcome to...
             
 ███▄ ▄███▓ ▒█████   ███▄    █   ██████ ▄▄▄█████▓▓█████  ██▀███      ██▓███   ██▓    ▄▄▄       ███▄    █ ▓█████▄▄▄█████▓
▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒   ▓██░  ██▒▓██▒   ▒████▄     ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▓██░ ██▓▒▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ▒██▄█▓▒ ▒▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒   ▒██▒ ░  ░░██████▒▓█   ▓██▒▒██░   ▓██░░▒████▒ ▒██▒ ░ 
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░   ▒▓▒░ ░  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░   ░▒ ░     ░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ░  ░   ░    
░      ░   ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░    ░         ░     ░░   ░    ░░         ░ ░    ░   ▒      ░   ░ ░    ░    ░      
       ░       ░ ░           ░       ░              ░  ░   ░                     ░  ░     ░  ░         ░    ░  ░        
                                                                  

             Storyline by:  @orangejacob
        Code Architecture:  @jsoconnell                               
"""


def main():
    cprint(' ███▄ ▄███▓ ▒█████   ███▄    █   ██████ ▄▄▄█████▓▓█████  ██▀███      ██▓███   ██▓    ▄▄▄       ███▄    █ ▓█████▄▄▄█████▓ ', 'green')
    cprint(' ▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒   ▓██░  ██▒▓██▒   ▒████▄     ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒', 'green')
    cprint(' ▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▓██░ ██▓▒▒██░   ▒██  ▀█▄  ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░', 'green')
    cprint(' ▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ▒██▄█▓▒ ▒▒██░   ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ', 'green')
    cprint(' ▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒   ▒██▒ ░  ░░██████▒▓█   ▓██▒▒██░   ▓██░░▒████▒ ▒██▒ ░ ', 'green')
    cprint(' ░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░   ▒▓▒░ ░  ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ', 'green')
    cprint(' ░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░   ░▒ ░     ░ ░ ▒  ░ ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ░  ░   ░    ', 'green')
    cprint(' ░      ░   ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░    ░         ░     ░░   ░    ░░         ░ ░    ░   ▒      ░   ░ ░    ░    ░      ', 'green')
    cprint('        ░       ░ ░           ░       ░              ░  ░   ░                     ░  ░     ░  ░         ░    ░  ░        ', 'green')
    print()
    player = Player(hp=30)
    map = Map()
    player.set_location(map.get_starting_location())
    game = CommandInterpreter(player, map)
    game.run()


main()