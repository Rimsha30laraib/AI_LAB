
#com_agent
from abc import abstractmethod

class Agent(object): #Represents an agent operating in the environment.
    @abstractmethod
    def __init__(self):  #Initializes the agent.
        pass
    
    @abstractmethod
    def sense(self, environment):   #Receives information from the environment (abstract).
        pass
    @abstractmethod
    def act(self):   #Performs an action in the environment based on the sensed information (abstract).
        pass

class VaccumAgent(Agent):
    def _init_(self):
        pass

    def sense(self, env):    #Sets the environment for the agent
        self.environment = env

    def act(self):      #Performs cleaning or movement actions based on the current room's status and location.
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'
        return 'left'