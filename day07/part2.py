import sys
from collections import defaultdict


def main(input_filename):
    diagram = read_input(input_filename)

    result = calculate(diagram)
    print("The beam splitted n-times:", result)


def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return [list(line.strip()) for line in inp.readlines()]


def calculate(diagram):
    beams_counter = defaultdict(int)
    start_index = diagram[0].index('S')
    beams_counter[start_index] = 1
    diagram[1][start_index] = '|'
    diagram.pop(0)

    for row_idx, line in enumerate(diagram):
        for col_idx, item in enumerate(line):
            item = diagram[row_idx][col_idx]

            if item == '^':
                if beams_counter[col_idx] > 0:
                    beams_counter[col_idx - 1] = beams_counter[col_idx - 1] + beams_counter[col_idx]
                    beams_counter[col_idx + 1] = beams_counter[col_idx + 1] + beams_counter[col_idx]
                    beams_counter[col_idx] = 0

    return sum(beams_counter.values())


if __name__ == '__main__':
    main(sys.argv[1])