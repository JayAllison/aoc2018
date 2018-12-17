GENERATIONS = 20
PAD = 20


def parse_input_file(filename):
    data = open(filename)
    plant_input = data.readline()
    plants = ['.']*PAD + list(plant_input.rstrip().split(': ')[1]) + ['.']*PAD
    data.readline()
    rules = [list(line.split(' => ')[0]) for line in data.readlines() if line.rstrip().split(' => ')[1] == "#"]
    return plants, rules


def parse_results_file(filename):
    return [list(line.split(": ")[1].rstrip()) for line in open(filename).readlines()]


def run_a_generation(plants, rules):
    return ['.']*2 + ['#' if plants[plant-2:plant+3] in rules else '.' for plant in range(2, len(plants)-2)] + ['.']*2


def get_score(plants):
    return sum([i - PAD for i in range(len(plants)) if plants[i] == '#'])


test = False
if test:
    input_filename = "day12_test_input.txt"
    test_results_filename = "day12_test_output.txt"
    test_results = parse_results_file(test_results_filename)
else:
    input_filename = "day12_input.txt"
    test_results = []

the_plants, the_rules = parse_input_file(input_filename)
for generation in range(GENERATIONS + 1):
    if test and test_results[generation] == the_plants[(PAD-3):len(test_results[generation])+(PAD-3)]:
        # for our test case, compare the expected result to the the middle of our working array
        print(f'Generation {generation}: PASS')
    print(f'Generation {generation}: {get_score(the_plants)}')
    the_plants = run_a_generation(the_plants, the_rules)
