# KKA Final Practicum

| Name           | NRP       |
| ---            | ---        |
| Kinar Naila Fauziah | 5025231001| 
| Safa Nadhira Azzahra | 5025231086 |
| Azkiya Rusyda Zahra  | 5025231072 |

A. Introduction 
Pathfinding is a crucial aspect of robotics and artificial intelligence, where the goal is to determine the most efficient route for a robot to reach a specified destination. This process involves navigating through complex environments, often filled with obstacles, to identify the shortest or most practical path based on specific criteria. Pathfinding algorithms are essential in a wide range of applications, such as guiding video game characters, programming robotic vacuum cleaners to maneuver around furniture, and enabling driverless cars to navigate safely through traffic. By leveraging algorithms like A* and genetic algorithms, robots and AI systems can not only avoid obstacles but also optimize their movements based on factors such as time, energy, and safety. These algorithms enable intelligent decision making, allowing robots to adapt dynamically to changes in their surroundings and improve their usefulness and efficiency in real-world scenarios, from autonomous delivery to disaster response. The development of sophisticated pathfinding techniques continues to drive advancements in robotics and AI, making autonomous systems increasingly capable of performing complex tasks with minimal human intervention.

B. Background & Problem Statement
Robots often operate in a simplified two-dimensional space known as a “grid world,” which consists of a grid of cells, each of which may represent either open space or an obstacle. This structure allows for systematic navigation but presents a challenge when it comes to determining the most efficient route from one location to another while avoiding obstacles and minimizing travel distance. The complexity increases when considering dynamic environments where obstacles or conditions may change, requiring the pathfinding algorithm to adapt on the fly. The goal of our project is to design an efficient pathfinding algorithm that can not only identify the optimal route through this grid world but can also perform well under dynamic conditions, finding the best path quickly and accurately. This approach will enable robots to navigate more effectively in real-world applications, enhancing their ability to make intelligent decisions about movement in complex, changing environments. By achieving this, we aim to create a pathfinding solution that balances speed, accuracy, and adaptability, crucial traits for effective navigation in various robotics applications.

C. Algorithm
- A* Algorithm : A* combines the strengths of  Best-First Search (BFS) with heuristic data, it computes the cost of traveling to a node using heuristics like euclidean distance, and estimates cost of traveling from the node to the destination.

A* algorithm is a powerful pathfinding and graph traversal algorithm that combines the strengths of Best-First Search (BFS) with heuristic data to efficiently find the optimal path from a start node to a goal node. A* computes the cost of traveling to a given node, known as the "g-score," which represents the actual cost of the path taken so far. It then adds a heuristic estimate of the cost to reach the goal from that node, known as the "h-score." This heuristic is typically calculated using methods like Euclidean distance or Manhattan distance, which provide an approximate "straight-line" or grid-based distance to the goal. By combining these two costs (g + h), A* is able to balance actual path length with the predicted distance remaining, allowing it to prioritize nodes that are likely to lead to the shortest overall path.

A* can be particularly effective in navigating the grid world environment where a robot needs to find the most efficient route to a specified destination while avoiding obstacles. The algorithm’s ability to estimate the remaining cost makes it both efficient and accurate in complex environments, as it doesn’t waste time exploring nodes that are unlikely to lead to the goal. In dynamic environments, where obstacles may appear or disappear, A* can quickly adapt by recalculating the optimal path based on updated grid data. This feature makes A* well-suited for robotics applications, where real-time decision-making and adaptability are essential.

- Genetic Algorithm : Genetic algorithms offer a unique approach to pathfinding by leveraging evolutionary principles rather than systematically exploring the search space, as is done in traditional algorithms like BFS and A*. Instead of sequentially evaluating nodes, a genetic algorithm generates an initial population of random possible paths, then iteratively selects, crosses over, and mutates these paths to produce new generations of potential solutions. By applying selection pressure—favoring paths that perform better based on criteria such as shorter distance or fewer obstacles—genetic algorithms refine the population over time, gradually evolving paths that are increasingly efficient.

