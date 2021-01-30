import random
import math

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
        self.last_id = 0
        self.users = {} # {1: User("1"), 2: User("2"), ...}
        self.friendships = {} #{1: {2,3,4}, 2: {1}, 3: {1}, 4: {1}}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name) 
        self.friendships[self.last_id] = set() # {1: {}}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")


        # Create friendships
        # Generate all the possible friendships and put them into an array
        # 3 users (0, 1, 2)
        possible_friendship = []
        for user_id in self.users:
                #to prevent duplicate friendship create from user_id + 1
            for friend_id in range(user_id +1, self.last_id + 1):
                possible_friendship.append((user_id, friend_id))
        # [(0, 1), (0, 2), (1, 2)]
        # Shuffle the friendship array
        # [(1, 2), (0, 1), (0 2)]
        random.shuffle(possible_friendship)
        # Take the first num_users * avg_friendships / 2 and that will be the friendship for that graph 
        for i in range(math.floor(num_users * avg_friendships / 2)):
                       friendship = possible_friendship[i]
                       self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        #manually add first user to the queue 
        q.enqueue(user_id)
        # the path from the user_id to user_id is itself. add it as starting path
        visited[user_id] = [user_id]
        
        #as long as there is a friend in the queue to discover:
        while q.size() > 0:
            #dequeue the use from queue 
            user = q.dequeue()
            # now we get the user's friends
            friends = self.friendships[user]
            
            #check every friend of the user
            for f in friends: 
                #if that friend is not visited yet 
                if f not in visited:
                    # add that friend to Queue 
                    q.enqueue(f)
                    # save the path for the friend. combine user;s path with frien's ID
                    visited[f] = visited[user] + [f]
        return visited
    
    
        # #mari batilando solution
        # visited = {} # a dictionary mapping from node id --> [path from user_Id]
        # queue = deque() # we need this for a bft
        # queue.append([user_id])
        # while len(queue) > 0:
        #     currPath = queue.popleft()
        #     currNode = currPath[-1]
        #     visited[currNode] = currPath # bft guarantees us that this is the shortest path to currNode from user_id
        #     for friend in self.friendships[currNode]:
        #         if friend not in visited:
        #             newPath = currPath.copy()
        #             newPath.append(friend)
        #             queue.append(newPath)
        # return visited 


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
