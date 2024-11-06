import heapq

# A* algorithm to find the shortest path in a grid world

class GridWorld:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != '#'

    def get_neighbors(self, position):
        x, y = position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [n for n in neighbors if self.is_valid_move(n)]

    def heuristic(self, position):
        # Manhattan distance heuristic for A*
        return abs(position[0] - self.goal[0]) + abs(position[1] - self.goal[1])

def a_star(grid_world):
    start = grid_world.start
    goal = grid_world.goal

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: grid_world.heuristic(start)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path from goal to start
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in grid_world.get_neighbors(current):
            tentative_g_score = g_score[current] + 1  # Each move costs 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + grid_world.heuristic(neighbor)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def print_grid(grid_world, path):
    grid_copy = [row[:] for row in grid_world.grid]
    for pos in path:
        x, y = pos
        if grid_copy[x][y] not in ['S', 'G', '#']:
            grid_copy[x][y] = 'X'

    for row in grid_copy:
        print(' '.join(str(cell) for cell in row))

# Example usage
grid = [
    ['S', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0'],
    ['#', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '#', '0', '#', '0', '0', '0', '0', '0', '#', '0', '0', '0', '#', '0'],
    ['#', '#', '0', '0', '0', '0', '0', '#', '#', '0', '0', '0', '#', '#', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '#', '0', '#', '0', '0', '0', '0', '0', '#', '0', '#', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '#', '0', '#', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '#', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '#', '#', '0', '0', '#', '#', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0'],
    ['#', '#', '#', '0', '0', '#', '#', '0', '0', '0', '0', '0', '#', '0', '#', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '#', '0', '0', '0', '#', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '#', '0', '0', '0', '#', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '#', '0', '#', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '#', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0'],
    ['#', '#', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '#', '0', '#'],
    ['0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0'],
    ['#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '#'],
    ['#', '0', '0', '#', '#', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '#', '0'],
    ['#', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '#', '0', '0', '0', '0', '#', '#', '0', '0', '0', '0', '#', '#', '0', '0', 'G']
]

start = (0, 0)
goal = (19, 19)

grid_world = GridWorld(grid, start, goal)
path = a_star(grid_world)

if path:
    print("Path found:")
    print(path)
    print("Final grid with path:")
    print_grid(grid_world, path)
else:
    print("No path found.")
