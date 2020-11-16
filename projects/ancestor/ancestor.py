class Queue():
    def __init__(self):
        self.queue = []
        
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: 
            return None
    
    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    graph = {}
    queue = Queue()
    visited = set()
    longest_path_len = 1
    earliest_ancestor = -1
    #loop through ancestors list
    #create graph dictionary child parents
    for pairs in ancestors:
        graph[pairs[1]] = set()
    for pairs in ancestors:
        graph[pairs[1]].add(pairs[0])
    print(f"starting node: ", starting_node)  
    
    #if the starting node is not key of graph(not parent) return -1
    if starting_node not in graph:
        return -1
    
    queue.enqueue([starting_node])
    
    #while queue is not empty
    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]
        
        # if it's not in visited, mark as visited 
        if current_node not in visited:
            visited.add(current_node)
            # get the neighbors
            neighbors = graph.get(current_node)
            # loop through neighbors  
            if neighbors is not None:
                for neighbor in neighbors:
            # construct new path by adding each neighbor to end if neighbor not none 
                    new_path = current_path + [neighbor]
                    queue.enqueue(new_path)
            else:
                 # check if length of current path is bigger than longest path 
                if len(current_path) > longest_path_len or (len(current_path) == longest_path_len and current_node < earliest_ancestor):
                    longest_path_len = len(current_path)
                    # assign current node to earliest ancestor             
                    earliest_ancestor = current_node
    print(f"earliest ancestors are: ", earliest_ancestor)
    return earliest_ancestor