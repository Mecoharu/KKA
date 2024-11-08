import heapq

# Class that represents the grid world
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
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            new_position = (x + dx, y + dy)
            if self.is_valid_move(new_position):
                neighbors.append(new_position)
        return neighbors

    def heuristic(self, position):
        x, y = position
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)

    def get_points(self, position):
        x, y = position
        return int(self.grid[x][y]) if self.grid[x][y].isdigit() else 0

# A* algorithm to find the shortest path while tracking total points along that path
def a_star_shortest_path_with_points(grid_world):
    open_set = []
    heapq.heappush(open_set, (0, grid_world.start))
    came_from = {}
    g_score = {grid_world.start: 0}
    f_score = {grid_world.start: grid_world.heuristic(grid_world.start)}
    points_collected = {grid_world.start: 0}  # Track total points collected along the path

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == grid_world.goal:
            return reconstruct_path(came_from, current), points_collected[current]  # Return the path and total points

        for neighbor in grid_world.get_neighbors(current):
            point_value = grid_world.get_points(neighbor)
            tentative_g_score = g_score[current] + 1
            tentative_points = points_collected[current] + point_value

        
        
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + grid_world.heuristic(neighbor)
                points_collected[neighbor] = tentative_points  # Track total points for the shortest path
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, 0  # No path found

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Function to print the grid with the path marke
def print_grid(grid, path):
    grid_copy = [row[:] for row in grid]
    for x, y in path:
        if grid_copy[x][y] not in ['S', 'G', '#']:
            grid_copy[x][y] = '*'
    for row in grid_copy:
        print(' '.join(row))
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

# Find the shortest path and calculate total points along this path
shortest_path_with_points, total_points = a_star_shortest_path_with_points(grid_world)
print("Shortest path (with total points collected):")
print_grid(grid, shortest_path_with_points)
print("Total points collected along the shortest path:", total_points)
