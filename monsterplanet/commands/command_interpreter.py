from .attack import Attack
from .drop import Drop
from .enter import Enter
from .exit import Exit
from .help import Help
from .inventory import Inventory
from .look import Look
from .lookat import LookAt
from .loot import Loot
from .pickup import Pickup
from .rename import Rename
from .whereto import WhereTo

from models import Map
from models import Player


class CommandInterpreter:
    """
    Processes commands input by player at command prompt.
    """
    def __init__(self, player: Player, map: Map):
        self.player = player
        self.house = map

        help_command = Help('help', player, map)
        self.commands = [
            Attack('attack', player, map),
            Drop('drop', player, map),
            Enter('enter', player, map),
            Exit('exit', player, map),
            help_command,
            Inventory('inventory', player, map),
            Look('look', player, map),
            LookAt('look at', player, map),
            Loot('loot', player, map),
            Pickup('pickup', player, map),
            Rename('change my name', player, map),
            WhereTo('where to', player, map)
        ]
        help_command.set_all_commands(self.commands)

    def run(self):
        while True:
            cmd = self.get_next_command()
            self.interpret_command(cmd)

    @staticmethod
    def get_next_command() -> str:
        cmd = input('> ')
        return cmd

    def interpret_command(self, command_str: str):
        command_str = command_str.lower()
        words = command_str.split()
        matched_command_str = ''
        text = ''
        matched_command = None

        for word in words:
            if matched_command:
                if len(text) > 0:
                    text += ' '
                text += word
            else:
                if len(matched_command_str) > 0:
                    matched_command_str += ' '
                matched_command_str += word
                for cmd in self.commands:
                    if cmd.matches(matched_command_str):
                        matched_command = cmd

        if matched_command:
            matched_command.do(text)
        else:
            print('Sorry, I don\'t recognize that command.')
