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
        prev_dial = dial

        if direction == 'R':
            dial += rotation
            zero_count += dial // dial_numbers
            dial %= dial_numbers
        else:
            full_rotation_count = rotation // dial_numbers        
            zero_count += full_rotation_count
            rotation_left = rotation % dial_numbers
            dial -= rotation_left

            if prev_dial > 0 and dial <= 0:
                zero_count += 1
            
            dial %= dial_numbers
        

    return zero_count


if __name__ == '__main__':
    main(sys.argv[1])