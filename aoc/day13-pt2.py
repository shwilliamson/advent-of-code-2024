import re
from typing import Optional

import numpy as np
from numpy.linalg import inv


def to_positive_whole(x: float) -> Optional[int]:
    # verify to 3 decimal places (precision matters here)
    # I get the same answer at 2 and 3 which agrees with AoC
    x = round(x, 3)
    return int(x) if x > 0 and float(int(x)) == x else None


def main():
    A = [[0, 0], [0, 0]]
    b = [0, 0]
    total_cost = 0
    with open('resources/day13.txt', 'r') as file:
        lines = [line.strip() for line in file]
        for idx, row in enumerate(lines):
            match idx % 4:
                case 0:
                    match = re.match(r"Button A: X\+(\d+), Y\+(\d+)", row)
                    A[0][0] = int(match.group(1))
                    A[1][0] = int(match.group(2))
                case 1:
                    match = re.match(r"Button B: X\+(\d+), Y\+(\d+)", row)
                    A[0][1] = int(match.group(1))
                    A[1][1] = int(match.group(2))
                case 2:
                    match = re.match(r"Prize: X=(\d+), Y=(\d+)", row)
                    b[0] = int(match.group(1)) + 10000000000000
                    b[1] = int(match.group(2)) + 10000000000000
                    try:
                        x = np.dot(inv(np.array(A)), np.array(b))
                        x0 = to_positive_whole(x[0])
                        x1 = to_positive_whole(x[1])
                        if x0 and x1:
                            total_cost += (3 * x0) + x1
                    except np.linalg.LinAlgError:
                        print("error")
                case 3:
                    A = [[0, 0], [0, 0]]
                    b = [0, 0]

        print(f"answer is {total_cost}")


if __name__ == '__main__':
    main()