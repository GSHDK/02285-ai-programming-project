from utils import _get_agt_loc, _get_box_loc
import sys
import config
"""
This module contains all the different heuristic functions for calculating the h_value in
"""


def h_replanner_pos(self: 'Heuristic', state: 'State', dist_function) -> 'int':
    # CALCULATE THE VALUES FROM LOCAL VARIABLE IN STATE coordinate_agent: str, coordinate_box: str, goal_agent: str, goal_box: str
    #  self.h_max_two(state, coordinate_agent: str, coordinate_box: str, goal_agent: str, goal_box: str)

    if 'agent_to' not in self.data and 'agent_char' not in self.data:
        raise Exception('Using wrong heuristic. **kwargs must contain agent_data')

    agent_location = _get_agt_loc(state, self.data['agent_char'])

    if 'box_to' in self.data:

        box_location = _get_box_loc(state, self.data['box_id'])
        dist_max = max(dist_function(agent_location, self.data['agent_to']),
                       dist_function(box_location, self.data['box_to']))
        if dist_max == 0:
            return 0

        if config.goal_location_evasion and (box_location in state.goal_positions.keys()) or (agent_location in state.goal_positions.keys()):
            return dist_max + config.goal_location_evasion_length
        else:
            return dist_max
    else:
        dist_max = dist_function(agent_location, self.data['agent_to'])

        if dist_max == 0:
            return 0

        if config.goal_location_evasion and (agent_location in state.goal_positions.keys()):
            return dist_max + config.goal_location_evasion_length
        else:
            return dist_max


# def h_goalassigner_box(self: 'Heuristic', state: 'State', dist_function) -> 'int':
#     # CALCULATE THE VALUES FROM LOCAL VARIABLE IN STATE coordinate_agent: str, coordinate_box: str, goal_agent: str, goal_box: str
#     #  self.h_max_two(state, coordinate_agent: str, coordinate_box: str, goal_agent: str, goal_box: str)
#
#     agent_location = _get_agt_loc(state, self.data['agent_char'])
#
#     if 'box_to' in self.data:
#         box_location = _get_box_loc(state, self.data['box_id'])
#         if config.goal_location_evasion and agent_location in state.goal_positions.keys():
#             return dist_function(box_location, self.data['box_to']) + dist_function(agent_location, box_location) - 1 + config.goal_location_evasion_length
#         else:
#             return dist_function(box_location, self.data['box_to']) + dist_function(agent_location, box_location) - 1
#     else:
#         raise Exception('Using wrong heuristic. **kwargs must contain agent_data')


def h_goalassigner_pos(self: 'Heuristic', state: 'State', dist_function) -> 'int':
    # CALCULATE THE VALUES FROM LOCAL VARIABLE IN STATE coordinate_agent: str, coordinate_box: str, goal_agent: str, goal_box: str

    if 'agent_to' not in self.data and 'agent_char' not in self.data:
        raise Exception('Using wrong heuristic. **kwargs must contain agent_data')
    agent_location = _get_agt_loc(state, self.data['agent_char'])

    # Fix for using h to determine goal
    if dist_function(agent_location, self.data['agent_to']) == 0:
        return 0

    if config.goal_location_evasion and agent_location in state.goal_positions.keys():
        return dist_function(agent_location, self.data['agent_to']) + config.goal_location_evasion_length
    else:
        return dist_function(agent_location, self.data['agent_to'])


def h_goalassigner_to_box(self: 'Heuristic', state: 'State', dist_function) -> 'int':
    # CALCULATE THE VALUES FROM LOCAL VARIABLE IN STATE coordinate_agent: str, coordinate_box: str, goal_agent: str, goal_box: str
   

    if 'box_id' not in self.data and 'agent_char' not in self.data:
        raise Exception('Using wrong heuristic. **kwargs must contain box_loc')
    agent_location = _get_agt_loc(state, self.data['agent_char'])
    box_location = _get_box_loc(state, self.data['box_id'])

    if dist_function(agent_location, box_location) == 1:
        return 1

    if config.goal_location_evasion and ((agent_location in state.goal_positions.keys()) or (box_location in state.goal_positions.keys())):
        return dist_function(agent_location, box_location)+config.goal_location_evasion_length
    else:
        return dist_function(agent_location, box_location)

def h_goalassigner_with_box(self: 'Heuristic', state: 'State', dist_functio) -> 'int':
    # CALCULATE THE VALUES FROM LOCAL VARIABLE IN STATE coordinate_agent: str, coordinate_box: str, goal_agent: str, goal_box: str

    if 'box_id' not in self.data and 'agent_char' not in self.data and 'goal_loc' not in self.data:
        raise Exception('Using wrong heuristic. **kwargs must contain box_loc')
    box_location = _get_box_loc(state, self.data['box_id'])

    if state.dijkstras_map[(self.data['goal_loc'], box_location)] == 0:
        return 0

    if (config.goal_location_evasion) and (box_location in state.goal_positions.keys()):
        return state.dijkstras_map[(self.data['goal_loc'], box_location)]+config.goal_location_evasion_length
    else:
        return state.dijkstras_map[(self.data['goal_loc'], box_location)]
