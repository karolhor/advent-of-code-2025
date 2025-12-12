import sys
from collections import namedtuple

Range = namedtuple('Range', ['start', 'end'])
IngredientsDB = namedtuple('IngredientsDB', ['ranges', 'ingredient_ids'])

def main(input_filename):
    lines = read_input(input_filename)
    db = parse_db(lines)
    
    fresh_ids = filter_fresh_ingredient(db)
    print("Number of fresh ids:", len(fresh_ids))

def read_input(input_filename):
    with open(input_filename, 'r') as inp:
        return [line.strip() for line in inp.readlines()]
    
def parse_db(lines):
    ranges = []
    ingredient_ids = []
    
    next_section = False
    for line in lines:
        if line == '':
            next_section = True
            continue

        if not next_section:
            range = line.split('-')
            ranges.append(Range(int(range[0]), int(range[1])))
        else:
            ingredient_ids.append(int(line))

    return IngredientsDB(ranges, ingredient_ids)

def filter_fresh_ingredient(db):
    return [ingredient_id for ingredient_id in db.ingredient_ids \
            if is_fresh(db.ranges, ingredient_id)]

def is_fresh(ranges, ingredient_id):
    for range in ranges:
        if ingredient_id >= range.start and ingredient_id <= range.end:
            return True
    return False
        

if __name__ == '__main__':
    main(sys.argv[1])