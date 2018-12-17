# the basic solution for puzzle 1 should work for puzzle 2, except for PAD and time
# can puzzle 1 be reworked to dynamically adjust PAD on a per-generation basis?
# if so, then puzzle 2 can just be solved with time

import datetime


ITERATIONS = 50000000000


# how long does a very basic 50-billion iteration loop take on my computer???
before = datetime.datetime.now()
count = 0
for i in range(ITERATIONS):
    count += 1
print(f'{count} iterations took {datetime.datetime.now()-before}')
