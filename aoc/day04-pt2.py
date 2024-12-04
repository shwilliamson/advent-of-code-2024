from typing import Callable, Tuple, Optional

MATCHES = ['MAS', 'SAM']

movements = {
    'NE': lambda i, j: (i + 1, j + 1),
    'SE': lambda i, j: (i - 1, j + 1),
    'NW': lambda i, j: (i + 1, j - 1),
    'SW': lambda i, j: (i - 1, j - 1),
}

def get_symbol(move: Callable[[int, int], Tuple[int, int]], matrix: [str], i: int, j: int) -> Optional[str]:
    ii, jj = move(i, j)
    if ii not in range(len(matrix)):
        return None
    if jj not in range(len(matrix[ii])):
        return None
    return matrix[ii][jj]


def x_mas_count(matrix: [str], i: int, j: int,) -> int:
    if matrix[i][j] != 'A':
        return 0
    symbols = {key : get_symbol(move, matrix, i, j) for key, move in movements.items()}
    if any(symbol is None for symbol in symbols.values()):
        return 0
    x1 = symbols['NW'] + 'A' + symbols['SE']
    x2 = symbols['SW'] + 'A' + symbols['NE']
    return 1 if (x1 in MATCHES and x2 in MATCHES) else 0


def main():
    with open('resources/day04.txt', 'r') as file:
        matrix = [line for line in file]
    answer = sum([x_mas_count(matrix, i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))])
    print(f"The answer is {answer}")


if __name__ == '__main__':
    main()