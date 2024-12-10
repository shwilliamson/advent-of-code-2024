
def main():
    with open('resources/day09.txt', 'r') as file:
        for line in file:
            line = line.strip()
            blocks = []
            for idx, c in enumerate(line):
                symbol = f"{int(idx/2)}" if (idx % 2) == 0 else '.'
                blocks += [symbol for _ in range(int(c))]

    j = len(blocks) - 1
    checksum = 0
    for i, c in enumerate(blocks):
        if c == '.':
            while blocks[j] == '.':
                j -= 1
            if i >= j:
                break
            blocks[i], blocks[j] = blocks[j], blocks[i]  # swap
        checksum += i * int(blocks[i])

    print(f"answer is {checksum}")


if __name__ == '__main__':
    main()