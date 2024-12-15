import re
from dataclasses import dataclass
from typing import TypeAlias, Tuple, Set

Coordinate: TypeAlias = Tuple[int, int]


@dataclass
class Robot:
    position: Coordinate
    velocity: Coordinate


def print_map(occupied_coordinates: Set[Coordinate]) -> None:
    for y in range(103):
        line = ["*" if (x,y) in occupied_coordinates else "." for x in range(101)]
        print("".join(line))


def main():
    robots = []
    with open('resources/day14.txt', 'r') as file:
        for line in file:
            numbers = [int(n) for n in re.findall(r'-?\d+', line.strip())]
            robots.append(Robot(
                position=(numbers[0], numbers[1]),
                velocity=(numbers[2], numbers[3])
            ))

    for t in range(1, 1000000):
        occupied_coordinates: Set[Coordinate] = set()
        for robot in robots:
            (x,y) = robot.position
            (dx,dy) = robot.velocity
            new_coordinate = ((x + dx * t) % 101, (y + dy * t) % 103)
            occupied_coordinates.add(new_coordinate)

        symmetric_points: Set[Coordinate] = set()
        for (x, y) in occupied_coordinates:
            reflected_point = (100 - x, y)
            if reflected_point in occupied_coordinates:
                symmetric_points.add(reflected_point)
                symmetric_points.add((x, y))

        other_points = occupied_coordinates - symmetric_points
        symmetry_measure = len(other_points)
        if symmetry_measure < 100:
            print(f"Symmetry at time {t} is {symmetry_measure}, occupied points {len(occupied_coordinates)}")
            #print_map(occupied_coordinates)



if __name__ == '__main__':
    main()