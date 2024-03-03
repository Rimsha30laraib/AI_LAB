from com_environment import Environment
from com_environment import Room
from agent_for_three_rooms import VaccumAgent

class ThreeRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        '''
        Constructor
        Initializes the environment with three rooms, an agent, and default parameters.
        '''
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.r3 = Room('C', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        #n: Number of steps to execute (default is 1).
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.move_right()
            elif res == 'left':
                self.move_left()
            self.displayAction()
            self.step += 1

    def executeAll(self):
        raise NotImplementedError('executeAll method must be defined!')

    def displayPerception(self):
        #Display the current perception of the environment.
        print("Perception at step %d is [%s, %s]" % (self.step, self.currentRoom.status, self.currentRoom.location))

    def displayAction(self):
        #Display the action taken by the agent at the current step.
        print("------- Action taken at step %d is [%s]" % (self.step, self.action))

    def move_right(self):
        #Move the agent to the room on the right based on the current room.
        if self.currentRoom == self.r1:
            self.currentRoom = self.r2
        elif self.currentRoom == self.r2:
            self.currentRoom = self.r3

    def move_left(self):
        #Move the agent to the room on the left based on the current room.
        if self.currentRoom == self.r3:
            self.currentRoom = self.r2
        elif self.currentRoom == self.r2:
            self.currentRoom = self.r1

# Test program
if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = ThreeRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(50)
