from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 2)

lookup = {
    'A': 0, # Opponent -> Rock
    'B': 1, # Opponent -> Paper
    'C': 2, # Opponent -> Scissors
    'X': 0, # Me -> Rock
    'Y': 1, # Me -> Paper
    'Z': 2, # Me -> Scissors
}

def get_winning_value(base: int):
    return (base + 1) % 3

def get_losing_value(base: int):
    return (base - 1) % 3

def process_line(line: str):
    return tuple(lookup[k] for k in line.split(' '))

def get_part2_score(op_score: int, outcome: int):
    if outcome == 0: # Me should lose
        return get_losing_value(op_score)
    if outcome == 1: # Me should tie
        return op_score
    # Me should win
    return get_winning_value(op_score)

def calculate_total_score(rounds: list[tuple[int, int]]):
    total_score = 0
    
    for round in rounds:
        op, me = round # Round should be a tuple of ints in range [0, 2]
        
        total_score += me + 1 # Points that "me" always gets
        
        win_value = get_winning_value(op)
        
        if op == me: # Tie
            total_score += 3
        elif me == win_value: # Win
            total_score += 6
            
    return total_score

def main():
    # Read in the data (ignoring last empty line)
    rounds = input_text.split('\n')[:-1]
    # Change data into int tuple
    rounds = [process_line(round) for round in rounds]
    
    rounds_part2 = [(op, get_part2_score(op, outcome)) for op, outcome in rounds]
    
    # Run calculations
    return calculate_total_score(rounds), calculate_total_score(rounds_part2)
    
if __name__ == "__main__":
    part1, part2 = main()
    print('Part1:', part1)
    print('Part2:', part2)
