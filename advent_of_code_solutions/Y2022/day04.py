from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 4)

def make_list(str_range: str):
    first_num, second_num = str_range.split('-')
    first_num, second_num = int(first_num), int(second_num)
    return list(range(first_num, second_num + 1))

def fully_contains(partner1: list[int], partner2: list[int]):
    return all(e in partner2 for e in partner1) or all(e in partner1 for e in partner2)

def any_contains(partner1: list[int], partner2: list[int], checked_other = False):
    return any(e in partner2 for e in partner1) or any(e in partner1 for e in partner2)

def process():
    lines = input_text.split('\n')[:-1]
    
    all_count = 0
    any_count = 0
    
    for line in lines:
        str_range1, str_range2 = line.split(',')
        
        partner1 = make_list(str_range1)
        partner2 = make_list(str_range2)
        
        if fully_contains(partner1, partner2):
            all_count += 1
            
        if any_contains(partner1, partner2):
            any_count += 1
        
    return all_count, any_count

def main():
    part1, part2 = process()
    print('Part1:', part1)
    print('Part2:', part2)
    
if __name__ == "__main__":
    main()