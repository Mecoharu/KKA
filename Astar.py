import heapq
# A* algorithm to find the shortest path in a grid world with points

class GridWorld:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def is_valid_move(self, position):
        x, y = position
        # Ensure position is within bounds and not a wall ('#')
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != '#'

    def get_neighbors(self, position):
        # Possible moves: right, down, left, up
        x, y = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            new_position = (x + dx, y + dy)
            if self.is_valid_move(new_position):
                neighbors.append(new_position)
        return neighbors

    def heuristic(self, position):
        # Heuristic for A*
        x, y = position
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)

    def get_points(self, position):
        x, y = position
        # Get numeric point value if the cell contains a number, else return 0
        return int(self.grid[x][y]) if self.grid[x][y].isdigit() else 0

def a_star(grid_world, minimize_points=False):
    open_set = []
    heapq.heappush(open_set, (0, grid_world.start))
    came_from = {}
    g_score = {grid_world.start: 0}
    f_score = {grid_world.start: grid_world.heuristic(grid_world.start)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == grid_world.goal:
            return reconstruct_path(came_from, current)

        for neighbor in grid_world.get_neighbors(current):
            # Use points for cost if minimizing points, else use a constant cost of 1
            point_cost = grid_world.get_points(neighbor) if minimize_points else 1
            tentative_g_score = g_score[current] + point_cost

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + grid_world.heuristic(neighbor)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def print_grid(grid_world, path):
    grid_copy = [row[:] for row in grid_world.grid]
    for pos in path:
        x, y = pos
        if grid_copy[x][y] not in ['S', 'G', '#']:
            grid_copy[x][y] = 'X'
    for row in grid_copy:
        print(' '.join(str(cell) for cell in row))

# Grid with start (S), goal (G), walls (#), and points
grid = [
    ['S', '0', '0', '0', '0', '#', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '#', '0', '0'],
    ['#', '0', '0', '0', '#', '0', '0', '2', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '3'],
    ['0', '2', '0', '0', '0', '3', '#', '0', '#', '0', '0', '0', '0', '0', '#', '0', '0', '0', '#', '0'],
    ['#', '#', '0', '0', '0', '3', '0', '#', '#', '2', '0', '0', '5', '#', '#', '0', '2', '0', '0', '0'],
    ['0', '0', '0', '0', '5', '0', '0', '#', '0', '#', '0', '0', '2', '0', '0', '#', '0', '#', '0', '0'],
    ['0', '0', '2', '0', '0', '0', '0', '#', '0', '0', '0', '#', '0', '#', '0', '0', '0', '3', '0', '0'],
    ['0', '0', '#', '0', '2', '0', '#', '0', '0', '0', '0', '3', '0', '0', '#', '0', '0', '0', '0', '0'],
    ['0', '3', '0', '#', '#', '0', '0', '#', '#', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0'],
    ['#', '#', '#', '0', '0', '#', '#', '0', '0', '0', '0', '0', '#', '0', '#', '0', '5', '0', '0', '0'],
    ['0', '0', '0', '2', '0', '0', '0', '0', '0', '#', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '5', '0', '#', '0', '0', '0', '#', '0', '0', '#', '0', '0', '0', '0', '0', '2', '0', '0'],
    ['0', '#', '0', '0', '0', '#', '0', '2', '#', '0', '0', '0', '0', '2', '0', '2', '0', '0', '0', '0'],
    ['0', '0', '0', '#', '0', '#', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '#', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0'],
    ['#', '#', '0', '0', '0', '0', '0', '0', '#', '0', '5', '0', '0', '#', '0', '0', '0', '#', '0', '#'],
    ['0', '0', '5', '0', '0', '0', '0', '#', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0'],
    ['#', '0', '0', '0', '0', '0', '3', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '#'],
    ['#', '0', '0', '#', '#', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '2', '3', '0', '#', '0'],
    ['#', '0', '3', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '#', '0', '0', '0', '0', '#', '#', '0', '2', '0', '0', '#', '#', '0', '0', 'G']
]

start = (0, 0)
goal = (19, 19)

grid_world = GridWorld(grid, start, goal)

# Find path with the least points
least_points_path = a_star(grid_world, minimize_points=True)
print("Path with the least points:")
print_grid(grid_world, least_points_path)

# Find shortest path ignoring points
shortest_path = a_star(grid_world, minimize_points=False)
print("\nShortest path (ignoring points):")
print_grid(grid_world, shortest_path)
