#com_environment
class Room:
    def __init__(self, location, status="dirty"):
        self.location = location
        self.status = status

from abc import abstractmethod

class Environment(object):
    @abstractmethod
    def __init__(self, n):
        self.n = n

    def executeStep(self, n=1):
        raise NotImplementedError('action must be defined!')

    def executeAll(self):
        raise NotImplementedError('action must be defined!')

    def delay(self, n=100):
        self.delay = n
