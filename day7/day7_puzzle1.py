import pprint
import re


pp = pprint.PrettyPrinter()


def get_pairs_from_file(filename):
    get_pair = re.compile(r'Step (\w) must be finished before step (\w) can begin')
    pairs = []

    # build the list of pairs from the input file
    with open(filename) as input_file:
        for line in input_file:
            pair_match = get_pair.match(line)
            pairs.append((pair_match.group(1), pair_match.group(2)))

    return pairs


def get_list_of_unique_entries(pairs):
    entries = set()
    for pair in pairs:
        entries.add(pair[0])
        entries.add(pair[1])
    return sorted(list(entries))


def find_starters_from_pairs(pairs):
    # find all of the letters that appear in position 0 that do not also appear in position 1
    starters = set()
    for pair1 in pairs:
        found = False
        for pair2 in pairs:
            if pair1[0] == pair2[1]:
                found = True
                break
        if not found:
            starters.add(pair1[0])
    return sorted(list(starters))


def add_x_after_y(answer, x, y):
    i = answer.index(x) + 1
    added = False
    while i < len(answer):
        if answer[i] > y:
            if y in answer:
                added = True
                j = answer.index(y)
                if j < i:
                    del answer[j]
                    answer.insert(i - 1, y)
            else:
                answer.insert(i, y)
                added = True
                break
        i += 1
    if not added:
        if y in answer:
            j = answer.index(y)
            if j < i:
                del answer[j]
                answer.insert(i - 1, y)
        else:
            answer.append(y)


def create_order(starters, entries, pairs):
    answer = starters
    print("Starters = " + str(starters))
    # print("Entries = " + str(entries))
    # print("Pairs:")
    # pp.pprint(pairs)

    count = 0
    while entries:
        count += 1
        if count > 100:
            print("I'm stuck.")
            pp.pprint(entries)
            break
        for entry in entries:
            if entry in answer:
                entries.remove(entry)
                # now build out the rest of the sequence
                for pair in pairs:
                    if pair[0] == entry:
                        add_x_after_y(answer, pair[0], pair[1])

    return answer


the_pairs = get_pairs_from_file("day7_input.txt")
the_entries = get_list_of_unique_entries(the_pairs)
the_start = find_starters_from_pairs(the_pairs)
list_result = create_order(the_start, the_entries, the_pairs)
string_result = ''.join(list_result)
print(string_result)
