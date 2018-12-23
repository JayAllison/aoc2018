# register: 0,1,2,3
# opcode: xxxx
# instruction: opcode, input, input, output
# input can be immediate (use value given) or indirect (use value in given register)
# output is always a register (indirect)


def parse_instruction_string(instruction_string):
    # ex: '4 1 0 1'
    return [int(s) for s in instruction_string.split()]


def parse_register_string(register_string):
    # ex: 'Before: [1, 0, 2, 0]' or: 'After:  [1, 1, 2, 0]'
    return [int(s) for s in register_string[9:19].split(', ')]


def addr(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]


def addi(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] + instruction[2]


def mulr(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]


def muli(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] * instruction[2]


def banr(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]


def bani(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] & instruction[2]


def borr(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]


def bori(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]] | instruction[2]


def setr(registers, instruction):
    registers[instruction[3]] = registers[instruction[1]]


def seti(registers, instruction):
    registers[instruction[3]] = instruction[1]


def gtir(registers, instruction):
    registers[instruction[3]] = int(instruction[1] > registers[instruction[2]])


def gtri(registers, instruction):
    registers[instruction[3]] = int(registers[instruction[1]] > instruction[2])


def gtrr(registers, instruction):
    registers[instruction[3]] = int(registers[instruction[1]] > registers[instruction[2]])


def eqir(registers, instruction):
    registers[instruction[3]] = int(instruction[1] == registers[instruction[2]])


def eqri(registers, instruction):
    registers[instruction[3]] = int(registers[instruction[1]] == instruction[2])


def eqrr(registers, instruction):
    registers[instruction[3]] = int(registers[instruction[1]] == registers[instruction[2]])


def compare_all_opcodes(resulting_codes, opcodes, starting_register_string, instruction_string, other_register_string):
    matching_opcodes = []
    starting_registers = parse_register_string(starting_register_string)
    other_registers = parse_register_string(other_register_string)
    instruction = parse_instruction_string(instruction_string)

    for opcode in opcodes:
        registers = starting_registers.copy()
        try:
            opcode(registers, instruction)
            if registers == other_registers:
                matching_opcodes.append((opcode.__name__, instruction[0]))
        except IndexError:
            pass

    for found_opcode in matching_opcodes:
        delete_these = []
        if found_opcode[0] in resulting_codes:
            # print(f'From {matching_opcodes} found {found_opcode[0]} in {resulting_codes}')
            delete_these.append(found_opcode)
        for found in delete_these:
            matching_opcodes.remove(found)

    # print(f'Resulting set is {matching_opcodes}')

    if len(matching_opcodes) == 1 and matching_opcodes[0][0] not in resulting_codes:
        # print(f'Adding {matching_opcodes[0][0]} = {matching_opcodes[0][1]}')
        resulting_codes[matching_opcodes[0][0]] = matching_opcodes[0][1]
    elif len(matching_opcodes) > 1:
        print(f'Unable to classify {matching_opcodes}')


opcode_list = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr
]

opcode_map = {}

filename = "day16_input.txt"
# filename = "day16_test_input.txt"
instructions = open(filename).readlines()

loop_counter = 1
while len(opcode_map) < 16 and loop_counter > 0:
    loop_counter -= 1
    i = 0
    while i < len(instructions):
        if instructions[i].startswith('Before'):
            compare_all_opcodes(opcode_map, opcode_list, instructions[i], instructions[i+1], instructions[i+2])
        i += 4

print(opcode_map)
