from typing import Tuple, Callable, Optional, Set
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

movements = {
    Direction.NORTH.value : lambda i, j: (i - 1, j),
    Direction.EAST.value : lambda i, j: (i, j + 1),
    Direction.SOUTH.value : lambda i, j: (i + 1, j),
    Direction.WEST.value : lambda i, j: (i, j - 1),
}

def turn(direction: int) -> int:
    return (direction + 1) % 4


def find_patrol_route(matrix: [str], position: Tuple[int, int], direction: int, additional_obstacle: Optional[Tuple[int,int]] = None) -> Optional[set[Tuple[int, int]]]:
    """Returns set of visited positions or None if there is a cycle in the route."""
    visited_positions = set()
    visited_positions_with_direction = set()
    while True:
        visited_positions.add(position)
        if (position, direction) in visited_positions_with_direction:
            return None # cycle
        visited_positions_with_direction.add((position, direction))
        new_position = movements[direction](*position)
        (i, j) = new_position
        if i not in range(len(matrix)) or j not in range(len(matrix[i])):
            return visited_positions
        if matrix[i][j] == '#' or new_position == additional_obstacle:
            direction = turn(direction)
        else:
            position = new_position


def main():
    matrix = []
    starting_position = (0, 0)
    with open('resources/day06.txt', 'r') as file:
        for idx, line in enumerate(file):
            matrix.append(line.strip())
            if '^' in line:
                starting_position = (idx, line.index('^'))
    potential_obstacles = find_patrol_route(matrix, starting_position, Direction.NORTH.value)
    potential_obstacles.remove(starting_position)
    new_obstacles_causing_cycles = 0
    for obstacle in potential_obstacles:
        if not find_patrol_route(matrix, starting_position, Direction.NORTH.value, obstacle):
            new_obstacles_causing_cycles += 1

    print(f"The answer is {new_obstacles_causing_cycles}.")


if __name__ == '__main__':
    main()



