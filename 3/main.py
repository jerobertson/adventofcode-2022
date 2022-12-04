from pathlib import Path

def priority(letter):
    out = ord(letter.swapcase()) - ord("A") + 1
    return out if letter.islower() else out - 6


def sum_groups(lines):
    sum = 0

    for i in range(0, len(lines),3):
        a = lines[i]
        b = lines[i+1]
        c = lines[i+2]

        for l in a:
            if l in b and l in c:
                sum += priority(l)
                break
    print(sum)


def sum_priorities(lines):
    sum = 0

    for l in lines:
        first, second = l[:len(l)//2], l[len(l)//2:]
        for i in range(0, len(first)):
            if first[i] in second:
                sum += priority(first[i])
                break
    print(sum)


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    sum_priorities(lines)
    sum_groups(lines)
