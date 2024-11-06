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
    move_count = 0
    max_moves = len(grid_world.grid) * len(grid_world.grid[0])  # Avoid infinite loops

    while current_position != grid_world.goal and move_count < max_moves:
        possible_moves = ['U', 'D', 'L', 'R']
        random.shuffle(possible_moves)
        for move in possible_moves:
            new_position = grid_world.move(current_position, move)
            if new_position != current_position:
                path.append(move)
                current_position = new_position
                break
        move_count += 1

    return path, current_position

def fitness(grid_world, path):
    current_position = grid_world.start
    for move in path:
        current_position = grid_world.move(current_position, move)
        if current_position == grid_world.goal:
            return len(path)  # Reward shorter paths
    # Penalize based on Manhattan distance to goal and length of the path
    return len(path) + abs(current_position[0] - grid_world.goal[0]) + abs(current_position[1] - grid_world.goal[1])

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

def genetic_algorithm(grid_world, population_size=50, generations=500):
    population = [generate_random_route(grid_world)[0] for _ in range(population_size)]
    best_path = None

    for gen in range(generations):
        population = sorted(population, key=lambda path: fitness(grid_world, path))
        
        if fitness(grid_world, population[0]) == len(population[0]):
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
    visited_positions = [position]
    for move in best_path:
        position = grid_world.move(position, move)
        visited_positions.append(position)

    return best_path, visited_positions

def print_grid(grid_world, visited_positions):
    grid_copy = [row[:] for row in grid_world.grid]
    for pos in visited_positions:
        x, y = pos
        if grid_copy[x][y] not in ['S', 'G', '#']:  
            grid_copy[x][y] = 'X'

    for row in grid_copy:
        print(' '.join(str(cell) for cell in row))

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
best_path, visited_positions = genetic_algorithm(grid_world)

print("Best path in moves:", best_path)
print("Visited positions:", visited_positions)
print("Final grid with visited positions:")
print_grid(grid_world, visited_positions)
