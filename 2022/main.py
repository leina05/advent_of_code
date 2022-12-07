

from pprint import pprint


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
            assert(len(chars) == 2)
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
                mid = int(size/2)
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
                seq = input[i-(seq_len-1):i+1]
                if len(set(seq)) == seq_len:
                    print(seq)
                    print(i + 1)
                    break


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
    day6(part=2)


if __name__ == "__main__":
    main()