from abc import ABCMeta, abstractmethod
import sys
import memory
from collections import deque
from state import State


# Super class that all agent classes inharit functions form
class Agent(metaclass=ABCMeta):

    @abstractmethod
    def act(self) -> 'Action': raise NotImplementedError

'''
Agents are given a goal by a central unit and plan how to achieve this goal themselves

agent_goal_task
(Box_name, (start_location, end_location)

'''


class search_agent(Agent):

    def __init__(self, agent_char: int, agent_color: chr, agent_goal_task: str, heuristic, strategy):
        super().__init__()
        self.agent_char = agent_char
        self.agent_color = agent_color
        self.agent_goal_task = agent_goal_task

        # Conflict only interacts with this one
        self.plan = deque()

        self.heuristic = heuristic
        self.strategy = strategy

    def __repr__(self):
        return 'search agent'

    def search_box(self, world_state: 'State', box_from, box_to):

        if world_state.boxes[box_from][0] != self.agent_color:
            raise Exception("Agent cannot move this box")

        self.world_state = State(world_state)
        print('Starting search with strategy {}.'.format(self.strategy), file=sys.stderr, flush=True)
        strategy = self.strategy

        # finding our initial location
        for key, value in self.world_state.agents:
            if value[1] == self.agent_char:
                location = key

        for key, value in self.world_state.boxes:
            if key == box_from:
                box_id = value[2]

        self.world_state.sub_goal_box = box_id

        strategy.add_to_frontier(self.world_state)

        iterations = 0
        while True:
            if iterations == 1000:
                print(strategy.search_status(), file=sys.stderr, flush=True)
                iterations = 0

            if memory.get_usage() > memory.max_usage:
                print('Maximum memory usage exceeded.', file=sys.stderr, flush=True)
                return None

            if strategy.frontier_empty():
                return None

            leaf = strategy.get_and_remove_leaf()

            if leaf.is_sub_goal_state(box_to, box_id):
                self._convert_plan_to_action_list(leaf.extract_plan())

            strategy.add_to_explored(leaf)
            for child_state in leaf.get_children():  # The list of expanded states is shuffled randomly; see state.py.
                if not strategy.is_explored(child_state) and not strategy.in_frontier(child_state):
                    strategy.add_to_frontier(child_state)

            iterations += 1

    def is_goal_location(self, leaf):
        return False

    def search_location(self, world_state: State):
        return False

    def execute_action(self):
        return False
        # Return an action

    def set_search_strategy(self, heuristic, strategy):
        self.heuristic = heuristic
        self.strategy = strategy

    def _convert_plan_to_action_list(self, list_states: [State, ...]):
        for state in list_states:
            self.plan.append(state.action)


