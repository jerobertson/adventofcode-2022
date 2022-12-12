from pathlib import Path

import re

def render_pixel(display, cycle, x):
    row = int((cycle) / 40)
    column = (cycle) % 40
    if column == x or column == x+1 or column == x+2:
        display[row] = display[row] + "#"
    else:
        display[row] = display[row] + "."


def render_screen(lines):
    cycle = 0
    x = 0
    display = ["","","","","",""]

    for l in lines:
        instruction = re.match(r"(\w+)", l)
        adjustment = re.match(r"\w+ (\-?\d+)", l)

        if instruction and instruction[1] == "noop":
            render_pixel(display, cycle, x)
            cycle += 1
        if instruction and instruction[1] == "addx":
            render_pixel(display, cycle, x)
            cycle += 1
            render_pixel(display, cycle, x)
            cycle += 1
            x += int(adjustment[1])
    
    for row in display:
        print(row)


def update_strength(strength, cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        strength += x * cycle
    return strength


def signal_strength(lines):
    cycle = 1
    x = 1
    strength = 0
    for l in lines:
        instruction = re.match(r"(\w+)", l)
        adjustment = re.match(r"\w+ (\-?\d+)", l)

        if instruction and instruction[1] == "noop":
            strength = update_strength(strength, cycle, x)
            cycle += 1
        if instruction and instruction[1] == "addx":
            strength = update_strength(strength, cycle, x)
            cycle += 1
            strength = update_strength(strength, cycle, x)
            cycle += 1
            x += int(adjustment[1])

    print(strength)


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    signal_strength(lines)
    render_screen(lines)
