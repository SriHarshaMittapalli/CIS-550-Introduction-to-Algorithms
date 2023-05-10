
def bfs(maze, start_x, start_y, end_x, end_y):
    #return -1 if path does not exists
    # otherwise return cost the shortest path

def dfs(maze, start_x, start_y, end_x, end_y):
    # return -1 if path does not exists
    # otherwise return steps with backtracking


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
        print("Shortest cost = ", dfs_res)
    else:
        print("Path does not exit")
if __name__ == '__main__':
    main()