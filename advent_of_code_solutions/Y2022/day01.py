from advent_of_code_solutions.utils import get_input_file

input_text = get_input_file(2022, 1)

def main():
    # Separate the elves
    elves = input_text.split('\n\n')
    
    # Convert the elves strings into number arrays
    elves = [[int(s or '0') for s in elf.split('\n')] for elf in elves]
    
    # Get the total calories of each elf
    elf_sums = [sum(elf) for elf in elves]
    # Sort the number of calories
    elf_sums.sort()
    
    # Print the largest number, and the sum of the top three
    print('Largest Number of Calories:', elf_sums[-1])
    print('Sum of the top 3 largest:', sum(elf_sums[-3:]))
    pass
    
if __name__ == "__main__":
    main()