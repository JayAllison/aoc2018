def score_recipes(recipe_target):
    scores = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(scores) < recipe_target + 10:
        scores += [int(c) for c in str(scores[elf1]+scores[elf2])]
        elf1 += scores[elf1] + 1
        elf2 += scores[elf2] + 1
        wrap = len(scores)
        while elf1 >= wrap:
            elf1 = elf1 % wrap
        while elf2 >= wrap:
            elf2 = elf2 % wrap

    return ''.join([str(n) for n in scores[-10:]])


targets = (
    (5, '0124515891'),
    (9, '5158916779'),
    (18, '9251071085'),
    (2018, '5941429882'),
    (702831, '1132413111'),  # this is puzzle #1
)

for target in targets:
    answer = score_recipes(target[0])
    print(f'{target[0]}: PASS' if answer == target[1] else f'{target[0]}: FAIL {answer} != {target[1]}')
