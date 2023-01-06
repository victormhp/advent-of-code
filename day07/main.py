def get_input():
    with open("./input.txt") as f:
        input_lines = f.read().splitlines()
    return input_lines


def part1(input_lines):
    size = 100000
    total = 0
    
    stack = [["/", 0]]
    for line in input_lines:
        if line == "$ cd /" or line == "$ ls":
            continue
        
        if line.startswith("$ cd"):
            dir = line[5:]
            if dir == "..":
                [_, amount] = stack.pop()
                if amount <= size:
                    total += amount
                stack[-1][1] += amount
            else:
                stack.append([dir, 0])
            continue
        
        [amount, name] = line.split(" ")
        if amount.isdigit(): 
            stack[-1][1] += int(amount)

    return total
    
        
def part2(input_lines):
    total_space = 70000000
    update_space = 30000000
    
    stack = [["/", 0]]
    complete_stack = []
    for line in input_lines:
        if line == "$ cd /" or line == "$ ls":
            continue
        
        if line.startswith("$ cd"):
            dir = line[5:]
            if dir == "..":
                [name, amount] = stack.pop()
                stack[-1][1] += amount
                complete_stack.append([name, amount])
            else:
                stack.append([dir, 0])
            continue
        
        [amount, name] = line.split(" ")
        if amount.isdigit(): 
            stack[-1][1] += int(amount)
    
    for i, [n, a] in enumerate(stack):
        complete_stack.append([n, a])
        if i < len(stack) - 1:
            stack[i + 1][1] += a
     
    unused = total_space - complete_stack[-1][1]
    required_space = update_space - unused
    
    return min([dir[1] for dir in complete_stack if dir[1] >= required_space])    
      

input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
