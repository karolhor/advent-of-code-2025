import sys

def main(input_filename):
    rolls_map = read_input(input_filename)

    total_removed = 0
    while True:
        rolls_to_remove = analyze_map(rolls_map)
        remove_rolls(rolls_map, rolls_to_remove)
        total_removed += len(rolls_to_remove)

        if len(rolls_to_remove) == 0:
            print("Number of removed rolls:", total_removed)
            return

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        lines = [line.strip() for line in inp.readlines()]
        return [list(line) for line in lines]
    
def analyze_map(rolls_map):
    to_remove = []
    for i, row in enumerate(rolls_map):
        for j, item in enumerate(row):

            if item == '.':
                continue
            
            adj_rolls = count_adj_rolls(rolls_map, i, j)
            if adj_rolls < 4:
                to_remove.append([i,j])
    return to_remove

def count_adj_rolls(rolls_map, i, j):
    return sum([
        check_position(rolls_map, i-1, j-1),
        check_position(rolls_map, i, j-1),
        check_position(rolls_map, i+1, j-1),
        check_position(rolls_map, i-1, j),
        check_position(rolls_map, i+1, j),
        check_position(rolls_map, i-1, j+1),
        check_position(rolls_map, i, j+1),
        check_position(rolls_map, i+1, j+1),
    ])

def check_position(rolls_map, i, j):
    max_i = len(rolls_map[0])
    max_j = len(rolls_map)

    if i < 0 or j < 0 or i >= max_i or j >= max_j:
        return 0
    if rolls_map[i][j] == '@':
        return 1
    else:
        return 0
    
def remove_rolls(rolls_map, to_remove):
    for pos in to_remove:
        rolls_map[pos[0]][pos[1]] = '.'

if __name__ == '__main__':
    main(sys.argv[1])