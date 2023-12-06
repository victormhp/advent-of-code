def get_input():
    with open("./input.txt") as f:
        input_lines = f.read().splitlines()
    return input_lines


def part1(input_lines):
    count = 0
    for i in input_lines:
        a, b = i.split(",")
        n1, n2 = map(int, a.split("-"))
        n3, n4 = map(int, b.split("-"))
        
        r1 = set(range(n1, n2 + 1))
        r2 = set(range(n3, n4 + 1))
        
        if r1 >= r2 or r1 <= r2:
            count += 1
            
    return count
        
        
def part2(input_lines):
    count = 0
    for i in input_lines:
        a, b = i.split(",")
        n1, n2 = map(int, a.split("-"))
        n3, n4 = map(int, b.split("-"))
        
        r1 = set(range(n1, n2 + 1))
        r2 = set(range(n3, n4 + 1))
        
        if r1.intersection(r2):
            count += 1
            
    return count
   
            
input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
