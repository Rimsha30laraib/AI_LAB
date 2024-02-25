'''A reflex-based agent typically makes decisions based on the current percept without maintaining an internal model of the environment. If the sensors are taken away from the agent, it won't be able to perceive anything directly. However, the reflex-based agent might still work to some extent if it can rely on its internal model or knowledge of the environment.

In the provided vacuum cleaner agent code, the VaccumAgent is reflex-based. It checks the current room's status and location and decides the action based on these factors. Let's consider the agent's behavior in the absence of sensors:'''

from com_agent import Agent
class VaccumAgent(Agent):
    def __init__(self):
        pass

    def sense(self, env):
        # No explicit sensing in this reflex-based agent
        pass

    def act(self):
        # Reflex action based on the currentRoom properties
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'
        return 'left'
