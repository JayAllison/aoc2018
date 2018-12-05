alphabet = 'abcdefghijklmnopqrstuvwxyz'
littles = [c for c in alphabet.lower()]
bigs = [c for c in alphabet.upper()]

half1 = [c1 + c2 for c1, c2 in zip(littles, bigs)]
half2 = [c1 + c2 for c1, c2 in zip(bigs, littles)]
combos = half1 + half2

the_string = open("day5_input.txt").readline().rstrip()

running = True
while running:
    before = len(the_string)
    for combo in combos:
        the_string = the_string.replace(combo, '')
    after = len(the_string)
    running = before != after

print(len(the_string))
