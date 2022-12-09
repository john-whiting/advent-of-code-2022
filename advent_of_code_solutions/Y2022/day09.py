from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 9)

vel_lookup = {
    "U": (1,  0),
    "D": (-1, 0),
    "L": (0, -1),
    "R": (0,  1),
}

def simulate_movement(positions: list[list[int, int]], vel: list[int, int]):
    positions[0][0] += vel[0]
    positions[0][1] += vel[1]
    
    for i in range(1, len(positions)):
        dx, dy = positions[i][0] - positions[i - 1][0], positions[i][1] - positions[i - 1][1]
        if abs(dx) >= 2 or abs(dy) >= 2:
            dx = max(-1, min(1, dx))
            dy = max(-1, min(1, dy))
            positions[i][0] -= dx
            positions[i][1] -= dy

def process():
    lines = input_text.split('\n')[:-1]
    # lines = input_text.split('\n')[0:6]
    
    part_1_cells_visited = { (0, 0) }
    part_1_positions = [[0, 0], [0, 0]]
    
    part_2_cells_visited = { (0, 0) }
    part_2_positions = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    
    for line in lines:
        direction, count = line.split(' ')
        count = int(count)
        
        vel = vel_lookup[direction]
                
        for i in range(count):
            simulate_movement(part_1_positions, vel)
            part_1_cells_visited.add(tuple(part_1_positions[-1]))
            simulate_movement(part_2_positions, vel)
            part_2_cells_visited.add(tuple(part_2_positions[-1]))
            
    print('Part 1:', len(part_1_cells_visited))
    print('Part 2:', len(part_2_cells_visited))

def main():
    process()
    
if __name__ == "__main__":
    main()