from abc import abstractmethod

class Agent(object):
    @abstractmethod
    def _init_(self):
        pass

    @abstractmethod
    def sense(self, environment):
        pass

    @abstractmethod
    def act(self):
        pass

class VaccumAgent(Agent):
    def _init_(self):
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'
        elif self.environment.currentRoom.location == 'B':
            return 'right'  # Added for three rooms
        return 'left'