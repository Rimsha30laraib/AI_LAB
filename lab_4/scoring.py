from com_environment import Environment
from com_environment import Room
from agent_for_n_rooms import VaccumAgent1

class NRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, num_rooms=5):
        self.rooms = [Room(chr(ord('A') + i), 'dirty') for i in range(num_rooms)]    #you create a list of rooms (self.rooms)
        self.agent = agent
        self.currentRoom = self.rooms[0]    #set the current room to the first room
        self.delay = 1000
        self.step = 1
        self.action = ""
        self.score=0

    def executeStep(self, n=1):
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':      #updates the current room based on the action
                self.score-=10
                self.currentRoom.status = 'clean'
                self.score+=25
            elif res == 'right':
                self.currentRoom = self.get_next_room()
                self.score-=1
            else:
                self.currentRoom = self.get_previous_room()
                self.score-=1
            self.displayAction()
            self.step += 1
           

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def displayPerception(self):
        print(f"Perception at step {self.step} is [{self.currentRoom.status}, {self.currentRoom.location}]")

    def displayAction(self):
        print(f"------- Action taken at step {self.step} is [{self.action}]")
        print(self.score)

    def delay(self, n=100):
        self.delay = n
 
    def get_next_room(self):    #These methods (get_next_room and get_previous_room) help in determining the next and previous rooms in a cyclic manner based on the current room's index.
        index = (self.rooms.index(self.currentRoom) + 1) % len(self.rooms)       #finds the index of the current room (self.currentRoom) in the list of rooms (self.rooms).+ 1: Increments the index by 1, effectively moving to the next room in a cyclic manner.
        return self.rooms[index]

    def get_previous_room(self):
        index = (self.rooms.index(self.currentRoom) - 1) % len(self.rooms)
        return self.rooms[index]
# Test program
if __name__ == '__main__':
    vcagent = VaccumAgent1 ()
    env = NRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(50)