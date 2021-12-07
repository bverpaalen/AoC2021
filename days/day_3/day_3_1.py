input_path = "input.txt"

input_file = open(input_path, 'r')

byte = input_file.readline()
pos_count = {}
while byte:
    for pos in range(len(byte)):
        bit = byte[pos]

        if pos in pos_count.keys():
            pos_count[pos][int(bit)] += 1
        else:

            if bit == "0":
                pos_count.update({pos: [1, 0]})
            elif bit == "1":
                pos_count.update({pos: [0, 1]})

    byte = input_file.readline()

gamma_byte = ""
epsilon_byte = ""
for pos in range(len(pos_count.keys())):
    if pos_count[pos][0] > pos_count[pos][1]:
        gamma_byte += "0"
        epsilon_byte += "1"
    elif pos_count[pos][0] < pos_count[pos][1]:
        gamma_byte += "1"
        epsilon_byte += "0"

gamma = int(gamma_byte, 2)
epsilon = int(epsilon_byte, 2)

print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")

power_con = gamma * epsilon

print(f"Power consumption: {power_con}")
