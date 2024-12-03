from typing import List

safe_range = range(1, 4)
allowed_anomalies = 1


def is_increasing(levels: List[int]) -> bool:
    cnt = 0
    for i in range(len(levels) - 1):
        if levels[i] < levels[i + 1]:
            cnt += 1
        elif levels[i] > levels[i + 1]:
            cnt -= 1
    if cnt == 0:
        raise AssertionError("Neither increasing nor decreasing between a majority of measurements.")
    elif cnt < 0:
        return False
    else:
        return True


def copy_and_pop(value_list, idx):
    # python doesn't make immutability easy :(
    c = value_list.copy()
    c.pop(idx)
    return c


def is_safe(levels: List[int], anomaly_count: int = 0) -> bool:
    if anomaly_count > allowed_anomalies:
        return False
    try:
        increasing = is_increasing(levels)
        for i in range(len(levels) - 1):
            delta = abs(levels[i + 1] - levels[i])
            directionally_correct = (increasing == (levels[i] < levels[i + 1]))
            if not directionally_correct or delta not in safe_range:
                # As soon as an anomaly is encountered, recurse and test
                # removing each of the levels being compared
                return (is_safe(copy_and_pop(levels, i), anomaly_count + 1) or
                        is_safe(copy_and_pop(levels, i + 1), anomaly_count + 1))
        return True
    except AssertionError:
        return False


def main():
    safe_count = 0
    with open('resources/day2.txt', 'r') as file:
        for line in file:
            levels = [int(level) for level in line.split(" ")]
            if is_safe(levels=levels):
                safe_count += 1

    print(f"There are {safe_count} safe reports.")


if __name__ == '__main__':
    main()