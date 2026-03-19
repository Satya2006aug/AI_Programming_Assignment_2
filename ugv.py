import heapq
import random

GRID_SIZE = 20   # smaller grid for faster execution

# create grid with obstacles
def generate_grid(density):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < density:
                grid[i][j] = 1   # obstacle

    return grid

# Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search
def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    nodes_explored = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_explored += 1

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], nodes_explored

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if (0 <= neighbor[0] < GRID_SIZE and
                0 <= neighbor[1] < GRID_SIZE and
                grid[neighbor[0]][neighbor[1]] == 0):

                new_cost = g_score[current] + 1

                if neighbor not in g_score or new_cost < g_score[neighbor]:
                    g_score[neighbor] = new_cost
                    f = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f, neighbor))
                    came_from[neighbor] = current

    return None, nodes_explored


print("Choose obstacle density:")
print("1. Low")
print("2. Medium")
print("3. High")

choice = int(input("Enter choice (1/2/3): "))

density_map = {1: 0.1, 2: 0.2, 3: 0.3}
density = density_map.get(choice, 0.2)

grid = generate_grid(density)

start = (0, 0)
goal = (GRID_SIZE - 1, GRID_SIZE - 1)

# make sure start and goal are free
grid[start[0]][start[1]] = 0
grid[goal[0]][goal[1]] = 0

path, explored = astar(grid, start, goal)

print("\n--- RESULT ---")

if path:
    print("Path found")
    print("Path length:", len(path))
    print("Nodes explored:", explored)

    print("\nPath:")
    print(path)
else:
    print("No path found")
    print("Nodes explored:", explored)
