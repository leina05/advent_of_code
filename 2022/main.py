import math
from pprint import pprint
import numpy as np
import copy


def day1(part: int):
    print("Day 1")
    with open("input/day1.txt", "r") as f:
        input = f.readlines()
        max1 = 0
        max2 = 0
        max3 = 0
        current = 0
        for n in input:
            if n.isspace():
                print(f"current: {current}")
                print(f"max1: {max1}")
                print(f"max2: {max2}")
                print(f"max3: {max3}")
                if current > max1:
                    max3 = max2
                    max2 = max1
                    max1 = current
                    print("updated max1")
                elif current > max2:
                    max3 = max2
                    max2 = current
                    print("updated max2")
                elif current > max3:
                    max3 = current
                    print("updated max3")
                current = 0
                continue
            current += int(n)
    if part == 1:
        print(max1)
    elif part == 2:
        print(max1 + max2 + max3)
    else:
        raise Exception("Invalid argument")


def day2(part: int):
    print(f"Day 2 part {part}")
    move_score = {"X": 1, "Y": 2, "Z": 3}
    wins = {"A": "Y", "B": "Z", "C": "X"}
    ties = {"A": "X", "B": "Y", "C": "Z"}
    outcome = {"X": 0, "Y": 3, "Z": 6}
    loses = {"A": "Z", "B": "X", "C": "Y"}
    move_selector = {"X": loses, "Y": ties, "Z": wins}
    with open("input/day2.txt", "r") as f:
        input = f.readlines()
        total = 0
        for l in input:
            chars = l.split(" ")
            assert len(chars) == 2
            first = chars[0].lstrip()
            second = chars[1].rstrip()
            if part == 1:
                total += move_score[second]
                print(first)
                print(second)
                print(f"total with move score: {total}")
                if second == wins[first]:
                    total += 6
                    print(f"total with win: {total}")
                elif second == ties[first]:
                    total += 3
                    print(f"total with tie: {total}")
            elif part == 2:
                print(first)
                print(second)
                total += outcome[second]
                my_move = move_selector[second][first]
                print(f"my move: {my_move}")
                total += move_score[my_move]
                print(f"total with my move: {total}")
            else:
                raise Exception("Invalid argument")

    print(total)


def day3(part: int):
    def get_priority(c):
        A = 97
        a = 65
        c = ord(c)
        if c >= A:
            return c - A + 1
        elif c >= a:
            return c - a + 27
        else:
            raise Exception("internal error")

    with open("input/day3.txt", "r") as f:
        input = f.readlines()
        total = 0
        A = 97
        a = 65
        total = 0
        for i, l in enumerate(input):
            if part == 1:
                size = len(l)
                mid = int(size / 2)
                first = l[:mid]
                second = l[mid:]
                set1 = set(first)
                set2 = set(second)
                common = list(set1.intersection(set2))
                assert len(common) == 1
                common = common[0]
                total += get_priority(common)
            elif part == 2:
                print(l)
                if i % 3 == 0:
                    common = set(l.strip())
                    continue
                common = common.intersection(set(l.strip()))
                if i % 3 == 2:
                    assert len(common) == 1
                    common = list(common)[0]
                    total += get_priority(common)
        print(total)


def day4(part: int):
    with open("input/day4.txt", "r") as f:
        input = f.readlines()
        count = 0
        for l in input:
            elves = l.split(",")
            assert len(elves) == 2
            first = elves[0].lstrip().split("-")
            second = elves[1].lstrip().split("-")
            set1 = set(range(int(first[0]), int(first[1]) + 1))
            set2 = set(range(int(second[0]), int(second[1]) + 1))
            ix = set1.intersection(set2)
            if part == 1:
                if len(ix) == len(set1) or len(ix) == len(set2):
                    count += 1
            elif part == 2:
                if len(ix) > 0:
                    count += 1
    print(count)


def day5(part: int):
    with open("input/day5.txt", "r") as f:
        input = f.readlines()

        stacks = {}
        procedure = False
        for l in input:
            if l.isspace():
                procedure = True
                pprint(stacks)
                continue
            if not procedure:
                # assemble stacks
                for i, c in enumerate(l):
                    if not c.isspace() and c != "[" and c != "]":
                        si = int((i + 3) / 4)
                        if stacks.get(si):
                            s = stacks.get(si)
                            s.insert(0, c)
                        else:
                            stacks[si] = [c]
            else:
                # follow procedure
                parts = l.split(" ")
                n = int(parts[1])
                f = int(parts[3])
                t = int(parts[5])
                if part == 1:
                    for i in range(n):
                        c = stacks.get(f).pop()
                        stacks.get(t).append(c)
                else:
                    cs = stacks.get(f)[-n:]
                    stacks[f] = stacks.get(f)[:-n]
                    stacks.get(t).extend(cs)

        pprint(stacks)
        message = ""
        keys = [int(k) for k in stacks.keys()]
        keys.sort()
        for s in keys:
            message = str.join("", [message, stacks.get(s).pop()])

        print(message)


