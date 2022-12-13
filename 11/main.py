from pathlib import Path

import re

inspections = [0,0,0,0,0,0,0,0]
items = [[71,86], [66,50,90,53,88,85], [97,54,89,62,84,80,63], [82,97,56,92], [50,99,67,61,86], [61,66,72,55,64,53,72,63], [59,79,63], [55]]
operations = [lambda x: x * 13, lambda x: x + 3, lambda x: x + 6, lambda x: x + 2, lambda x: x * x, lambda x: x + 4, lambda x: x * 7, lambda x: x +7]
tests = [lambda x: x % 19 == 0, lambda x: x % 2 == 0, lambda x: x % 13 == 0, lambda x: x % 5 == 0, lambda x: x % 7 == 0, lambda x: x % 11 == 0, lambda x: x % 17 == 0, lambda x: x % 3 == 0]
truths = [6,5,4,6,5,3,2,2]
falses = [7,4,1,0,3,0,7,1]

def worried_cycle():
    for monkey_ind in range(0, len(items)):
        monkey = items[monkey_ind]
        for item in monkey:
            item = int(operations[monkey_ind](item)) % 9699690
            if tests[monkey_ind](item):
                items[truths[monkey_ind]].append(item)
            else:
                items[falses[monkey_ind]].append(item)
            inspections[monkey_ind] += 1
        items[monkey_ind] = []


def cycle():
    for monkey_ind in range(0, len(items)):
        monkey = items[monkey_ind]
        for item in monkey:
            item = int(operations[monkey_ind](item) / 3)
            if tests[monkey_ind](item):
                items[truths[monkey_ind]].append(item)
            else:
                items[falses[monkey_ind]].append(item)
            inspections[monkey_ind] += 1
        items[monkey_ind] = []


if __name__ == "__main__":
    for i in range(0, 10000):
        #cycle()
        worried_cycle()
    print(inspections)
    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])
