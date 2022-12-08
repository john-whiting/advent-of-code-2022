from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 8)

def is_edge(width: int, height: int, row: int, col: int):
    return row % (height - 1) == 0 or col % (width - 1) == 0

def is_visible(grid: list[list[int]], width: int, height: int, row: int, col: int, value: int):
    if is_edge(width, height, row, col):
        return True
    
    # Check up direction
    if all(grid[row - i][col] < value for i in range(1, row + 1)):
        return True
    
    # Check down direction
    if all(grid[row + i][col] < value for i in range(1, height - row)):
        return True
    
    # Check left direction
    if all(grid[row][col - i] < value for i in range(1, col + 1)):
        return True
    
    # Check right direction
    if all(grid[row][col + i] < value for i in range(1, width - col)):
        return True
    
    return False

def get_scenic_score(grid: list[list[int]], width: int, height: int, row: int, col: int, value: int):
    if is_edge(width, height, row, col):
        return 0
    
    scenic_score = 1
    
    # Check up direction
    count_visible = 0
    for i in range(1, row + 1):
        check_value = grid[row - i][col]
        count_visible += 1
        if check_value >= value:
            break
    
    # Check down direction
    scenic_score *= count_visible
    count_visible = 0
    for i in range(1, height - row):
        check_value = grid[row + i][col]
        count_visible += 1
        if check_value >= value:
            break

    # Check left direction
    scenic_score *= count_visible
    count_visible = 0
    for i in range(1, col + 1):
        check_value = grid[row][col - i]
        count_visible += 1
        if check_value >= value:
            break
    

    # Check right direction
    scenic_score *= count_visible
    count_visible = 0
    for i in range(1, width - col):
        check_value = grid[row][col + i]
        count_visible += 1
        if check_value >= value:
            break
    
    scenic_score *= count_visible
    
    return scenic_score

def process():
    lines = input_text.split('\n')[:-1]
    
    grid = [[int(n) for n in line] for line in lines]
    
    width = len(grid[0])
    height = len(grid)
    
    visible_grid = [[is_visible(grid, width, height, row_idx, col_idx, value) for col_idx, value in enumerate(row)] for row_idx, row in enumerate(grid)]
    
    part1 = len(list(filter(lambda item: item, [item for sublist in visible_grid for item in sublist])))
    
    score_grid = [[get_scenic_score(grid, width, height, row_idx, col_idx, value) for col_idx, value in enumerate(row)] for row_idx, row in enumerate(grid)]
    
    part2 = max(list(filter(lambda item: item, [item for sublist in score_grid for item in sublist])))
    
    return part1, part2

def main():
    part1, part2 = process()
    
    print('Part 1:', part1)
    print('Part 2:', part2)
    
if __name__ == "__main__":
    main()