def day6(part: int):
    if part == 1:
        seq_len = 4
    else:
        seq_len = 14
    with open("input/day6.txt", "r") as f:
        input = f.readline()
        for i in range(len(input)):
            if i >= seq_len - 1:
                seq = input[i - (seq_len - 1) : i + 1]
                if len(set(seq)) == seq_len:
                    print(seq)
                    print(i + 1)
                    break


def day7(part: int):
    with open("input/day7.txt", "r") as f:
        input = f.readlines()
        tree = {}
        stack = []
        # create graph
        for l in input:
            if l.isspace():
                continue
            parts = l.split(" ")
            parts = [p.strip() for p in parts]
            if parts[0] == "$":
                if parts[1] == "cd":
                    assert len(parts) == 3
                    if parts[2] == "..":
                        stack.pop()
                    else:
                        stack.append(parts[2])
                elif parts[1] == "ls":
                    continue
                else:
                    raise Exception(f"unexpected pattern: {l}")
            elif parts[0] == "dir":
                assert len(parts) == 2
                key = "".join(stack)
                if tree.get(key) is None:
                    tree[key] = {"dirs": set(), "files": set()}
                tree[key]["dirs"].add(parts[1])
            else:
                assert len(parts) == 2
                key = "".join(stack)
                if tree.get(key) is None:
                    tree[key] = {"dirs": set(), "files": set()}
                tree[key]["files"].add((int(parts[0]), parts[1]))

        sizes = {}

        def sum_files(current: str) -> int:
            node = tree[current]
            total = sum([s[0] for s in node["files"]])
            for d in node["dirs"]:
                total += sum_files(current + d)
            sizes[current] = total
            return total

        sum_files("/")

        if part == 1:
            LIMIT = 100000
            print(sum([v for (_, v) in sizes.items() if v <= LIMIT]))
        else:
            TOTAL_DISK = 70000000
            REQ_DISK_FREE = 30000000
            disk_used = sizes["/"]
            disk_free = TOTAL_DISK - disk_used
            to_delete = REQ_DISK_FREE - disk_free
            min = disk_used
            for (_, v) in sizes.items():
                if v >= to_delete and v < min:
                    min = v
            print(min)


def find_visible(arr):
    v = set()
    max = 0
    for i, n in enumerate(arr):
        n = int(n)
        if i == 0 or n > max:
            max = n
            v.add(i)
    return v


def day8(part: int):
    with open("input/day8.txt", "r") as f:
        input = f.readlines()
        input = [list(row.strip()) for row in input]
        arr = np.array(input)
        visible = 0
        max_score = 0
        rows = len(arr)
        cols = len(arr[0])
        for m in range(rows):
            for n in range(cols):
                if m == 0 or m == rows - 1 or n == 0 or n == cols - 1:
                    visible += 1
                    continue
                tree = arr[m][n]
                row = arr[m]
                left = row[:n]
                right = row[n + 1 :]

                col = arr[:, n]
                up = col[:m]
                down = col[m + 1 :]
                if (
                    tree > max(left)
                    or tree > max(right)
                    or tree > max(up)
                    or tree > max(down)
                ):
                    visible += 1

                left_d = min([n - i for i, t in enumerate(left) if t >= tree or i == 0])
                right_d = min(
                    [
                        i + 1
                        for i, t in enumerate(right)
                        if t >= tree or i == len(right) - 1
                    ]
                )
                up_d = min([m - i for i, t in enumerate(up) if t >= tree or i == 0])
                down_d = min(
                    [
                        i + 1
                        for i, t in enumerate(down)
                        if t >= tree or i == len(down) - 1
                    ]
                )
                score = left_d * right_d * up_d * down_d
                if score > max_score:
                    max_score = score

        if part == 1:
            print(visible)
        else:
            print(max_score)

