from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from graph import MazeGraph
from util import Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# traversal_path = ['n', 'n']
traversal_path = []

room_path = []

opposite_move_map = { 'n' : 's', 'e' : 'w', 's' : 'n', 'w' : 'e'}


def get_direction(graph, room_id, visited):
    unexplored_exits = []
    for direction in graph.vertices[room_id]:
        if graph.vertices[room_id][direction] is "?":
            return direction
    #         unexplored_exits.append(direction)
    #
    # print(f"Room{room_id} Unexplored Exits{unexplored_exits}")
    # room = world.rooms[room_id]
    # for exit in unexplored_exits:
    #     if room.get_room_in_direction(exit) not in visited:
    #         return exit

    return None


import time
# Fill this out with directions to walk
def traverse(starting_room_id = 0, steps = 3000):

    # traversal_path.append(starting_room_id)

    visited = set()
    stack = Stack()
    # stack.push(0)
    room_stack = Stack()
    graph = MazeGraph()

    vertex = starting_room_id
    # graph.add_vertex(vertex)
# depth first search to find the dead end
# backtrack to find


    while steps > 0:

        # if steps % 5 == 0:
        # time.sleep(2)
        # generate graph
        room_id = player.current_room.id

        # if (vertex)
        # visited.add(vertex)
        visited.add(room_id)
        # stack.push(move_to)

        # room_stack.push(room_id)

        if room_id == 0:
            print("0")

        # check if the vertex has been initialized
        if room_id not in graph.vertices:
            graph.add_vertex(room_id)
            # find available direction
            exits = player.current_room.get_exits()
            # add to adjacent map
            for ex in exits:
                graph.vertices[room_id][ex] = '?'



        # if len(exits) == 0:
        #     # backtrack
        #     last_move = stack.pop()
        #     # move in opposite direction
        if room_id == 0:
            print('b')
        # check graph
        unexplored_exits = []
        # check if the vertex has visited

        for direction in graph.vertices[room_id]:
            if graph.vertices[room_id][direction] is "?":
                unexplored_exits.append(direction)

        print(f"Room{room_id} Unexplored Exits{unexplored_exits}")
        if len(unexplored_exits) > 0:
            # move_to = random.choice(unexplored_exits)
            move_to = unexplored_exits[0]
        else:
        # move_to = get_direction(graph, room_id, visited)
        # if not move_to:
            # visited.add(room_id)

            # check for cycle
            # temp_room_stack = list(room_stack.stack)
            if room_id in room_stack.stack[:-1]:
                temp_track = []
                track_count = 0

                while room_stack.size() > 0:

                    rid = room_stack.pop()
                    # keep track of the rooms to reconstruct and count for quick delete
                    temp_track.append(rid)
                    # skip itself
                    if track_count == 0:
                        track_count+=1
                        continue

                    # found it, delete the stacks so no need to backtrack the whole way
                    if rid == room_id:
                        while track_count > 1:
                            stack.pop()
                            track_count -= 1
                        break


                    if '?' in graph.vertices[rid].values():
                        # reconstruct the stack if there are still unexplored room in between
                        for i in range(len(temp_track) - 1, -1, -1):
                            room_stack.push(temp_track[i])
                        break
                    track_count += 1




            # # check if it's on the stack
            # for i in range(len(room_stack.stack) -2, -1, -1):
            #     rid = room_stack.stack[i]
            #     if '?' not in graph.vertices[rid].values() and rid == room_id:
            #         # cycle detected, chop stack
            #         stack.stack = stack.stack[:len(stack.stack) - i]
            #         room_stack = room_stack.stack[:len(room_stack.stack) - i]

            else:
                room_stack.pop()

            move_to = opposite_move_map[stack.pop()]
            # room_stack.pop()
            player.travel(move_to, True)
            traversal_path.append(move_to)
            room_path.append((player.current_room.id))
            # print(traversal_path)
            steps -= 1
            continue

        print(move_to)


        player.travel(move_to, True)


        room_id_move_to = player.current_room.id

        room_path.append(room_id_move_to)


        if room_id_move_to not in graph.vertices:
            graph.add_vertex(room_id_move_to)
            exits = player.current_room.get_exits()
            # add to adjacent map
            for ex in exits:
                graph.vertices[room_id_move_to][ex] = '?'

        graph.add_edge(room_id, room_id_move_to, move_to)
        graph.add_edge(room_id_move_to, room_id, opposite_move_map[move_to])
        # visited.add(room_id_move_to)
        traversal_path.append(move_to)
        print(traversal_path)
        # store the move
        stack.push(move_to)

        room_stack.push(room_id_move_to)
        steps -= 1

        if len(graph.vertices) == len(world.rooms):
            for ver in range(len(world.rooms)):
                for neighbor in graph.vertices[ver].values():
                    if neighbor is "?":
                        print("")

            print(F"Maze Traversal Complete. Took {len(traversal_path)} Steps")
            break







# test moving one step
traverse(0, 5000)




print(room_path)
from collections import Counter
c= Counter(room_path)
print(c.keys())
print(c.values())

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
