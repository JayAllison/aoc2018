import pprint
pp = pprint.PrettyPrinter()


class Tree(object):

    def __init__(self):
        self.nodes = []
        self.data = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_data(self, data):
        self.data.append(data)


def parse_substring_into_tree(tree, buf, pos):
    # recurse through the string of numbers
    # call this once for each of the indicated nodes, advance the pointer after
    # when we're done, the pointer will point to the metadata
    node_count = buf[pos]
    pos += 1
    data_count = buf[pos]
    pos += 1
    for i in range(node_count):
        tree.add_node(Tree())
        pos = parse_substring_into_tree(tree.nodes[i], buf, pos)
    for i in range(data_count):
        tree.add_data(buf[pos])
        pos += 1
    return pos


def sum_tree_data(tree):
    total = 0
    for node in tree.nodes:
        total += sum_tree_data(node)
    total += sum(tree.data)
    return total


def calculate_tree_value(tree):
    length = len(tree.nodes)
    if not length:
        total = sum(tree.data)
        return total
    else:
        total = 0
        for i in tree.data:
            i = i - 1
            if i < length:
                total += calculate_tree_value(tree.nodes[i])
        return total


input_file = open("day8_input.txt")
the_numbers = [int(s) for s in input_file.readline().split()]
the_tree = Tree()

parse_substring_into_tree(the_tree, the_numbers, 0)
answer = sum_tree_data(the_tree)
print("Sum of Metadata = " + str(answer))

answer = calculate_tree_value(the_tree)
print("Tree Value = " + str(answer))
