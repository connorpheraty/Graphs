"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        
        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            vert = q.dequeue()
            # If that vertex has not been visited
            if vert not in visited:
                visited.add(vert)
                print(vert)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vert]:
                    q.enqueue(neighbor)
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        
        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first vertex
            vert = s.pop()
            # If that vertex has not been visited
            if vert not in visited:
                visited.add(vert)
                print(vert)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[vert]:
                    s.push(neighbor)
        

        
    def dft_recursive(self, starting_vertex, stack=None, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if not stack:
            stack = Stack()
            stack.push(starting_vertex)
            
        if not visited:
            visited = set()
        
        if stack.size() == 0:
            return
        
        else:
            vert = stack.pop()
            
            if vert not in visited:
                visited.add(vert)
                print(vert)
        
                for neighbor in self.vertices[vert]:
                    stack.push(neighbor)
            
            return self.dft_recursive(starting_vertex, stack=stack, visited=visited)
            
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        
        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty...
        while destination_vertex not in visited:
            # Dequeue the first vertex
            path = q.dequeue()
            # If that vertex has not been visited
            v = path[-1]
            if v not in visited:
                if v == destination_vertex:
                    return path
                visited.add(v)
            for neighbor in self.get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

        return None
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        # Create a stack
        s = Stack()
        s.push(starting_vertex)
        
        # Store visited vertices
        visited = set()
        
        while destination_vertex not in visited:
            # Dequeue the first vertex
            path = s.pop()
            v = path[-1]
            # If that vertex has not been visited
            while destination_vertex not in visited:
                # Dequeue the first vertex
                path = s.pop()
                # If that vertex has not been visited
                v = path[-1]
                if v not in visited:
                    if v == destination_vertex:
                        return path
                    visited.add(v)
                for neighbor in self.get_neighbors(v):
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    s.push(path_copy)

            return None





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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
