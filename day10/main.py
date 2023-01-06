def get_input():
    with open("./input.txt") as f:
        input = f.read().splitlines()
    return input


def part1(input_lines):
    cycles = 0
    x = 1
    
    signals = {}
    singal_strengths = [20, 60, 100, 140, 180, 220]
    
    for l in input_lines:
        if l.startswith("a"):
            _, value = l.split(" ")
            
            cycles += 1
            signals[cycles] = x
            
            cycles += 1
            signals[cycles] = x
            
            x += int(value)
        else:
            cycles += 1
            signals[cycles] = x
    

    return sum(n * signals[n] for n in singal_strengths)
    
      
def part2(input_lines):
    cycles = 0
    x = 1
    
    signals = {}
    for l in input_lines:
        if l.startswith("a"):
            _, value = l.split(" ")
            
            cycles += 1
            signals[cycles] = x
            
            cycles += 1
            signals[cycles] = x
            
            x += int(value)
        else:
            cycles += 1
            signals[cycles] = x
    

    crt_row = ""
    next_line = 1
    for _, val in signals.items():
        if next_line > 40:
            crt_row += "\n"
            next_line = 1
            
        crt_row += "#" if next_line in range(val, val + 3) else "."
        next_line += 1
    
    return crt_row
    


input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2:\n{part2(input_lines)}")
