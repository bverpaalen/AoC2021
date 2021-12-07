input_path = "input.txt"

input_file = open(input_path, 'r')

increased_counter = 0
line_counter = 2

previous_value = int(input_file.readline())
new_value = input_file.readline()

while new_value:
    new_value = int(new_value)
    if new_value > previous_value:
        increased_counter += 1
    previous_value = new_value
    print(previous_value)
    new_value = input_file.readline()

print(increased_counter)
