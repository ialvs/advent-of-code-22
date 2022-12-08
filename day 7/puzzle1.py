with open('input2.txt') as input:
    lines = input.readlines()


def get_directories_size(lines):
    current_path = ''
    directory = {'/': 0}
   

    for line in lines:
        line.replace('\n','')
        if '$ ls' in line:
            continue
        elif "$ cd /" in line:
            current_path = "/"
        elif "$ cd .." in line:
            current_path = "/".join(current_path.split("/")[:-2]) + "/"
        elif line.startswith("$ cd"):
            current_path += line.split(" ")[-1] + "/"
        elif line.startswith("dir "):
            directory[current_path + line.split(" ")[-1] + "/"] = 0
        else:
            directory[current_path] += int(line.split(" ")[0])
    return {k: sum([directory[l] for l in directory if l.startswith(k)]) for k in directory}

def part_1(lines):
    dir_sizes = get_directories_size(lines)
    return sum([dir_sizes[d] for d in dir_sizes if dir_sizes[d] <= 100000])

output = part_1(lines = lines)
possibilities = []

def part_2(lines):
    dir_sizes = get_directories_size(lines)
    available = 70000000 - dir_sizes["/"]
    needed = 30000000 - available
    return min([dir_sizes[d] for d in dir_sizes if dir_sizes[d] >= needed])


print(part_2(lines))