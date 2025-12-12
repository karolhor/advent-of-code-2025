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
    max_size = 12
    joltage = [0] * max_size

    for bank_idx in range(len(battery_bank)):
        current = int(battery_bank[bank_idx])

        joltage_min_digit_idx = max_size - len(battery_bank[bank_idx:])
        if joltage_min_digit_idx < 0:
            joltage_min_digit_idx = 0

        for i  in range(joltage_min_digit_idx, len(joltage)):
            idx_value = joltage[i]
            if current > idx_value:
                joltage[i] = current
                _reset_list_part(joltage, i+1)
                break


    return int(''.join([str(i) for i in joltage]))

def _reset_list_part(l, start_idx):
    if start_idx == len(l):
        return
    for i in range(start_idx, len(l)):
        l[i] = 0

if __name__ == '__main__':
    main(sys.argv[1])