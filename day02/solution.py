import sys

def main(input_filename):
    input = read_input(input_filename)
    id_ranges = parse_input(input)

    invalid_ids = find_all_invalid_ids(id_ranges)
    code = sum(invalid_ids)
    
    print("The code is:", code)

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return inp.readline()
    
def parse_input(input):
    return [ id_range.split('-') for id_range in input.split(',')]

def find_all_invalid_ids(id_ranges):
    invalid_ids = []
    for id_range in id_ranges:
        left = id_range[0]
        right = id_range[1]
        invalid_ids.extend(find_invalid_ids_by_range(left, right))
    return invalid_ids

def find_invalid_ids_by_range(left, right):
    invalid_ids = []
    for i in range(int(left), int(right)+1):
        product_id = str(i)
        pivot = len(product_id) // 2

        id_part_left = product_id[0:pivot]
        id_part_right = product_id[pivot:]

        if id_part_left == id_part_right:
            invalid_ids.append(i)

    return invalid_ids




if __name__ == '__main__':
    main(sys.argv[1])