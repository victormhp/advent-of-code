def get_input():
    with open("./input.txt") as f:
        input_lines = f.read()
    return input_lines


def part1(input_lines):
    packet = []
    start_index = 0
    
    for i in range(4, len(input_lines) - 3):
        packet += input_lines[start_index:i]
        
        if len(packet) == len(set(packet)):
            return i
        else:
            packet = []
            start_index += 1

  
def part2(input_lines):
    packet = []
    start_index = 0
    
    for i in range(14, len(input_lines) - 3):
        packet += input_lines[start_index:i]
        
        if len(packet) == len(set(packet)):
            return i
        else:
            packet = []
            start_index += 1
      

input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
