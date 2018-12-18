def score_recipes(recipe_target):
    scores = [3, 7]
    elf1 = 0
    elf2 = 1
    final = ''

    while final != recipe_target:
        scores += [int(c) for c in str(scores[elf1] + scores[elf2])]
        elf1 += scores[elf1] + 1
        elf2 += scores[elf2] + 1
        wrap = len(scores)
        while elf1 >= wrap:
            elf1 = elf1 % wrap
        while elf2 >= wrap:
            elf2 = elf2 % wrap
        final = ''.join([str(n) for n in scores[-len(recipe_target):]])
        # print(recipe_target)
        # print(final)

    return len(scores) - len(recipe_target)


targets = (
    ('01245', 5),
    ('51589', 9),
    ('92510', 18),
    ('59414', 2018),
    ('702831', None),  # this is puzzle #2
)

for target in targets:
    answer = score_recipes(target[0])
    print(f'{target[0]}: PASS' if answer == target[1] else f'{target[0]}: FAIL {answer} != {target[1]}')
