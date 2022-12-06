import sys
from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 6)

sys.setrecursionlimit(500000)

def find_start_of_packet(buffer: str, prev_chars: list[int], count: int = 3, necessary_distinct = 3):
    print(prev_chars)
    if buffer[count] in prev_chars or len(set(prev_chars)) != necessary_distinct:
        return find_start_of_packet(buffer, prev_chars[1:] + [buffer[count]], count + 1, necessary_distinct)
    return count

def process():
    part1 = find_start_of_packet(input_text, prev_chars=list(input_text[:3]))
    part2 = find_start_of_packet(input_text, prev_chars=list(input_text[:13]), count = 13, necessary_distinct=13)
    return part1 + 1, part2 + 1

def main():
    part1, part2 = process()
    print('Part 1:', part1)
    print('Part 2:', part2)
    
if __name__ == "__main__":
    main()