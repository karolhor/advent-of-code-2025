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

        min_seq_length = 1
        for seq_length in range(min_seq_length, pivot+1):
            parts = [ product_id[i:i + seq_length] for i in range(0, len(product_id), seq_length) ]
            unique_parts = set(parts)
            if len(unique_parts) == 1:
                invalid_ids.append(int(product_id))
                break

    return invalid_ids




if __name__ == '__main__':
    main(sys.argv[1])