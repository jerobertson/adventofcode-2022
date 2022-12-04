from pathlib import Path
import re

def any_overlap(lines):
    sum = 0

    for l in lines:
        a_min, a_max, b_min, b_max = map(int, re.findall(r"\d+", l))

        if (a_max < b_min or b_max < a_min):
            sum += 1

    print(len(lines) - sum)


def inside_range(lines):
    sum = 0

    for l in lines:
        a_min, a_max, b_min, b_max = map(int, re.findall(r"\d+", l))

        if (a_min >= b_min and a_max <= b_max) or (b_min >= a_min and b_max <= a_max):
            sum += 1

    print(sum)
    

def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    inside_range(lines)
    any_overlap(lines)
