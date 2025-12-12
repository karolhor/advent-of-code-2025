import sys

def main(input_filename):
    diagram = read_input(input_filename)

    result = calculate(diagram)
    print("The beam splitted n-times:", result)

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return [list(line.strip()) for line in inp.readlines()]

def calculate(diagram):
    start_index = diagram[0].index('S')
    diagram[1][start_index] = '|'
    diagram.pop(0)
    last_row_idx = len(diagram) - 1
    result = 0

    for row_idx, line in enumerate(diagram):
        for col_idx, item in enumerate(line):
            if item != '|':
                continue
            
            next_row_idx = row_idx + 1
            if next_row_idx == last_row_idx:
                break

            next_pos = diagram[next_row_idx][col_idx]

            if next_pos == '^':                  
                result += 1
                diagram[next_row_idx][col_idx-1] = '|'
                diagram[next_row_idx][col_idx+1] = '|'
            else:
                diagram[next_row_idx][col_idx] = '|'
                next_row_idx += 1

    return result

def print_diagram(diagram):
    for line in diagram:
        print(''.join(line))

if __name__ == '__main__':
    main(sys.argv[1])