import pprint
import re

pp = pprint.PrettyPrinter()

filename = "day3_input.txt"
rows = 1000
columns = 1000

# parse the values out of a string like this: #1 @ 432,394: 29x14
claim_parser = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
claims = {}
with open(filename) as input_file:
    for claim_string in input_file:
        parsed_claim = claim_parser.search(claim_string)
        claims[parsed_claim.group(1)] = {
            "id": int(parsed_claim.group(1)),
            "x_offset": int(parsed_claim.group(2)),
            "y_offset": int(parsed_claim.group(3)),
            "x_length": int(parsed_claim.group(4)),
            "y_length": int(parsed_claim.group(5))
        }

# initialize a 2D array
fabric = [[0 for j in range(columns)] for i in range(rows)]

# apply each claim to the fabric
for claim in claims:
    for x_count in range(claims[claim]["x_length"]):
        for y_count in range(claims[claim]["y_length"]):
            x = claims[claim]["x_offset"] + x_count
            y = claims[claim]["y_offset"] + y_count
            fabric[x][y] += 1

count = 0
for x in range(rows):
    for y in range(columns):
        if fabric[x][y] > 1:
            count += 1

print(count)
