import sys
from collections import namedtuple

Range = namedtuple('Range', ['start', 'end'])

def main(input_filename):
    lines = read_input(input_filename)
    fresh_ranges = parse_db(lines)
    
    all_fresh_number = count_all_fresh_ids(fresh_ranges)
    print("Number of total fresh ids:", all_fresh_number)

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return [line.strip() for line in inp.readlines()]
    
def parse_db(lines):
    ranges = []
        
    for line in lines:
        if line == '':
            break

        fresh_range = line.split('-')
        ranges.append(Range(int(fresh_range[0]), int(fresh_range[1])))

    return ranges

def count_all_fresh_ids(fresh_ranges):
    sorted_ranges = sorted(list(fresh_ranges), key=lambda fr: fr.start)
    merged_ranges = merge_ranges(sorted_ranges)
    
    return count_by_ranges(merged_ranges)

def merge_ranges(ranges):
    current_idx = 1
    result = [ranges[0]]
    for current_idx in range(1, len(ranges)):
        last_added = result[-1]
        current_range = ranges[current_idx]
        prev_start = last_added.start
        prev_end = last_added.end        
        start = current_range.start
        end = current_range.end

        if prev_end >= start:
            if end < prev_end:
                continue
            prev_end = end
            result[-1] = Range(prev_start, prev_end)
        else:
            result.append(current_range)
    
    return result

def count_by_ranges(ranges):
    total = 0
    for fresh_range in ranges:
        total += fresh_range.end - fresh_range.start + 1

    return total

def print_ranges(ranges):
    for r in ranges:
        print(f"{r.start}-{r.end}")


if __name__ == '__main__':
    main(sys.argv[1])