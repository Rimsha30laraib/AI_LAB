# main
from com_environment import Environment
from com_environment import Room
from com_agent import VaccumAgent

class TwoRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        ''' 
        Constructor 
        Initializes the environment with two rooms, an agent, and default parameters.
        '''
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B', 'dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.delay = 1000
        self.step = 1
        self.action = ""

    def executeStep(self, n=1):
        #  n: Number of steps to execute (default is 1).
        for _ in range(0, n):
            self.displayPerception()
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res
            if res == 'clean':
                self.currentRoom.status = 'clean'
            elif res == 'right':
                self.currentRoom = self.r2
            else:
                self.currentRoom = self.r1
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

    def delay(self, n=100):
        self.delay = n

# Test program
if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = TwoRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(50)
