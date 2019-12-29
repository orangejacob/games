from .chest import Chest
from .item import Item
from .monster import Monster
from .room import Room
from .weapon import Weapon


class Map:
    def __init__(self):
        self.starting_location = None
        self.room_directory = None
        self.build_map()

    def build_map(self):
        pass
        # TODO set up the rooms

        # call this at the end with a list of all the rooms
        # self.setup_directory()

    # Dad's fancy way of setting up the directory
    def setup_directory(self, *args):
        for room in args:
            self.room_directory.update({
                room.name.lower(): room
            })

    def get_starting_location(self):
        return self.starting_location

    def find_room_by_name(self, name: str):
        room = self.room_directory.get(name)
        return room
