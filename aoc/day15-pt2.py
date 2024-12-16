from dataclasses import dataclass
from typing import TypeAlias, Tuple, Set, List

Coordinate: TypeAlias = Tuple[int, int]


moves = {
    "^" : lambda i, j: (i - 1, j),
    ">" : lambda i, j: (i, j + 1),
    "v" : lambda i, j: (i + 1, j),
    "<" : lambda i, j: (i, j - 1),
}


@dataclass(frozen=True)
class Box:
    left: Coordinate
    right: Coordinate

    def shifted_left(self) -> 'Box':
        return Box(moves['<'](*self.left), moves['<'](*self.right))

    def shifted_right(self) -> 'Box':
        return Box(moves['>'](*self.left), moves['>'](*self.right))


class Warehouse:
    walls: Set[Coordinate] = set()
    boxes: Set[Box] = set()
    robot: Coordinate = (0, 0)
    movements: List[str] = []

    def move_box(self, m: str, box: Box, dry_run: bool = False) -> bool:
        new_box = Box(moves[m](*box.left), moves[m](*box.right))
        if new_box.left in self.walls or new_box.right in self.walls:
            return False

        possible_obstructions = {
            new_box.shifted_left(),
            new_box,
            new_box.shifted_right()
        }
        obstructions = []
        for po in possible_obstructions:
            if po != box and po in self.boxes:
                obstructions.append(po)

        if len(obstructions) > 0:
            can_move_all_obstacles = all([self.move_box(m, b, dry_run=True) for b in obstructions])
            if can_move_all_obstacles:
                for obstacle in obstructions:
                    self.move_box(m, obstacle)
                if not dry_run:
                    self.boxes.remove(box)
                    self.boxes.add(new_box)
                return True
            else:
                return False
        else:
            if not dry_run:
                self.boxes.remove(box)
                self.boxes.add(new_box)
            return True

    def move_robot(self, m: str):
        next_pos = moves[m](*self.robot)
        if next_pos in self.walls:
            return
        box1 = Box(moves['<'](*next_pos), next_pos)
        box2 = Box(next_pos, moves['>'](*next_pos))
        if box1 in self.boxes:
            if self.move_box(m, box1):
                self.robot = next_pos
        elif box2 in self.boxes:
            if self.move_box(m, box2):
                self.robot = next_pos
        else:
            self.robot = next_pos

    def print_map(self):
        for i in range(50):
            line = ""
            for j in range(100):
                c = ""
                if (i, j) in self.walls:
                    c = "#"
                    line += c
                if Box((i,j), (i,j+1)) in self.boxes:
                    c = "["
                    line += c
                if Box((i,j-1), (i,j)) in self.boxes:
                    c = "]"
                    line += c
                if self.robot == (i,j):
                    c = "@"
                    line += c
                if len(c) == 0:
                    line += "."
            print(line)
        print()

    def execute(self):
        for i, m in enumerate(self.movements):
            self.move_robot(m)

    def compute_answer(self) -> int:
        result_sum = 0
        for b in self.boxes:
            result_sum += (100 * b.left[0]) + b.left[1]
        return result_sum

    @staticmethod
    def transform_input(input_str: str) -> str:
        return (input_str
                .replace(".", "..")
                .replace("O", "[]")
                .replace("#", "##")
                .replace("@", "@.")
                )

    def parse(self):
        with open('resources/day15.txt', 'r') as file:
            lines = [self.transform_input(line.strip()) for line in file]
            for i, line in enumerate(lines):
                for j, c in enumerate(line):
                    if c == '@':
                        self.robot = (i, j)
                    elif c == '#':
                        self.walls.add((i, j))
                    elif c == '[':
                        self.boxes.add(Box((i, j), (i, j + 1)))
                    elif c == ']' or c == '.':
                        pass
                    else:
                        self.movements.append(c)


if __name__ == '__main__':
    w = Warehouse()
    w.parse()
    w.execute()
    w.print_map()
    print(f"Answer is {w.compute_answer()}")