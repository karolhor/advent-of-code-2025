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
        return [line.strip() for line in inp.readlines()]

def read_matrix(lines):
    return [ line.split() for line in lines ] 

def convert_matrix(matrix):
    nb_cols = len(matrix[0])
    arguments = []
    for i in range(nb_cols):
        arg = []
        for j in range(len(matrix)):
            arg.append(matrix[j][i])
        
        arguments.append(arg)
    
    return arguments

def calculate(all_arguments):
    total = 0
    for arguments in all_arguments:
        operation = arguments.pop()
        numbers = [int(a) for a in arguments]

        if operation == '+':
            operation_func = operator.add
        else: 
            operation_func = operator.mul

        total += reduce(operation_func, numbers)
    
    return total

        

if __name__ == '__main__':
    main(sys.argv[1])