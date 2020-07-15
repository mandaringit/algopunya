from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self, name, skills, load):
        self.name: str = name
        self.skills: List[str] = skills
        self.load: int = load

    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id: str = id
        self.restrictions: List[str] = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        result = None
        min_loaded = 999
        for agent in agents:
            if agent.load < min_loaded:
                result = agent
                min_loaded = agent.load

        if result:
            return result

        raise NoAgentFoundException()


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        result = None
        for agent in agents:
            common = set(ticket.restrictions) & set(agent.skills)
            if common:
                if not result:
                    result = agent
                elif len(agent.skills) <= len(result.skills):
                    result = agent

        if result:
            return result

        raise NoAgentFoundException()


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_flexible_policy = LeastFlexibleAgent()
print(least_flexible_policy.find(ticket, [agent1, agent2]))
