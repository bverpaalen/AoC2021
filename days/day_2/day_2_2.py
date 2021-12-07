input_path = "input.txt"

input_file = open(input_path, 'r')

change_dir = {"up": -1, "down": +1}

hor = 0
dep = 0
aim = 0

line = input_file.readline()
while line:
    direction, value = line.split(" ")
    if direction in change_dir.keys():
        aim += int(value) * change_dir[direction]
    else:
        hor += int(value)
        dep += aim * int(value)
    line = input_file.readline()
print(hor*dep)
