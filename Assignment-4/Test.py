from collections import deque

def bfs(maze, start_x, start_y, end_x, end_y):
    # return -1 if path does not exists
    # otherwise return cost the shortest path

    # Mark the start cell as visited and enqueue it
    queue = deque([(start_x, start_y, 0)])  # (x, y, cost)
    visited = {(start_x, start_y)}

    # Check if start cell is the goal cell
    if (start_x, start_y) == (end_x, end_y):
        return 0

    # Do BFS traversal starting from the start cell
    while queue:
        x, y, cost = queue.popleft()

        # Check if goal cell is reached
        if (x, y) == (end_x, end_y):
            return cost

        # Add adjacent cells to queue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy

            # Check if next cell is valid and not visited
            if (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and
                maze[next_x][next_y] == 1 and (next_x, next_y) not in visited):
                queue.append((next_x, next_y, cost+1))
                visited.add((next_x, next_y))

    # Path does not exist
    return -1

def dfs(maze, start_x, start_y, end_x, end_y):
    # return -1 if path does not exists
    # otherwise return steps with backtracking
    # Mark the start cell as visited and do DFS
    visited = {(start_x, start_y)}
    res = dfs_helper(maze, start_x, start_y, end_x, end_y, visited)

    # Check if goal cell is reached
    if res is not None:
        found, steps, path = res
        if found:
            return steps, path
    
    # Path does not exist
    return -1

def dfs_helper(maze, x, y, end_x, end_y, visited):
    # Check if goal cell is reached
    if (x, y) == (end_x, end_y):
        return (True, 0, [(x, y)])

    # Recursively search for adjacent cells
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + dx, y + dy

        # Check if next cell is valid and not visited
        if (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and
            maze[next_x][next_y] == 1 and (next_x, next_y) not in visited):
            visited.add((next_x, next_y))
            res = dfs_helper(maze, next_x, next_y, end_x, end_y, visited)
            if res is not None:
                found, steps, path = res
                if found:
                    return (True, steps+1, [(x, y)] + path)

    # Path does not exist
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
        print("Shortest cost = ", dfs_res)
    else:
        print("Path does not exit")

if __name__ == '__main__':
    main()