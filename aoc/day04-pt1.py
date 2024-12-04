from typing import Callable, Tuple, Optional

XMAS = 'XMAS'

directions = [
    lambda i, j: (i + 1, j), # North
    lambda i, j: (i - 1, j), # South
    lambda i, j: (i, j + 1), # East
    lambda i, j: (i, j - 1), # West
    lambda i, j: (i + 1, j + 1), # NE
    lambda i, j: (i - 1, j + 1), # SE
    lambda i, j: (i + 1, j - 1), # NW
    lambda i, j: (i - 1, j - 1), # SW
]


def next_symbol(symbol: str) -> Optional[str]:
    idx = XMAS.find(symbol) + 1
    return XMAS[idx] if idx < len(XMAS) else None


def follow_direction(direction: Callable[[int, int], Tuple[int, int]], matrix: [str], i: int, j: int, symbol: str) -> int:
    ii, jj = direction(i, j)
    if ii not in range(len(matrix)):
        return 0
    if jj not in range(len(matrix[ii])):
        return 0
    if matrix[ii][jj] != symbol:
        return 0
    next_sym = next_symbol(symbol)
    if next_sym is None:
        return 1
    return follow_direction(direction, matrix, ii, jj, next_sym)


def xmas_count(matrix: [str], i: int, j: int,) -> int:
    if matrix[i][j] != 'X':
        return 0
    return sum([follow_direction(direction, matrix, i, j, 'M') for direction in directions])


def main():
    with open('resources/day04.txt', 'r') as file:
        matrix = [line for line in file]
    answer = sum([xmas_count(matrix, i, j) for i in range(len(matrix)) for j in range(len(matrix[i]))])
    print(f"The answer is {answer}")


if __name__ == '__main__':
    main()