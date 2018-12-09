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


# according to the rules of the puzzle, how many seconds will this step take?
# for example, it's +1 but for actual it's +61
def get_time_for_step(c):
    return ord(c) - ord("A") + 61


def create_order(dependencies):
    count = -1
    result = []
    # keep going until all of the dependencies are resolved
    workers = []
    while dependencies or workers:
        completed_steps = []
        workers_to_remove = []
        count += 1
        # first, process the work being done in this one-second iteration and check if any steps were finished
        # if so, record which one(s) were completed and remove their worker(s) from the queue
        # we can't remove them immediately because we're iterating over that list (silly Python)
        for worker in workers:
            worker[1] -= 1
            if worker[1] == 0:
                completed_steps.append(worker[0])
                workers_to_remove.append(worker)
        for worker in workers_to_remove:
                workers.remove(worker)
        # the order here (sorted or not) doesn't actually matter, because this puzzle isn't asking for the sequence
        result += sorted(completed_steps)
        # next, if any dependencies were met this iteration, remove them from all of the remaining dependency lists
        for remaining_entry in dependencies:
            for step in completed_steps:
                if step in dependencies[remaining_entry]:
                    dependencies[remaining_entry].remove(step)
        # finally, if any of the dependencies have now been met, add them to the workers queue, if we have room
        for entry in sorted(dependencies.keys()):
            if not dependencies[entry]:
                # 2 workers for example, 5 for actual problem
                if len(workers) < 5:
                        new_worker = [entry, get_time_for_step(entry)]
                        workers.append(new_worker)
                        del dependencies[entry]
    print("Final Count = " + str(count))
    return result


the_pairs = get_pairs_from_file("day7_input.txt")
the_dependencies = build_dependencies_from_pairs(the_pairs)
list_result = create_order(the_dependencies)
string_result = ''.join(list_result)
print(string_result)
