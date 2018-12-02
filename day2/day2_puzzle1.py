from collections import Counter

twos = 0
threes = 0

with open("day2_input.txt") as input_file:
    for box_id in input_file:
        char_counts = Counter(box_id)
        for char in char_counts:
            if char_counts[char] == 2:
                twos += 1
                break
        for char in char_counts:
            if char_counts[char] == 3:
                threes += 1
                break

print(f'{twos} x {threes} = {twos*threes}')
