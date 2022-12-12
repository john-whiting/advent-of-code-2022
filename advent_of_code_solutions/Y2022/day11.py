from math import lcm
from tqdm import tqdm
from typing import Callable

class Monkey:
    def __init__(self, divide_by_three: bool, common_factor: int, starting_inventory: list[int], operation: Callable[[int], int], test_action: Callable[[int], int]):
        """Creates a monkey that performs the given test_action.

        Args:
            starting_inventory (list[int]): The list of worry levels for starting items
            test_action (Callable[[int], int]): The input is the current worry level of an item
                and it returns the int of the new worry level of the item
            test_action (Callable[[int], int]): The input is the current worry level of an item
                and it returns the int of the next monkey to throw it to 
        """
        self.inventory = starting_inventory
        self.inspection_count = 0
        self.operation = operation
        self.test_action = test_action
        
        self.common_factor = common_factor
        self.divide_by_three = divide_by_three
        
    def inspect_item(self, old_worry_level: int):
        self.inspection_count += 1
        
        # get the new worry level (mod it by a common factor)
        worry_level = (self.operation(old_worry_level)) % self.common_factor
        if self.divide_by_three:
            worry_level //= 3
        
        # return where the item should move and what the new worry level is
        return self.test_action(worry_level), worry_level
        
    def take_turn(self):
        # list of new monkeys for items to move to as a:
        # tuple with 0th index being the new monkey,
        # and the 1st index being the worry value
        where_to_move = [self.inspect_item(old_worry_level) for old_worry_level in self.inventory]
        
        # Clear inventory, since the monkey always throws all the items
        self.inventory = []
        
        return where_to_move
    
    def add_item(self, item_worry: int):
        self.inventory += [item_worry]

def process_part(round_count: int, divide_by_three = False):
    common_factor = lcm(5, 2, 19, 7, 17, 13, 3, 11)
    
    # define our monkeys
    monkeys = [
        Monkey(divide_by_three, common_factor, [98, 89, 52],                        lambda old_worry: old_worry * 2,            lambda worry: 6 if worry % 5  == 0 else 1),
        Monkey(divide_by_three, common_factor, [57, 95, 80, 92, 57, 78],            lambda old_worry: old_worry * 13,           lambda worry: 2 if worry % 2  == 0 else 6),
        Monkey(divide_by_three, common_factor, [82, 74, 97, 75, 51, 92, 83],        lambda old_worry: old_worry + 5,            lambda worry: 7 if worry % 19 == 0 else 5),
        Monkey(divide_by_three, common_factor, [97, 88, 51, 68, 76],                lambda old_worry: old_worry + 6,            lambda worry: 0 if worry % 7  == 0 else 4),
        Monkey(divide_by_three, common_factor, [63],                                lambda old_worry: old_worry + 1,            lambda worry: 0 if worry % 17 == 0 else 1),
        Monkey(divide_by_three, common_factor, [94, 91, 51, 63],                    lambda old_worry: old_worry + 4,            lambda worry: 4 if worry % 13 == 0 else 3),
        Monkey(divide_by_three, common_factor, [61, 54, 94, 71, 74, 68, 98, 83],    lambda old_worry: old_worry + 2,            lambda worry: 2 if worry % 3  == 0 else 7),
        Monkey(divide_by_three, common_factor, [90, 56],                            lambda old_worry: old_worry * old_worry,    lambda worry: 3 if worry % 11 == 0 else 5),
    ]

    # Go through each round
    for round in tqdm(range(round_count)):
        # Process each monkey in turn
        for monkey in monkeys:
            # Redistribute the items
            for monkey_idx, worry_level in monkey.take_turn():
                monkeys[monkey_idx].add_item(worry_level)
                
    inspected_list = sorted(monkeys, key=lambda monkey: monkey.inspection_count, reverse=True)
    result = inspected_list[0].inspection_count * inspected_list[1].inspection_count
    
    return result

def main():
    part_1 = process_part(20, True)
    part_2 = process_part(10000)
    
    print('Part 1', part_1)
    print('Part 2', part_2)

if __name__ == "__main__":
    main()