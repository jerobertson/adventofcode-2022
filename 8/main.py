from pathlib import Path

def visible_trees(lines):
    count = 0

    for y in range(0, len(lines)):
        for x in range (0, len(lines[y].strip())):
            visible = False

            m = -1
            for yi in range(0, y):
                m = max(int(lines[yi][x]), m)
            if m < int(lines[y][x]):
                visible = True

            m = -1
            for yi in range(y+1, len(lines)):
                m = max(int(lines[yi][x]), m)
            if m < int(lines[y][x]):
                visible = True

            m = -1
            for xi in range(0, x):
                m = max(int(lines[y][xi]), m)
            if m < int(lines[y][x]):
                visible = True

            m = -1
            for xi in range(x+1, len(lines[y].strip())):
                m = max(int(lines[y][xi]), m)
            if m < int(lines[y][x]):
                visible = True

            if (visible):
                count += 1

    print(count)


def scenic_score(lines):
    best_score = 0

    for y in range(1, len(lines)-1):
        for x in range (1, len(lines[y].strip())-1):
            individual_score = 1

            # check north
            score = 0
            for yi in range(1, y+1):
                score += 1
                if int(lines[y-yi][x]) >= int(lines[y][x]):
                    break
            individual_score *= score

            # check south
            score = 0
            for yi in range(y+1, len(lines)):
                score += 1
                if (int(lines[yi][x]) >= int(lines[y][x])):
                    break
            individual_score *= score

            # check west
            score = 0
            for xi in range(1, x+1):
                score += 1
                if int(lines[y][x-xi]) >= int(lines[y][x]):
                    break
            individual_score *= score

            # check east
            score = 0
            for xi in range(x+1, len(lines[y].strip())):
                score += 1
                if (int(lines[y][xi]) >= int(lines[y][x])):
                    break
            individual_score *= score

            best_score = max(best_score, individual_score)

    print(best_score)


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    visible_trees(lines)
    scenic_score(lines)
