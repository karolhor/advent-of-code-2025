import sys

def main(input_filename):
    battery_banks = read_input(input_filename)

    bank_joltages = calc_bank_joltages(battery_banks)
    total = sum(bank_joltages)
    
    print("The total value is:", total)

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return [line.strip() for line in inp.readlines()]

def calc_bank_joltages(battery_banks):
    return [calc_joltage(bank) for bank in battery_banks]

def calc_joltage(battery_bank):
    joltage = '00'
    last_index = len(battery_bank) - 1

    for i in range(len(battery_bank)):
        digit1 = int(joltage[0])
        digit2 = int(joltage[1])

        current = int(battery_bank[i])
        if current > digit1 and i != last_index:
            joltage = f"{current}0"
            continue
        if current > digit2:
            joltage = f"{digit1}{current}"

    return int(joltage)

if __name__ == '__main__':
    main(sys.argv[1])