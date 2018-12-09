from collections import defaultdict
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


def build_dependencies_from_pairs(pairs):
    dependencies = defaultdict(set)
    for pair in pairs:
        dependencies[pair[1]].add(pair[0])
        if pair[0] not in dependencies:
            dependencies[pair[0]] = set()
    return dependencies


def create_order(dependencies):
    result = []
    # keep going until all of the dependencies are resolved
    while dependencies:
        # if any of the dependencies have been met, add the first of them to the results
        for entry in sorted(dependencies.keys()):
            if not dependencies[entry]:
                result.append(entry)
                del dependencies[entry]
                break
        # this dependency has been met - remove it from all of the remaining dependency lists
        for remaining_entry in dependencies:
            if entry in dependencies[remaining_entry]:
                dependencies[remaining_entry].remove(entry)
    return result


the_pairs = get_pairs_from_file("day7_input.txt")
the_dependencies = build_dependencies_from_pairs(the_pairs)
list_result = create_order(the_dependencies)
string_result = ''.join(list_result)
print(string_result)
if string_result != "GNJOCHKSWTFMXLYDZABIREPVUQ":
    print("WRONG ANSWER (should be'GNJOCHKSWTFMXLYDZABIREPVUQ')")
