from pathlib import Path

import re

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.folders = []
        self.files = []

    def get_size(self):
        total_size = sum([f.size for f in self.files])
        for folder in self.folders:
            total_size += folder.get_size()
        return total_size


def parse_tree(lines):
    filesystem = Folder("*", None)
    pointer = filesystem
    
    for l in lines:
        folder_name = re.match(r"\$ cd (\/|\.\.|\w+)", l)
        file = re.match(r"^(\d+) (.+)$", l)
        if folder_name and folder_name[1] != "..":
            new_dir = Folder(folder_name[1], pointer)
            pointer.folders.append(new_dir)
            pointer = new_dir
        if folder_name and folder_name[1] == "..":
            pointer = pointer.parent
        if file:
            pointer.files.append(File(file[2], int(file[1])))

    return filesystem.folders[0]


def dir_sizes(root):
    total_size = 0

    for dir in root.folders:
        if dir.get_size() <= 100000:
            total_size += dir.get_size()
        total_size += dir_sizes(dir)

    return total_size


def all_dir_sizes(root):
    sizes = []

    for dir in root.folders:
        sizes.append(dir.get_size())
        sizes += all_dir_sizes(dir)

    return sizes


def clear_space(root):
    total_space = 70000000
    required_space = 30000000
    used_space = root.get_size()
    remaining_space = total_space - used_space
    to_clear = required_space - remaining_space

    all_sizes = all_dir_sizes(root)
    all_sizes.sort()

    for size in all_sizes:
        if size >= to_clear:
            return size


def read_input(file):
    with open(file) as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input(Path(__file__).parent / 'input.txt')
    root = parse_tree(lines)
    print(dir_sizes(root))
    print(clear_space(root))
