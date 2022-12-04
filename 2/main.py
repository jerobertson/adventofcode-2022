from pathlib import Path

def strategy_score(lines):
    combinations = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7
    }

    sum = 0
    for l in lines:
        sum += combinations[l[0] + l[2]]

    print(sum)


def rps_score(lines):
    combinations = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3
    }
    hand_values = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    sum = 0
    for l in lines:
        sum += combinations[l[0] + l[2]] + hand_values[l[2]]

    print(sum)


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    rps_score(lines)
    strategy_score(lines)
