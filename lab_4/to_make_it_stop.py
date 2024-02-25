from com_environment import Environment
from com_environment import Room
from com_agent import VaccumAgent

class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, num_rooms=2):
        self.rooms = [Room(chr(ord('A') + i), 'dirty') for i in range(num_rooms)]
        self.agent = agent
        self.currentRoom = self.rooms[0]
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1, max_steps=None):
        for _ in range(0, n):       #to stop
            if max_steps is not None and self.step >= max_steps:
                print(f"Stopping after {max_steps} steps.")
                return

            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.currentRoom = self.get_next_room()
            else:
                self.currentRoom = self.get_previous_room()
            self.displayAction()
            self.step += 1
    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print(f"Perception at step {self.step} is [{self.currentRoom.status}, {self.currentRoom.location}]")

    def displayAction(self):
        print(f"------- Action taken at step {self.step} is [{self.action}]")

    def delay(self, n=100):
        self.delay = n

    def get_next_room(self):
        index = (self.rooms.index(self.currentRoom) + 1) % len(self.rooms)
        return self.rooms[index]

    def get_previous_room(self):
        index = (self.rooms.index(self.currentRoom) - 1) % len(self.rooms)
        return self.rooms[index]
# Test program with a maximum of 10 steps
if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = NRoomVaccumCleanerEnvironment(vcagent, num_rooms=3)
    env.executeStep(50, max_steps=10)