def day9(part: int):
    with open("input/day9.txt", "r") as f:
        input = f.readlines()
        visited = set()
        if part == 1:
            k = 2
        else:
            k = 10
        positions = [[0,0] for _ in range(k)]
        visited.add(tuple(positions[k-1]))
        for i, l in enumerate(input):
            parts = l.split(" ")
            d = parts[0].strip()
            n = parts[1].strip()

            for _ in range(int(n)):
                if d == "R":
                    positions[0][0] += 1
                elif d == "L":
                    positions[0][0] -= 1
                elif d == "U":
                    positions[0][1] += 1
                elif d == "D":
                    positions[0][1] -= 1

                for i in range(1,k):
                    h_x = positions[i-1][0]
                    h_y = positions[i-1][1]
                    t_x = positions[i][0]
                    t_y = positions[i][1]

                    if abs(h_x - t_x) > 1:
                        if t_x < h_x:
                            t_x += 1
                        elif t_x > h_x:
                            t_x -= 1
                        if t_y > h_y:
                            t_y -= 1
                        elif t_y < h_y:
                            t_y += 1
                    elif abs(h_y - t_y) > 1:
                        if t_y < h_y:
                            t_y += 1
                        elif t_y > h_y:
                            t_y -= 1
                        if t_x > h_x:
                            t_x -= 1
                        elif t_x < h_x:
                            t_x += 1
                    positions[i][0] = t_x
                    positions[i][1] = t_y

                visited.add(tuple(positions[k-1]))

        print(len(visited))

def day10(part: int):
    def get_crt_coords(cycle: int):
        x = (cycle-1) % 40
        y = int((cycle-1) / 40)
        return (x, y)
    with open("input/day10.txt", "r") as f:
        input = f.readlines()
        cycle = 1
        x = 1
        sum = 0
        screen = [[' ' for _ in range(40)] for _ in range(6)]
        for l in input:
            if part == 1:
                if cycle == 20 or (cycle-20) % 40 == 0:
                    sum += x * cycle
            else:
                (col, row) = get_crt_coords(cycle)
                if col in [x-1, x, x+1]:
                    screen[row][col] = '#'
            parts = [c.strip() for c in l.split(" ")]
            if parts[0] == "noop":
                cycle += 1
            elif parts[0] == "addx":
                cycle += 1
                if part == 1:
                    if cycle == 20 or (cycle-20) % 40 == 0:
                        sum += x * cycle
                else:
                    (col, row) = get_crt_coords(cycle)
                    if col in [x-1, x, x+1]:
                        screen[row][col] = '#'
                cycle += 1
                x += int(parts[1])
        if part == 1:
            print(sum)
        else:
            for r in screen:
                print("".join(r))


def day11(part: int):
    monkeys = {}
    # build monkey init state
    with open("input/day11.txt", "r") as f:
        input = f.readlines()
        current_monkey = 0
        for l in input:
            l = l.strip()
            if l.startswith("Monkey"):
                current_monkey = int(l.split(" ")[1][0])
                monkeys[current_monkey] = {}
            elif l.startswith("Starting items:"):
                monkeys[current_monkey]["items"] = [int(p.strip()) for p in l.split(":")[1].split(",")]
            elif l.startswith("Operation:"):
                monkeys[current_monkey]["op"] = l.split("=")[1].strip().split(" ")[1:]
            elif l.startswith("Test:"):
                monkeys[current_monkey]["div_by"] = int(l.split(" ")[-1].strip())
            elif l.startswith("If true:"):
                monkeys[current_monkey]["true_monkey"] = int(l.split(' ')[-1].strip())
            elif l.startswith("If false:"):
                monkeys[current_monkey]["false_monkey"] = int(l.split(' ')[-1].strip())


    lcm = math.lcm(*[m["div_by"] for m in monkeys.values()])

    activity = [0 for _ in range(len(monkeys))]
    for _ in range(20):
        for m in range(len(monkeys)):
            monkey = monkeys[m]
            items = copy.deepcopy(monkey["items"])
            monkey["items"] = []
            for j, i in enumerate(items):
                activity[m] += 1
                operand = monkey["op"][1]
                if operand == "old":
                    operand = i
                else:
                    operand = int(operand)
                # apply operation
                if monkey["op"][0] == "*":
                    i = i * operand
                elif monkey["op"][0] == "+":
                    i = i + operand
                if part == 1:
                    # divide by 3
                    i = int(i / 3)
                # test
                if i % monkey["div_by"] == 0:
                    true_monkey = monkey["true_monkey"]
                    monkeys[true_monkey]["items"].append(i % lcm) # checked the sub for this guy :)
                else:
                    false_monkey = monkey["false_monkey"]
                    monkeys[false_monkey]["items"].append(i % lcm)


    pprint(activity)
    activity.sort(reverse=True)
    monkey_businiess = activity[0] * activity[1]
    print(monkey_businiess)



def main():
    # day1(part=1)
    # day1(part=2)
    # day2(part=1)
    # day2(part=2)
    # day3(part=1)
    # day3(part=2)
    # day4(part=1)
    # day4(part=2)
    # day5(part=1)
    # day5(part=2)
    # day6(part=1)
    # day6(part=2)
    # day7(part=1)
    # day7(part=2)
    # day8(part=1)
    # day8(part=2)
    # day9(part=1)
    # day9(part=2)
    # day10(part=1)
    # day10(part=2)
    # day11(part=1)
    day11(part=2)



if __name__ == "__main__":
    main()
