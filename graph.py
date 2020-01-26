"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy



class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.visited = set()
        self.path = []

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.

        if both exist, add a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    # Part 2
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        queue.enqueue(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
        #    Pop the first item
            vertex = queue.dequeue()
        #    If not visited
            if vertex not in visited:
        #       DO THE THING!
                print(vertex)
                visited.add(vertex)
        #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
        #           Add that edge to the queue/stack
                    queue.enqueue(next_vert)
    # Part 3
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the stack
        while stack.size() > 0:
            #    Pop the first item
            vertex = stack.pop()
            #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
                #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the stack
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Make a set to keep track of where we've been
        vertex = starting_vertex

        if vertex not in self.visited:
            # do something
            print(vertex)
            self.visited.add(vertex)
            for next_vert in self.get_neighbors(vertex):
                self.dft_recursive(next_vert)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enqueue a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
            #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
                #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)  # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue/stack as appropriate
        stack = Stack()
        # Put the starting point in that
        # Push a list to use as our path
        stack.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while stack.size() > 0:
            #    Pop the first item
            path = stack.pop()
            vertex = path[-1]
            #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
                #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)  # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    stack.push(new_path)

    def _dfs_recursive(self, starting_vertex, destination_vertex):
        vertex = starting_vertex

        if vertex is destination_vertex:
            return [vertex]
        else:
            if vertex not in self.visited:
                self.visited.add((vertex))
                for next_vert in self.get_neighbors(vertex):
                    result = self._dfs_recursive(next_vert, destination_vertex)
                    if result is not None:
                        result.insert(0, vertex)
                        return result
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Make a set to keep track of where we've been
        self.visited.clear()

        result = self._dfs_recursive(starting_vertex, destination_vertex)
        return result
        # vertex = starting_vertex
        #
        # if vertex is destination_vertex:
        #     return [vertex]
        # else:
        #     if vertex not in self.visited:
        #         self.visited.add((vertex))
        #         for next_vert in self.get_neighbors(vertex):
        #             result = self.dfs_recursive(next_vert, destination_vertex)
        #             if result is not None:
        #                 result.insert(0, vertex)
        #                 return result
        # return None

class MazeGraph(Graph):
    def add_vertex(self, vertex_id):
        if vertex_id in self.vertices.keys():
            print(f"Vertex{vertex_id} exists")
        self.vertices[vertex_id] = {}#{'n': '?', 's': '?', 'w': '?', 'e': '?'}
    def add_edge(self, v1, v2, direction):
        if v1 == 0 or v2 == 0:
            print('b')
        # assert(self.vertices[v1][direction] is '?')
        self.vertices[v1][direction] = v2
        # self.vertices[v2][direction] = v1
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack as appropriate
        stack = Stack()
        # Put the starting point in that
        stack.push(starting_vertex)
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the stack
        while stack.size() > 0:
            #    Pop the first item
            vertex = stack.pop()
            #    If not visited
            if vertex not in visited:
                #       DO THE THING!
                print(vertex)
                visited.add(vertex)
                #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    #           Add that edge to the stack
                    stack.push(next_vert)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue/stack as appropriate
        queue = Queue()
        # Put the starting point in that
        # Enqueue a list to use as our path
        queue.enqueue([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # While there is stuff in the queue/stack
        while queue.size() > 0:
            #    Pop the first item
            path = queue.dequeue()
            vertex = path[-1]
            #    If not visited
            if vertex not in visited:
                if vertex == destination_vertex:
                    # Do the thing!
                    return path
                visited.add(vertex)
                #       For each edge in the item
                for next_vert in self.get_neighbors(vertex):
                    # Copy path to avoid pass by reference bug
                    new_path = list(path)  # Make a copy of path rather than reference
                    new_path.append(next_vert)
                    queue.enqueue(new_path)



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
    print("************ bft *************")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("************ dft *************")
    graph.dft(1)
    print("************ dft_recursive *************")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("************ bfs *************")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("************ dfs *************")
    print(graph.dfs(1, 6))
    print("************ dfs_recursive *************")
    graph.visited.clear()
    print(graph.dfs_recursive(1, 6))
