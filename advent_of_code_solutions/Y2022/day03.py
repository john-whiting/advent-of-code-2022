from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 3)

def get_priority(c: str):
    if c.islower():
        return ord(c) - 96
    return ord(c) - 38

def part_1():
    priority_sum = 0
    for line in input_text.split('\n'):
        half = len(line) // 2
        first = line[:half]
        second = line[half:]
        
        for c in first:
            if c in second:
                priority_sum += get_priority(c)
                break
    return priority_sum

def part_2():
    priority_sum = 0
    lines = input_text.split('\n')
    for i in range(0, len(lines) - 1, 3):
        l1 = lines[i]
        l2 = lines[i + 1]
        l3 = lines[i + 2]
        
        for c in l1:
            if c in l2 and c in l3:
                priority_sum += get_priority(c)
                break
    return priority_sum
        
if __name__ == "__main__":
    print('Part 1:', part_1())
    print('Part 2:', part_2())