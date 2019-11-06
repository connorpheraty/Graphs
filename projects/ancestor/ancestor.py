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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


    def earliest_ancestor(self, ancestors, starting_node):


        for i in range(1,12):
            self.add_vertex(i)

        for i in ancestors:
            self.add_edge(i[0], i[1])

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_node])

        # Create a set to track visited vertices/
        visited = set()

        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # Check if it is the target
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for i in self.vertices:
                    if v in self.get_neighbors(i):
                        path_copy = list(path)
                        path_copy.append(i)
                        q.enqueue(path_copy)

        if len(path) == 1:
            return -1
        else:
            return path[-1]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for i in range(1,12):
        graph.add_vertex(i)

    for i in ancestors:
        graph.add_edge(i[0], i[1])

    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    q = Queue()
    q.enqueue([starting_node])

    # Create a set to track visited vertices/
    visited = set()

    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()
        # Grab the last vertex from the PATH
        v = path[-1]
        # If that vertex has not been visited...
        if v not in visited:
            # Check if it is the target
            visited.add(v)
            # Then add A PATH TO its neighbors to the back of the queue
            counter = 0
            for i in graph.vertices:      
                if v in graph.get_neighbors(i):
                    if counter == 0:
                        path_copy = list(path)
                        path_copy.append(i)
                        q.enqueue(path_copy)
                        counter +=1
                        print(counter)
                    else:
                        if i < path[-1]:
                            path_copy = list(path)
                            path_copy.append(i)
                            q.enqueue(path_copy)
                                             

    if len(path) == 1:
        return -1
    else:
        return path[-1]