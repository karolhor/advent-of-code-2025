import sys

def main(input_filename):
    input = read_input(input_filename)
    instructions = parse_instructions(input)

    code = decode(instructions)

    print("The code is:", code)

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return inp.readlines()

def parse_instructions(input):
    return [(line[0], int(line[1:])) for line in input]    

def decode(instructions):
    dial = 50
    dial_numbers = 100
    zero_count = 0

    for step in instructions:
        direction = step[0]
        rotation = step[1]

        if direction == 'R':
            dial += rotation
        else:
            dial -= rotation

        dial %= dial_numbers

        if dial == 0:
            zero_count +=1

    return zero_count


if __name__ == '__main__':
    main(sys.argv[1])