from dataclasses import dataclass, field
import time
from typing import TypeAlias, Tuple, Set, List, Optional
from enum import Enum

Coordinate: TypeAlias = Tuple[int, int]


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


moves = {
    Direction.NORTH: lambda i, j: (i - 1, j),
    Direction.EAST: lambda i, j: (i, j + 1),
    Direction.SOUTH: lambda i, j: (i + 1, j),
    Direction.WEST: lambda i, j: (i, j - 1),
}


@dataclass(frozen=True)
class Node:
    position: Coordinate = (0, 0)
    dir: Direction = Direction.EAST
    score: int = 0
    parent: Optional['Node'] = None

    def has_cycle(self) -> bool:
        parent = self.parent
        while parent is not None:
            if parent.position == self.position and parent.dir == self.dir:
                return True
            parent = parent.parent
        return False

    def children(self) -> ['Node']:
        left_dir = Direction((self.dir.value - 1) % len(Direction))
        right_dir = Direction((self.dir.value + 1) % len(Direction))
        return [
            Node(
                position=moves[self.dir](*self.position),
                dir=self.dir,
                score=(self.score + 1),
                parent=self
            ),
            Node(
                position=moves[left_dir](*self.position),
                dir=left_dir,
                score=(self.score + 1001),
                parent=self
            ),
            Node(
                position=moves[right_dir](*self.position),
                dir=right_dir,
                score=(self.score + 1001),
                parent=self
            )
        ]


class Maze:
    walls: Set[Coordinate] = set()
    goal: Coordinate = (0, 0)
    min_score: int = 99999999999999999999999
    to_visit: List[Node] = []

    def walk_all_paths(self) -> int:
        while len(self.to_visit) > 0:
            node = self.to_visit.pop()
            for child in node.children():
                if child.position == self.goal:
                    self.min_score = min(self.min_score, child.score)
                elif child.score > self.min_score:
                    pass
                elif child.position in self.walls:
                    pass
                elif child.has_cycle():
                    pass
                else:
                    self.to_visit.append(child)
        return self.min_score

    def parse(self):
        with open('resources/day16.txt', 'r') as file:
            lines = [line.strip() for line in file]
            for i, line in enumerate(lines):
                for j, c in enumerate(line):
                    if c == 'S':
                        self.to_visit.append(Node(position=(i, j)))
                    elif c == '#':
                        self.walls.add((i, j))
                    elif c == 'E':
                        self.goal = (i, j)


if __name__ == '__main__':
    m = Maze()
    m.parse()
    score = m.walk_all_paths()
    print(f"Answer is {score}")
