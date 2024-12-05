from math import ceil

def main():
    total = 0
    rules = set()
    with open('resources/day05.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if '|' in line:
                rules.add(line)
            elif len(line) > 0:
                pages = line.split(',')
                update_good = True
                for idx, i in enumerate(pages):
                    if idx < len(pages) - 1:
                        for j in pages[idx + 1:]:
                            contravening_rule = f"{j}|{i}"
                            if contravening_rule in rules:
                                update_good = False
                if update_good:
                    middle_idx = ceil((len(pages) - 1) / 2)
                    total += int(pages[middle_idx])

    print(f"The answer is {total}")


if __name__ == '__main__':
    main()