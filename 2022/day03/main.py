import string

def get_input():
    with open("./input.txt") as f:
        input_lines = f.read().splitlines()
    return input_lines

# String with all the lowercase and uppercase letters
letters = string.ascii_letters

def part1(input_lines):
    s = 0
    
    for i in input_lines:
        first = i[:len(i) // 2]
        second = i[len(i) // 2:]
         
        s += letters.index(''.join(sorted(set(first) & set(second), key = first.index))) + 1
    
    return s

def part2(input_lines):
    s = 0
    groupsOfThree = [input_lines[i:i+3] for i in range(0, len(input_lines), 3)]
    
    for i in groupsOfThree:
        s += letters.index(''.join(sorted( set(i[0]) & set(i[1]) & set(i[2]) ))) + 1
    
    return s
            
input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
