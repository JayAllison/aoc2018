# register: 0,1,2,3
# opcode: xxxx
# instruction: opcode, input, input, output
# input can be immediate (use value given) or indirect (use value in given register)
# output is always a register (indirect)


def parse_instruction_string(instruction_string):
    # ex: 'seti 5 0 1'
    if instruction_string.startswith('#'):
        return None
    else:
        splits = instruction_string.split()
        return [splits[0], int(splits[1]), int(splits[2]), int(splits[3])]


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


opcodes = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}

test = False
if test:
    filename = "day19_test_input.txt"
    ir = 0
else:
    filename = "day19_input.txt"
    ir = 1

instructions = [parse_instruction_string(istr) for istr in open(filename).readlines() if not istr.startswith('#')]

part1 = False
if part1:
    the_registers = [0, 0, 0, 0, 0, 0]
else:
    the_registers = [1, 0, 0, 0, 0, 0]

loop_counter = 100_000_000_000
while the_registers[ir] < len(instructions) and loop_counter > 0:
    loop_counter -= 1
    actual_instruction = the_registers[ir]
    opcodes[instructions[actual_instruction][0]](the_registers, instructions[actual_instruction])
    # print(f'{actual_instruction}: {instructions[actual_instruction]} -> {the_registers}')
    the_registers[ir] += 1

if loop_counter:
    print(f'Reached the end of the program: IR = {the_registers[ir]}  Registers = {the_registers}')
else:
    print(f'ERROR! Loop counter reached before end of program.')
