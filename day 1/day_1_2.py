input_file = open("input.txt", "r")

text = input_file.readlines()

counter = 0

numbers = []
for line in text:
    numbers.append(int(line))

for i in range(len(numbers)):
    if (i+3) > len(numbers):
        break

    old_window = numbers[i:i+3]
    new_window = numbers[i+1:i+4]

    if sum(new_window) > sum(old_window):
        counter += 1

print(counter)