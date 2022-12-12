from pathlib import Path

import re

def move(head, tail):
    if head[0] - tail[0] > 1:
        if head[1] - tail[1] > 1:
            return tail[0]+1, tail[1]+1
        elif head[1] - tail[1] < -1:
            return tail[0]+1, tail[1]-1
        else:
            return tail[0]+1, head[1]
    elif head[0] - tail[0] < -1:
        if head[1] - tail[1] > 1:
            return tail[0]-1, tail[1]+1
        elif head[1] - tail[1] < -1:
            return tail[0]-1, tail[1]-1
        else:
            return tail[0]-1, head[1]
    elif head[1] - tail[1] > 1:
        if head[0] - tail[0] > 1:
            return tail[0]+1, tail[1]+1
        elif head[0] - tail[0] < -1:
            return tail[0]-1, tail[1]+1
        else:
            return head[0], tail[1]+1
    elif head[1] - tail[1] < -1:
        if head[0] - tail[0] > 1:
            return tail[0]+1, tail[1]-1
        elif head[0] - tail[0] < -1:
            return tail[0]-1, tail[1]-1
        return head[0], tail[1]-1
    else:
        return tail


def big_rope(lines, size):
    knots = [(0, 0)] * size
    tail_locs = {knots[len(knots)-1]}
    
    for l in lines:
        repetitions = int(re.match(r"\w (\d+)", l)[1])
        for _ in range(repetitions):
            if l[0] == "U":
                knots[0] = knots[0][0], knots[0][1]+1
            elif l[0] == "D":
                knots[0] = knots[0][0], knots[0][1]-1
            elif l[0] == "L":
                knots[0] = knots[0][0]-1, knots[0][1]
            elif l[0] == "R":
                knots[0] = knots[0][0]+1, knots[0][1]

            for i in range(1, size):
                knots[i] = move(knots[i-1], knots[i])

            tail_locs.add(knots[len(knots)-1])

    print(len(tail_locs))


def tail_visited(lines):
    head = 0, 0
    tail = 0, 0
    tail_locs = {tail}
    
    for l in lines:
        repetitions = int(re.match(r"\w (\d+)", l)[1])
        for _ in range(repetitions):
            if l[0] == "U":
                head = head[0], head[1]+1
                if abs(head[1] - tail[1]) > 1:
                    tail = head[0], tail[1]+1
            elif l[0] == "D":
                head = head[0], head[1]-1
                if abs(head[1] - tail[1]) > 1:
                    tail = head[0], tail[1]-1
            elif l[0] == "L":
                head = head[0]-1, head[1]
                if abs(head[0] - tail[0]) > 1:
                    tail = tail[0]-1, head[1]
            elif l[0] == "R":
                head = head[0]+1, head[1]
                if abs(head[0] - tail[0]) > 1:
                    tail = tail[0]+1, head[1]
            tail_locs.add(tail)

    print(len(tail_locs))


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    tail_visited(lines)
    big_rope(lines, 10)
