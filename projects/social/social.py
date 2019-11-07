import random

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

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        
        # Add users
        for i in range(1, numUsers+1):
            self.addUser(i)
        
        pair_lst = pair_sets(numUsers, avgFriendships)
        
        # Add Friendships
        for i in pair_lst:
            self.addFriendship(i[0],i[1])
            
            
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Do a BFT, store the paths as we go
        # Create an empty queue
        q = Queue()

        q.enqueue([userID])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH from the queue
            path = q.dequeue()
            v = path[-1]
            # Check if it's been visited
            if v not in visited:
                # If not mark it as visited
                visited[v] = path
                # Add a path to each neighbor to the back of the queue
                for friendID in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friendID)
                    q.enqueue(path_copy)
        # Return visited dictionary
        return visited

def pair_sets(num_users, num_friends):
    
    total_connecs = num_friends * num_users // 2
    
    connecs = set()
    
    while len(connecs) < total_connecs:
        x = random.randint(1, num_users)
        y = random.randint(1, num_users) 
        
        if x != y:
            pair = (x,y)
            opp_pair = (y,x)
            if opp_pair not in connecs:
                connecs.add((x,y))
            
            
    return connecs

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
