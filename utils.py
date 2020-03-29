

def cityblock_distance(pos1, pos2):
    '''
    :param pos1: Is a tuple of x,y coordinates
    :param pos2: Is a tuple of x,y coordinates
    :return: the cityblock distance (manhatten distance)
    '''
    return abs(pos2[0] - pos1[0])+abs(pos2[1] - pos1[1])

