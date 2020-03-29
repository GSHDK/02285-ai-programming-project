
from state import State
from collections import deque


class ConflictManager:


    def __init__(self):

        '''
        Percept the world with current state
        '''
        self.world_state = None





def ConflictSolve(agents):

    #antage at world_state bliver opdateret i agent control loop, så vi hver gang i denne metode har det korrekte billede af miljøet. 
    

    temp_state = State(self.world_state)

    agentDict = temp_state.rever_agent_dict()

    for agent in agents:
        action = agent.plan[0]
        agent_row = self.world_state[agent.id][0][0]
        agent_col = self.world_state[agent.id][0][1]

        if action.action_type is ActionType.Move:
            ''' 
            Assume we can get agent ID
            AND agent dict is indexed on agent id
            '''
            temp_state.agents[agent.id][0][0] = agent_row + action.agent_dir.d_row
            temp_state.agents[agent.id][0][1] = agent_col + action.agent_dir.d_col

        else if action.action_type is Actiontype.Pull:
            temp_state.agents[agent.id][0][0] = agent_row + action.agent_dir.d_row
            temp_state.agents[agent.id][0][1] = agent_col + action.agent_dir.d_col
            
            if len(temp_state.boxes[f'{agent_row},{agent_col}']) > 1:



        else if action.action_type is Actiontype.Push:
            temp_state.agents[agent.id][0][0] = self.world_state[agent.id][0][0] + action.agent_dir.d_row
            temp_state.agents[agent.id][0][1] = self.world_state[agent.id][0][1] + action.agent_dir.d_col
            
            temp_state.boxes[] = 
        
    









            





    
        

    





