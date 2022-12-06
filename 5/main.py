from copy import deepcopy
from pathlib import Path
import re

def hanoi(towers, moves):
    for move in moves:
        for _ in range(0, int(move[0])):
            from_tower = int(move[1]) - 1
            to_tower = int(move[2]) - 1

            towers[to_tower].insert(0, towers[from_tower].pop(0))

    print("".join([t[0] for t in towers]))


def hanoi_9001(towers, moves):
    for move in moves:
        from_tower = int(move[1]) - 1
        to_tower = int(move[2]) - 1

        towers[to_tower] = towers[from_tower][0:int(move[0])] + towers[to_tower]
        del towers[from_tower][:int(move[0])]
    
    print("".join([t[0] for t in towers]))


def read_input(file):
    with open(file) as f:
        lines = f.readlines()
        tower_height = 8
        tower_width = int(len(lines[0])/4) 
        towers = [[] * i for i in range (tower_width)]

        for w in range(0, tower_width*4, 4):
            for h in range(0, tower_height):
                if lines[h][w+1] != " ":
                    towers[int(w/4)].append(lines[h][w+1])

        moves = [re.findall(r"\d+",l) for l in lines[-len(lines)+10:]]

        return towers, moves


if __name__ == "__main__":
    towers, moves = read_input(Path(__file__).parent / 'input.txt')
    hanoi(deepcopy(towers), moves)
    hanoi_9001(deepcopy(towers), moves)
