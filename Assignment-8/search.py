"""
search.py: Search algorithms on grid.
"""


def heuristic(a, b):
    """
    Calculate the heuristic distance between two points.

    For a grid with only up/down/left/right movements, a
    good heuristic is manhattan distance.
    """

    # BEGIN HERE #

    return abs(a[0]-b[0])+abs(a[1]-b[1])

    # END HERE #

def breadthFirstSearch(graph, start, goal):
    """
    Perform breadth first search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    queue=[]
    ex_list=[]
    out=[]
    queue.append([start])
    out=queue.pop(0)
    while goal not in out:
        while True:
            if out[-1] in ex_list:
                if queue==[]:
                    return came_from
                    break
                else:
                    out=queue.pop(0)
            else:
                break
        if out[-1]==goal:
            break
        for p in graph.neighboursOf(out[-1]):
            if p not in ex_list:
                l=out
                m=l+[p]
                queue.append(m)
                
        ex_list.append(out[-1])

        if queue==[]:
            return came_from
            break
        else:
            out=queue.pop(0)

    for i in range(1,len(out)):
        came_from[out[i]]=out[i-1]

    # END HERE #

    return came_from

def depthFirstSearch(graph, start, goal):
    """
    Perform depth first search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    stack=[]
    ex_list=[]
    out=[]
    stack.append([start])
    out=stack.pop()
    
    while goal not in out:
        while True:
            if out[-1] in ex_list:
                if stack==[]:
                    return came_from
                    break
                else:
                    out=stack.pop()
            else:
                break
        if out[-1]==goal:
            break
        for p in graph.neighboursOf(out[-1]):
            if p not in ex_list:
                l=out
                m=l+[p]
                stack.append(m)
        
        ex_list.append(out[-1])

        if stack==[]:
            return came_from
            break
        else:
            out=stack.pop()
    
    for i in range(1,len(out)):
        came_from[out[i]]=out[i-1]
        
    # END HERE #
    
    return came_from



def searchHillClimbing(graph, start, goal):
    """
    Perform hill climbing search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    stack=[]
    ex_list=[]
    out=[]
    stack.append([start])
    out=stack.pop()
 
    while goal not in out:
        while True:
            if out[-1] in ex_list:
                if stack==[]:
                    return came_from
                    break
                else:
                    out=stack.pop()
            else:
                break
        if out[-1]==goal:
            break
        temp=[]
        for p in graph.neighboursOf(out[-1]):
            temp.append(p)
            temp.sort(key=lambda x:heuristic(x,goal), reverse=True)
        for j in range(0,len(temp)):
            if temp[j] not in ex_list:
                l=out
                m=l+[temp[j]]
                stack.append(m)
                
        ex_list.append(out[-1])
        
        if stack==[]:
            return came_from
            break
        else:
            out=stack.pop()

    for i in range(1,len(out)):
        came_from[out[i]]=out[i-1]

    # END HERE #

    return came_from


def searchBestFirst(graph, start, goal):
    """
    Perform best first search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """


    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None


    # BEGIN HERE #
    stack=[]
    ex_list=[]
    out=[]
    stack.append([start])
    out=stack.pop()

    while goal not in out:
        while True:
            if out[-1] in ex_list:
                if stack==[]:
                    return came_from
                    break
                else:
                    out=stack.pop()
            else:
                break
        if out[-1]==goal:
            break
        for p in graph.neighboursOf(out[-1]):
            if p not in ex_list:
                l=out
                m=l+[p]
                stack.append(m)
                
        ex_list.append(out[-1])
        stack.sort(key=lambda x:heuristic(x[-1],goal), reverse=True)
    
        if stack==[]:
            return came_from
            break
        else:
            out=stack.pop()

    for i in range(1,len(out)):
        came_from[out[i]]=out[i-1]

    # END HERE #

    return came_from



def searchBeam(graph, start, goal, beam_length=3):
    """
    Perform beam search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    queue=[]
    ex_list=[]
    out=[]
    queue.append([start])
    out=queue.pop(0)

    while goal not in out:
        while True:
            if out[-1] in ex_list:
                if queue==[]:
                    return came_from
                    break
                else:
                    out=queue.pop(0)
            else:
                break
        if out[-1]==goal:
            break
        for p in graph.neighboursOf(out[-1]):
            l=out
            m=l+[p]
            queue.append(m)
                
        ex_list.append(out[-1])
        
        if queue==[]:
            return came_from
            break
        else:
            flag=1
            level=len(queue[0])
            for j in range(0,len(queue)):
                if len(queue[j])!=level:
                    flag=0
                    break
            if flag==1:
                queue.sort(key=lambda x:heuristic(x[-1],goal))
                while len(queue)>beam_length:
                    queue.pop()
            out=queue.pop(0)
        
    for i in range(1,len(out)):
        came_from[out[i]]=out[i-1]

    # END HERE #

    return came_from


def searchAStar(graph, start, goal):
    """
    Perform A* search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None

    # BEGIN HERE #
    stack=[]
    ex_list=[]
    out=[]
    stack.append([start])
    out=stack.pop()
    
    while goal not in out:
        while True:
            if out[-1] in ex_list:
                if stack==[]:
                    return came_from
                    break
                else:
                    out=stack.pop()
            else:
                break
        if out[-1]==goal:
            break
        for p in graph.neighboursOf(out[-1]):
            if p not in ex_list:
                l=out
                m=l+[p]
                stack.append(m)
                
        ex_list.append(out[-1])
        cost=[]
        for t in stack:
            g=0
            for j in range(1,len(t)):
                g=g+heuristic(t[j],t[j-1])
            cost.append(g)
    
        stack=sorted(stack, key=lambda x: cost[stack.index(x)]+heuristic(x[-1],goal), reverse=True)
        
        if stack==[]:
            return came_from
            break
        else:
            out=stack.pop()
        
    for i in range(1,len(out)):
        came_from[out[i]]=out[i-1]
    
    # END HERE #

    return came_from

