from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 10)

class Computer:
    def __init__(self, instructions: list[str]):
        self.instructions = instructions
        self.instruction_register = 0
        self.clock_register = 1
        self.register_x = 1
        
    def can_tick(self):
        return self.instruction_register < len(self.instructions) - 1
    
    def tick(self, halt_count = 0):
        instruction = self.instructions[self.instruction_register]
        
        op_code, *args = instruction.split(' ')
        
        should_halt = False
        
        if op_code == "noop":
            pass
        elif op_code == "addx":
            if halt_count > 0:
                value = int(args[0])
                self.register_x += value
            else:
                should_halt = True
        
        self.clock_register += 1
        
        if not should_halt:
            self.instruction_register += 1
            
        return should_halt

def process():
    computer = Computer(input_text.split('\n'))
    
    part_1 = 0
    part_2 = ""
    
    halt_count = 0
    while computer.can_tick():
        pixel = (computer.clock_register - 1) % 240
        pixel_x = pixel % 40
        
        if pixel_x == 0:
            part_2 += "\n"
        
        if abs(pixel_x - computer.register_x) < 2:
            part_2 += "#"
        else:
            part_2 += "."
        
        if not computer.tick(halt_count):
            halt_count = 0
        else:
            halt_count += 1
            
        if (computer.clock_register + 20) % 40 == 0:
            part_1 += computer.register_x * computer.clock_register
            
            
    return part_1, part_2

def main():
    part_1, part_2 = process()
    print('Part 1', part_1)
    print('Part 2', part_2)
    
if __name__ == "__main__":
    main()