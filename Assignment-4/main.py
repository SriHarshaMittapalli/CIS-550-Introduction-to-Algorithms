from collections import deque

def bfs(maze, start_x, start_y, end_x, end_y):
    #return -1 if path does not exists
    # otherwise return cost the shortest path
    queue_datastructure, start_x_start_y_cost = deque(), 0; queue_datastructure.append((start_x, start_y, start_x_start_y_cost))
    visited_x_and_y = set(); visited_x_and_y.add((start_x, start_y))
    while queue_datastructure:
        pop_left_value = queue_datastructure.popleft(); value_of_x, value_of_y, value_of_cost = pop_left_value[0], pop_left_value[1], pop_left_value[2]
        if (value_of_x, value_of_y) == (end_x, end_y): return value_of_cost # We return the cost once we reach the end pair of x and y
        neighour_list_in_2d = []; neighour_list_in_2d.append((0, 1)), neighour_list_in_2d.append((0, -1)), neighour_list_in_2d.append((1, 0)), neighour_list_in_2d.append((-1, 0))
        for neighour_x, neighour_y in neighour_list_in_2d:
            next_x, next_y = value_of_x + neighour_x, value_of_y + neighour_y
            valid_and_not_visited = (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 1 and (next_x, next_y) not in visited_x_and_y)
            if valid_and_not_visited: incremental_value = 1; queue_datastructure.append((next_x, next_y, value_of_cost + incremental_value)); visited_x_and_y.add((next_x, next_y))
    return -1

def dfs(maze, start_x, start_y, end_x, end_y):
    # return -1 if path does not exists
    # otherwise return steps with backtracking
    visited_x_and_y = set(); visited_x_and_y.add((start_x, start_y)); resolution = dfs_visit(maze, start_x, start_y, end_x, end_y, visited_x_and_y)
    if resolution != None and resolution[0]: return resolution[1], resolution[2]    
    return -1

def dfs_visit(maze, value_of_x, value_of_y, end_x, end_y, visited_x_and_y):
    bool = True; start_x_start_y_cost = 0
    if (value_of_x, value_of_y) == (end_x, end_y): return (bool, start_x_start_y_cost, [(value_of_x, value_of_y)])
    neighour_list_in_2d = []; neighour_list_in_2d.append((0, 1)), neighour_list_in_2d.append((0, -1)), neighour_list_in_2d.append((1, 0)), neighour_list_in_2d.append((-1, 0))
    for neighour_x, neighour_y in neighour_list_in_2d:
        next_x, next_y = value_of_x + neighour_x, value_of_y + neighour_y; valid_and_not_visited = (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 1 and (next_x, next_y) not in visited_x_and_y)
        if valid_and_not_visited:
            visited_x_and_y.add((next_x, next_y)); resolution, incremental_value = dfs_visit(maze, next_x, next_y, end_x, end_y, visited_x_and_y), 1
            if resolution != None and resolution[0]: return (bool, resolution[1] + incremental_value, [(value_of_x, value_of_y)] + resolution[2])
    return None

def main():
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    end_x, end_y = 10, 0
    start_x, start_y = 3, 11
    bfs_res = bfs(maze, start_x, start_y, end_x, end_y)
    if bfs_res != -1:
        print("Shortest cost = ", bfs_res)
    else:
        print("Path does not exit")

    dfs_res = dfs(maze, start_x, start_y, end_x, end_y)
    if dfs_res != -1:
        print("Shortest cost = ", dfs_res[0])
        print("Back Tracking Steps = ", dfs_res[1])
    else:
        print("Path does not exit")
if __name__ == '__main__':
    main()