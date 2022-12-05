import copy
from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 5)

starting_positions = [
    ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
    ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
    ['C', 'B', 'S', 'N', 'W'],
    ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
    ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
    ['J', 'V', 'T', 'W', 'M', 'N'],
    ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
    ['B', 'D', 'Z'],
    ['M', 'N', 'Z', 'W'],
]

def process():
    positions1 = copy.deepcopy(starting_positions)
    positions2 = copy.deepcopy(starting_positions)
    actions = input_text.split('\n')[10:-1]
    
    for action in actions:
        action = action[5:] # remove "move"
        count, action = action.split(" from ")
        from_num, to_num = action.split(" to ")
        
        count, from_num, to_num = int(count), int(from_num) - 1, int(to_num) - 1
        
        # Move all the "count" from the "from" to the "to"
        positions2[to_num].extend(positions2[from_num][-count:])
        
        for i in range(count):
            positions1[to_num].append(positions1[from_num].pop()) # Move one at a time
            positions2[from_num].pop() # Remove from the "from" stack
            
    return ''.join(stack[-1] for stack in positions1), ''.join(stack[-1] for stack in positions2)

def main():
    part1, part2 = process()
    print("Part 1:", part1)
    print("Part 2:", part2)
    
if __name__ == "__main__":
    main()