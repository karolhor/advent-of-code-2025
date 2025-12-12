import sys
from functools import reduce
import operator

def main(input_filename):
    lines = read_input(input_filename)
    matrix = read_matrix(lines)
    arguments = convert_matrix(matrix)

    result = calculate(arguments)

    print("The result is:", result)

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return inp.readlines()

def read_matrix(lines):
    return [ list(line) for line in lines ] 

def convert_matrix(matrix):
    operations_line = matrix.pop()
    cols_number = len(matrix)

    arguments = []
    operation_numbers = []
    for i in reversed(range(0, len(operations_line))):
        op = operations_line[i]
        col_start = False
        if op != ' ':
            col_start = True
    
        number = ''
        for row_idx in range(cols_number):
            digit = matrix[row_idx][i]
            if digit != ' ':
                number += digit
        
        if number != '':
            operation_numbers.append(number)

        if col_start:
            arguments.append(operation_numbers + [op])
            operation_numbers = []
        
    return arguments

def calculate(all_arguments):
    total = 0
    for arguments in all_arguments:
        operation = arguments.pop()
        numbers = extract_numbers(arguments)

        if operation == '+':
            operation_func = operator.add
        else: 
            operation_func = operator.mul

        total += reduce(operation_func, numbers)
    
    return total

def extract_numbers(args):
    return [int(a) for a in args]
        

if __name__ == '__main__':
    main(sys.argv[1])