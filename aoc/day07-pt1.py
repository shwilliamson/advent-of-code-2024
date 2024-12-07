from itertools import product
from typing import Callable

operators = [
    lambda a, b: a + b,
    lambda a, b: a * b,
]

def evaluate(operands: [int], ops:[Callable[[int,int],int]]) -> int:
    result = operands[0]
    for i in range(len(ops)):
        result = ops[i](result, operands[i+1])
    return result


def is_valid(test_val: int, operands: [int]) -> bool:
    operator_combos = product(operators, repeat=len(operands) - 1)
    for operator_combo in operator_combos:
        if evaluate(operands, operator_combo) == test_val:
            return True
    return False

def main():
    with open('resources/day07.txt', 'r') as file:
        answer = 0
        for line in file:
            parts = line.strip().split(":")
            test_val = int(parts[0])
            operands = [int(x) for x in parts[1].strip().split()]
            if is_valid(test_val, operands):
                answer += test_val
        print(f"answer is {answer}")

if __name__ == '__main__':
    main()