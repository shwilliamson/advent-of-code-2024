

def main():
    list1 = []
    list2 = []
    with open('resources/day01.txt', 'r') as file:
        for (idx, line) in enumerate(file):
            values = line.split("   ")
            list1.append(int(values[0]))
            list2.append(int(values[1]))

    score = 0
    list2_map = {}
    for v2 in list2:
        list2_map[v2] = list2_map.get(v2, 0) + 1
    for v1 in list1:
        score += (v1 * list2_map.get(v1, 0))

    print(f"The similarity score is {score}")


if __name__ == '__main__':
    main()