"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        self.vertices[v1].add(v2)
        
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        
        return self.vertices[vertex_id]
        
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        #make a queue 
        q = Queue()
        # enqueue starting node
        q.enqueue(starting_vertex)
        #make set to track if we've visited there before
        visited = set()
        #while our queue is not empty
        while q.size() > 0:
            #dequeue whatever's at the front of our line, this is current_node
            current_node = q.dequeue()
        #if haven't visited this node yet,
            if current_node not in visited:
                #mark as visited
                visited.add(current_node)
                print(current_node)
                
                #get neighbors 
                neighbors = self.get_neighbors(current_node)
                #for each of the neighbors 
                for neighbor in neighbors:
                    #add to queue 
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        #make a stack
        s = Stack()
        #push starting node
        s.push(starting_vertex)
        #make a set to track if we've visited before
        visited = set()
        #while stack is not empty 
        while s.size() > 0:
            #pop off whatever's on top, this will be current_node 
            current_node = s.pop()
            # if not visited vertex before
            if current_node not in visited:
                #mark as visited
                visited.add(current_node)
                print(current_node)
                #get neighbors
                neighbors = self.get_neighbors(current_node)
                #for each of the nighbor
                for neighbor in neighbors:
                    # add to stack
                    s.push(neighbor)
        
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        #if start node is not in visited:
        if starting_vertex not in visited:
            #add start node to visited
            visited.add(starting_vertex)
            #print the start node
            print(starting_vertex)
            #get neighbors of the node
            neighbors = self.get_neighbors(starting_vertex)
            #loop through the neighbors
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        #use a queue and enqueue first path with starting vertex as the only item in the list
        queue = Queue()
        #track visited vertices with set
        visited = set()
        #track current path and shortest path
        queue.enqueue([starting_vertex])
        #while queue is not empty 
        while queue.size() > 0:
        #dequeue the current path
            current_path = queue.dequeue()
            #grab the last vertex from current path list
            last_vertex = current_path[-1]
            #if the last vertex is the destinaion, path has been found 
            if last_vertex == destination_vertex:
                return current_path
            # else, if last vertex is not in visited list
            if last_vertex not in visited:
                # add to visited     
                visited.add(last_vertex)
                 # get neighbors of the last vertex      
                for neighbor in self.get_neighbors(last_vertex):
                    #construct the new path by adding each neighbor to the path            
                    new_path = current_path + [neighbor]
                    #and enqueue new path
                    queue.enqueue(new_path)
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            current_path = stack.pop()
            last_vertex = current_path[-1]
            if last_vertex == destination_vertex:
                return current_path
            if last_vertex not in visited:
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = current_path + [neighbor]
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        
        #mark node as visited
        visited.add(starting_vertex)
        
        #check if it is the target node, if it is, return
        if starting_vertex == destination_vertex:
            return path
        
        if len(path) == 0:
            path.append(starting_vertex)
            #iterate over neighbors 
        neighbors = self.get_neighbors(starting_vertex)
            #check if visited
        for neighbor in neighbors:
            #if not recurse with a path
            if neighbor not in visited:
                new_path = path + [neighbor]
                result = self.dfs_recursive(
                    neighbor, destination_vertex, new_path, visited)
                if result is not None:
                        return result
                    
        
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
