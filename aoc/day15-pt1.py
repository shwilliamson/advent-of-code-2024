from typing import TypeAlias, Tuple, Set, List

Coordinate: TypeAlias = Tuple[int, int]

moves = {
    "^" : lambda i, j: (i - 1, j),
    ">" : lambda i, j: (i, j + 1),
    "v" : lambda i, j: (i + 1, j),
    "<" : lambda i, j: (i, j - 1),
}

class Warehouse:
    walls: Set[Coordinate] = set()
    boxes: Set[Coordinate] = set()
    robot: Coordinate = (0, 0)
    movements: List[str] = []

    def move_box(self, m: str, pos: Coordinate) -> bool:
        next_pos = moves[m](*pos)
        if next_pos in self.walls:
            return False
        elif next_pos in self.boxes:
            if self.move_box(m, next_pos):
                self.boxes.remove(pos)
                self.boxes.add(next_pos)
                return True
        else:
            self.boxes.remove(pos)
            self.boxes.add(next_pos)
            return True

    def move_robot(self, m: str):
        next_pos = moves[m](*self.robot)
        if next_pos in self.walls:
            pass
        elif next_pos in self.boxes:
            if self.move_box(m, next_pos):
                self.robot = next_pos
        else:
            self.robot = next_pos

    def execute(self):
        for m in self.movements:
            self.move_robot(m)

    def compute_answer(self) -> int:
        result_sum = 0
        for b in self.boxes:
            result_sum += (100 * b[0]) + b[1]
        return result_sum - 100 * len(self.boxes)

    def parse(self):
        with open('resources/day15.txt', 'r') as file:
            i = 0
            for line in file:
                i += 1
                for j, c in enumerate(line.strip()):
                    if c == '@':
                        self.robot = (i, j)
                    elif c == '#':
                        self.walls.add((i, j))
                    elif c == 'O':
                        self.boxes.add((i, j))
                    elif c != '.':
                        self.movements.append(c)


if __name__ == '__main__':
    w = Warehouse()
    w.parse()
    w.execute()
    result = w.compute_answer()
    print(result)