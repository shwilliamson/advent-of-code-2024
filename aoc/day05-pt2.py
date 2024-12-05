from math import ceil

rules = set()


def update_good(pages: [str]) -> bool:
    for idx, i in enumerate(pages):
        if idx < len(pages) - 1:
            for j in pages[idx + 1:]:
                contravening_rule = f"{j}|{i}"
                if contravening_rule in rules:
                    return False
    return True


def find_first(pages: [str]) -> str:
    for i in pages:
        is_good = True
        for j in pages:
            contravening_rule = f"{j}|{i}"
            if contravening_rule in rules:
                is_good = False
        if is_good:
            return i
    raise ValueError(f"Can't find a page to go first in {pages}")


def fix_update(pages: [str]) -> [str]:
    if len(pages) == 0:
        return []
    first = find_first(pages)
    pages.remove(first)
    return [first] + fix_update(pages)


def main():
    total = 0
    with open('resources/day05.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if '|' in line:
                rules.add(line)
            elif len(line) > 0:
                pages = line.split(',')
                if not update_good(pages):
                    reordered_update = fix_update(pages)
                    middle_idx = ceil((len(reordered_update) - 1) / 2)
                    total += int(reordered_update[middle_idx])

    print(f"The answer is {total}")


if __name__ == '__main__':
    main()