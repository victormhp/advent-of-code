import string

def get_input():
    with open("./input.txt") as f:
        input = f.read().splitlines()
    return input

# String with all the lowercase and uppercase letters
letters = string.ascii_letters

def part1(input):
    s = 0
    
    for i in input:
        first = i[:len(i) // 2]
        second = i[len(i) // 2:]
         
        s += letters.index(''.join(sorted(set(first) & set(second), key = first.index))) + 1
    
    return s

def part2(input):
    s = 0
    groupsOfThree = [input[i:i+3] for i in range(0, len(input), 3)]
    
    for i in groupsOfThree:
        s += letters.index(''.join(sorted( set(i[0]) & set(i[1]) & set(i[2]) ))) + 1
    
    return s
            
input = get_input()
print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
