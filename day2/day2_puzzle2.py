# from https://pythonadventures.wordpress.com/2010/10/19/hamming-distance/
def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


filename = "day2_input.txt"
with open(filename) as input_file1:
    for box_id1 in input_file1:
        with open(filename) as input_file2:
            for box_id2 in input_file2:
                if hamming_distance(box_id1, box_id2) == 1:
                    print(f'{box_id1}{box_id2}')
                    exit(0)