This evolutionary approach is particularly advantageous in situations where the search space is vast or highly complex, making systematic exploration slow or computationally expensive. In these cases, genetic algorithms can efficiently approximate an optimal solution by exploring a diverse set of paths and refining them through generations. Although they may not guarantee an absolute optimal solution, genetic algorithms often converge to a near-optimal path quickly. By balancing exploration with targeted refinement, genetic algorithms provide an effective, adaptable solution for complex pathfinding problems, especially where other algorithms might struggle with time constraints or large, intricate search spaces.

D. Data 
In this project, a grid-based environment serves as the testing ground for implementing the A* algorithm and a genetic algorithm to solve an enhanced pathfinding problem. The grid consists of traversable and non-traversable cells, with a designated starting point, marked by a green circle in the top-left corner, and a goal, represented by a red square in the bottom-right corner. Black cells in the grid signify obstacles that block direct movement, forcing the pathfinding algorithm to navigate around them. The A* algorithm, known for finding the shortest path by balancing the cost of reaching each cell with an estimated distance to the goal, successfully identifies an optimal path, shown in blue, connecting the start and goal.

Beyond simply finding the shortest path, the grid environment includes collectible points scattered along the paths, which add another layer of complexity to the problem. In this enhanced scenario, the objective is not only to reach the goal efficiently but also to maximize the collection of points along the way, aiming to find the path with the highest point total. The genetic algorithm is especially useful in this context, as it generates and evolves multiple potential paths, selecting the best ones based on fitness criteria that now include both path length and points collected. This hybrid approach demonstrates the adaptability of combining A* and genetic algorithms to balance path efficiency with point maximization, showcasing their suitability for real-world applications where navigation may involve both obstacle avoidance and the collection of valuable items, such as in robotics, search-and-rescue operations, or game design. The grid example visually illustrates how these algorithms can achieve optimal paths that are not only efficient but also reward-maximizing, adding depth to traditional pathfinding scenarios. 

This is the grid when it has points to be searched, with ‘S’ is the starting point, ‘G’ is the goal point, ‘0’ as the path, and ‘#’ as the obstacles:

['S', '0', '0', '0', '0', '#', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '#', '0', '0']
['#', '0', '0', '0', '#', '0', '0', '2', '0', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '3']
['0', '2', '0', '0', '0', '3', '#', '0', '#', '0', '0', '0', '0', '0', '#', '0', '0', '0', '#', '0']
['#', '#', '0', '0', '0', '3', '0', '#', '#', '2', '0', '0', '5', '#', '#', '0', '2', '0', '0', '0']
['0', '0', '0', '0', '5', '0', '0', '#', '0', '#', '0', '0', '2', '0', '0', '#', '0', '#', '0', '0']
['0', '0', '2', '0', '0', '0', '0', '#', '0', '0', '0', '#', '0', '#', '0', '0', '0', '3', '0', '0']
['0', '0', '#', '0', '2', '0', '#', '0', '0', '0', '0', '3', '0', '0', '#', '0', '0', '0', '0', '0']
['0', '3', '0', '#', '#', '0', '0', '#', '#', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0']
['#', '#', '#', '0', '0', '#', '#', '0', '0', '0', '0', '0', '#', '0', '#', '0', '5', '0', '0', '0']
['0', '0', '0', '2', '0', '0', '0', '0', '0', '#', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['0', '0', '5', '0', '#', '0', '0', '0', '#', '0', '0', '#', '0', '0', '0', '0', '0', '2', '0', '0']
['0', '#', '0', '0', '0', '#', '0', '2', '#', '0', '0', '0', '0', '2', '0', '2', '0', '0', '0', '0']
['0', '0', '0', '#', '0', '#', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
['0', '#', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '0']
['#', '#', '0', '0', '0', '0', '0', '0', '#', '0', '5', '0', '0', '#', '0', '0', '0', '#', '0', '#']
['0', '0', '5', '0', '0', '0', '0', '#', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0']
['#', '0', '0', '0', '0', '0', '3', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '0', '0', '#']
['#', '0', '0', '#', '#', '0', '0', '0', '0', '0', '0', '0', '0', '#', '0', '2', '3', '0', '#', '0']
['#', '0', '3', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0', '#', '0', '0', '0', '0', '0']
['0', '0', '0', '0', '#', '0', '0', '0', '0', '#', '#', '0', '2', '0', '0', '#', '#', '0', '0', 'G']



