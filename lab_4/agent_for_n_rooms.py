
from agent_for_two_rooms import Agent

class VaccumAgent1 (Agent):
    def __init__(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        current_room = self.environment.currentRoom
        all_rooms = self.environment.rooms
        total_rooms = len(all_rooms)

        if current_room.status == 'dirty':
            return 'clean'

        current_index = all_rooms.index(current_room)
        next_index = (current_index + 1) % total_rooms  # Move to the next room in a cyclic manner

        if current_index == total_rooms - 1:
            return 'left'  # Move to the first room when at the last room
        elif next_index == current_index + 1:
            return 'right'  # Move to the next room
        else:
            return 'left'  # Default to moving left
