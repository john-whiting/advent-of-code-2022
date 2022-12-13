from typing import Union
from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 12)

class TreeNode():
    def __init__(self, coords: tuple[int, int], parent: Union["TreeNode", None]):
        self.coords = coords
        self.parent = parent

def get_height(char: str):
    return ord(char) - 97

def load_grid():
    lines = input_text.split('\n')[:-1]
    return [[get_height(col) for col in row] for row in lines]

def find_points_of_interest(grid: list[list[int]]) -> tuple[tuple[int, int], tuple[int, int], list[tuple[int, int]]]:
    start = None
    end = None
    naught_values = []
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            val = grid[row_idx][col_idx]
            if val == 0:
                naught_values += [(row_idx, col_idx)]
            if val == -14:
                # this is the start ord('S') - 97 = -14
                start = (row_idx, col_idx)
                naught_values += [start]
            if val == -28:
                # this is the start ord('E') - 97 = -28
                end = (row_idx, col_idx)
    return start, end, naught_values

def can_move(fro: int, to: int):
    return to - fro < 2

def get_value(grid: list[list[int]], coords: tuple[int, int]):
    if coords[0] < 0 or coords[0] >= len(grid):
        return -1 # Invalid Row
    if coords[1] < 0 or coords[1] >= len(grid[coords[0]]):
        return -1 # Invalid Column
    
    value = grid[coords[0]][coords[1]]
    
    if value == -14: # Start = elevation 0
        return 0
    
    if value == -28: # End = elevation 25
        return 25
    
    return value

def shortest_path(grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    # Shortest path using a BFS algorithm (up until we find the end and can stop)
    queue=[(-1, start)]
    visited: set[tuple[int, int]] = {start}
    tree_nodes: list[TreeNode] = []
    
    while len(queue) != 0:
        # Use BFS algorithm
        parent_idx, (row, col) = queue.pop(0)
        value = get_value(grid, (row, col))
        
        tree_nodes.append(TreeNode((row, col), tree_nodes[parent_idx] if parent_idx > -1 else None))
        node_idx = len(tree_nodes) - 1 # the idx of the current added tree node
        
        if (row, col) == end:
            # Stop BFS, we found our end
            break
        
        # Add children to queue
        up = (row, col - 1)
        down = (row, col + 1)
        left = (row - 1, col)
        right = (row + 1, col)
        
        for dir in [up, down, left, right]:
            if get_value(grid, dir) > -1 and can_move(value, get_value(grid, dir)) and not (dir in visited):
                queue += [(node_idx, dir)]
                visited.add(dir)
            
    # We ended BFS early, so we know the last node of the list is the end node
    # Trace it's parent tree to count the number of steps
    depth = 0
    cur_node = tree_nodes[-1]
    
    if cur_node.coords != end:
        return -1 # Never reached the end
    
    while cur_node.parent != None:
        depth += 1
        cur_node = cur_node.parent
        
    return depth


def process():
    grid = load_grid()
    
    part1_start, end, naught_values = find_points_of_interest(grid)
    
    part_1 = shortest_path(grid, part1_start, end)
    
    # Find the shortest valid path for any with a naught value
    part_2 = min(filter(lambda val: val > 0, [shortest_path(grid, start, end) for start in naught_values]))
    
    return part_1, part_2

def main():
    part_1, part_2 = process()
    print('Part 1', part_1)
    print('Part 2', part_2)
    
if __name__ == "__main__":
    main()