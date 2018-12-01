import datetime

frequency = 0
frequencies = []
repeating = True
count = 0

before = datetime.datetime.now()

while repeating:
    print(f'Passed through file {count} times')
    count += 1
    with open("day1_input.txt") as input_file:
        for entry in input_file:
            frequency += int(entry)
            if frequency in frequencies:
                print(frequency)
                repeating = False
                break
            else:
                frequencies.append(frequency)

after = datetime.datetime.now()

print(f'Time Elapsed: {after-before}')
