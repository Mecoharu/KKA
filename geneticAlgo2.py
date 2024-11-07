import random

class GridWorld:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal

    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] != '#'

    def move(self, position, direction):
        x, y = position
        if direction == 'U':
            return (x - 1, y) if self.is_valid_move((x - 1, y)) else position
        elif direction == 'D':
            return (x + 1, y) if self.is_valid_move((x + 1, y)) else position
        elif direction == 'L':
            return (x, y - 1) if self.is_valid_move((x, y - 1)) else position
        elif direction == 'R':
            return (x, y + 1) if self.is_valid_move((x, y + 1)) else position
        return position

def generate_random_route(grid_world):
    path = []
    current_position = grid_world.start
    visited = set([current_position])
    move_count = 0
    max_moves = len(grid_world.grid) * len(grid_world.grid[0])

    while current_position != grid_world.goal and move_count < max_moves:
        possible_moves = ['U', 'D', 'L', 'R']
        random.shuffle(possible_moves)
        
        move_made = False
        for move in possible_moves:
            new_position = grid_world.move(current_position, move)
            if new_position != current_position and new_position not in visited:
                path.append(move)
                current_position = new_position
                visited.add(current_position)
                move_made = True
                break
        
        if not move_made:
            new_position = grid_world.move(current_position, possible_moves[0])
            path.append(possible_moves[0])
            current_position = new_position
            visited.add(current_position)

        move_count += 1

    return path, current_position

def fitness_points_first(grid_world, path):
    current_position = grid_world.start
    collected_points = 0
    visited = set([current_position])
    
    for move in path:
        current_position = grid_world.move(current_position, move)
        if grid_world.grid[current_position[0]][current_position[1]].isdigit():
            collected_points += int(grid_world.grid[current_position[0]][current_position[1]])
            grid_world.grid[current_position[0]][current_position[1]] = '0'  # Mark point as collected
        visited.add(current_position)
        if current_position == grid_world.goal:
            break
    
    return -collected_points, len(path)  # Higher points collected is better

def fitness_direct_goal(grid_world, path):
    current_position = grid_world.start
    visited = set([current_position])
    for move in path:
        current_position = grid_world.move(current_position, move)
        if current_position == grid_world.goal:
            return len(path)  # Reward shorter paths
        visited.add(current_position)
    return len(path) + 2 * len(visited) + abs(current_position[0] - grid_world.goal[0]) + abs(current_position[1] - grid_world.goal[1])

def genetic_algorithm(grid_world, fitness_function, population_size=50, generations=500):
    population = [generate_random_route(grid_world)[0] for _ in range(population_size)]
    best_path = None

    for gen in range(generations):
        population = sorted(population, key=lambda path: fitness_function(grid_world, path))
        
        if fitness_function(grid_world, population[0]) == len(population[0]):
            best_path = population[0]
            break

        next_generation = population[:10]
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population[:20], 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate=0.2)
            next_generation.append(child)

        population = next_generation

    if best_path is None:
        best_path = population[0]

    position = grid_world.start
    fixed_path_positions = [position]
    for move in best_path:
        new_position = grid_world.move(position, move)
        if new_position != position:
            fixed_path_positions.append(new_position)
        position = new_position

    return best_path, fixed_path_positions

def crossover(parent1, parent2):
    crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

def mutate(path, mutation_rate=0.1):
    new_path = path[:]
    for i in range(len(new_path)):
        if random.random() < mutation_rate:
            new_move = random.choice(['U', 'D', 'L', 'R'])
            new_path[i] = new_move
    return new_path

def print_grid(grid_world, path):
    grid_copy = [row[:] for row in grid_world.grid]
    for pos in path:
        x, y = pos
        if grid_copy[x][y] not in ['S', 'G', '#']:
            grid_copy[x][y] = '*'
    for row in grid_copy:
        print(' '.join(str(cell) for cell in row))

# Example usage
grid = [
    ['S', '0', '0', '0', '0', '#', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0','0', '#', '0', '0'],
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

# Towards points first, then the goal
best_path_points, fixed_path_positions_points = genetic_algorithm(grid_world, fitness_points_first)
print("Best path towards points first:", best_path_points)
print("Fixed path positions (points first):")
print_grid(grid_world, fixed_path_positions_points)

# Reset grid for next run
grid_world = GridWorld(grid, start, goal)

# Directly to the goal
best_path_goal, fixed_path_positions_goal = genetic_algorithm(grid_world, fitness_direct_goal)
print("\nBest path directly to the goal:", best_path_goal)
print("Fixed path positions (direct to goal):")
print_grid(grid_world, fixed_path_positions_goal)
