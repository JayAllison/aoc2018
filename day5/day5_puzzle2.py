import pprint

pp = pprint.PrettyPrinter()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
littles = [c for c in alphabet.lower()]
bigs = [c for c in alphabet.upper()]

half1 = [c1 + c2 for c1, c2 in zip(littles, bigs)]
half2 = [c1 + c2 for c1, c2 in zip(bigs, littles)]
combos = half1 + half2

the_string = open("day5_input.txt").readline().rstrip()


def reduce(s):
    running = True
    while running:
        before = len(s)
        for combo in combos:
            s = s.replace(combo, '')
        after = len(s)
        running = before != after

    return len(s)


def remove_all(s, c):
    running = True
    while running:
        before = len(s)
        s = s.replace(c, '')
        after = len(s)
        running = before != after

    return s


results = {}

for c in alphabet:
    charless_string = remove_all(the_string, c.lower())
    charless_string = remove_all(charless_string, c.upper())
    length = reduce(charless_string)
    results[c] = length

pp.pprint(results)

min_char = None
min_count = None

for c in results:
    if not min_count or results[c] < min_count:
        min_char = c
        min_count = results[c]

print((min_char, min_count))
