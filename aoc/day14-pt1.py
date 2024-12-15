import re

def multiply_array(arr):
    result = 1
    for num in arr:
        result *= num
    return result

def main():
    quad_counts = [0,0,0,0]
    with open('resources/day14.txt', 'r') as file:
        for line in file:
            numbers = [int(n) for n in re.findall(r'-?\d+', line.strip())]
            (x, y) = (numbers[0], numbers[1])
            (dx, dy) = (numbers[2], numbers[3])
            (x100, y100) = ((x + dx * 100) % 101, (y + dy * 100) % 103)
            if x100 in range(50) and y100 in range(51):
                quad_counts[0] += 1
            elif x100 in range(51, 101) and y100 in range(51):
                quad_counts[1] += 1
            elif x100 in range(50) and y100 in range(52, 103):
                quad_counts[2] += 1
            elif x100 in range(51, 101) and y100 in range(52, 103):
                quad_counts[3] += 1

        result = multiply_array(quad_counts)
        print(f"answer is {result}")


if __name__ == '__main__':
    main()