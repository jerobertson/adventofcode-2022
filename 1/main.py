from pathlib import Path
import re


def calorie_count_many_elves(lines, count):
    max_calories = [0] * count
    current_calories = 0

    for l in lines:
        calories = re.sub('\D', '', l)
        if (calories == ''):
            for i in range(0,len(max_calories)):
                if current_calories > max_calories[i]:
                    max_calories[i] = current_calories
                    max_calories.sort()
                    break
            current_calories = 0
        else:
            current_calories += int(calories)
    
    print(sum(max_calories))


def calorie_count(lines):
    max_calories = 0
    current_calories = 0

    for l in lines:
        calories = re.sub('\D', '', l)
        if (calories == ''):
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        else:
            current_calories += int(calories)
    
    print(max_calories)


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    calorie_count(lines)
    calorie_count_many_elves(lines, 3)
