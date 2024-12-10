
class BlockInfo:
    def __init__(self, symbol: str, length: int, start_idx: int):
        self.symbol = symbol
        self.length = length
        self.start_idx = start_idx

    def is_free(self) -> bool:
        return self.symbol == '.'

    def __str__(self):
        return f"BlockInfo('{self.symbol}', {self.length}, {self.start_idx})"


def main():
    block_infos = []
    blocks = []
    with open('resources/day09.txt', 'r') as file:
        for line in file:
            for idx, c in enumerate(line.strip()):
                symbol = f"{int(idx/2)}" if (idx % 2) == 0 else '.'
                block_infos.append(BlockInfo(symbol, int(c), len(blocks)))
                blocks += [symbol for _ in range(int(c))]

    for j in range(len(block_infos) - 1, -1, -1):
        blk_j = block_infos[j]
        if not blk_j.is_free():
            for i in range(j):
                blk_i = block_infos[i]
                if blk_i.is_free() and blk_i.length >= blk_j.length:
                    # swap blocks
                    print(f"Move {blk_j} to {blk_i}")
                    for x in range(blk_i.start_idx, blk_i.start_idx + blk_j.length):
                        blocks[x] = blk_j.symbol
                    for x in range(blk_j.start_idx, blk_j.start_idx + blk_j.length):
                        blocks[x] = '.'
                    # remove free space from this block_info that is now occupied
                    blk_i.start_idx += blk_j.length
                    blk_i.length -= blk_j.length
                    break

    checksum = 0
    for idx, c in enumerate(blocks):
        checksum += idx * int(c) if c != '.' else 0

    print("Defragmented blocks:")
    print(blocks)
    print(f"answer is {checksum}")


if __name__ == '__main__':
    main()