def get_input():
    with open("./input.txt") as f:
        input_lines = f.read().splitlines()
        
    return input_lines


def part1(input_lines):
    calories = []
    elf_calories = 0

    for line in input_lines:
        if line:
            elf_calories += int(line)
        else:
            calories.append(elf_calories)
            elf_calories = 0

    return max(calories)


def part2(input_lines):
    calories = []
    elf_calories = 0

    for line in input_lines:
        if line:
            elf_calories += int(line)
        else:
            calories.append(elf_calories)
            elf_calories = 0

    calories.sort()
    return sum(calories[-3:])


input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
