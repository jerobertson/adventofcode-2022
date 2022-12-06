from pathlib import Path

def first_marker(code, marker_length):
    window = list(code[0:marker_length-1])
    for i in range(marker_length-1, len(code)):
        window.append(code[i])
        if (len(window) == len(set(window))):
            print(i+1)
            break
        window.pop(0)


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    first_marker(lines[0], 4)
    first_marker(lines[0], 14)
