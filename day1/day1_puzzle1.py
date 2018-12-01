frequency = 0
with open("day1_input.txt") as input_file:
    for entry in input_file:
        frequency += int(entry)

print(frequency)
