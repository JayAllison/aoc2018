# this works on the test string but not on the actual string :(


def reduce(input_string):
    length = len(input_string)
    i = 0
    j = i + 1

    result = []
    reduced = False

    while i < length and j < length:
        if input_string[i].upper() == input_string[j] or input_string[i].lower() == input_string[j]:
            i = j + 1
            j = i + 1
            reduced = True
        else:
            result.append(input_string[i])
            i = j
            j += 1

    # makes an assumption that the match does not happen on the last two characters
    result.append(input_string[i])
    return reduced, result


starting_string = open("day5_input.txt").readline().rstrip()
working_buffer = [c for c in starting_string]
working = True
while working:
    working, working_buffer = reduce(working_buffer)

print(working_buffer)
print(len(working_buffer))
