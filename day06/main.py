def get_input():
    with open("./input.txt") as f:
        input = f.read()
    return input


def part1(input):
    packet = []
    start_index = 0
    
    for i in range(4, len(input) - 3):
        packet += input[start_index:i]
        
        if len(packet) == len(set(packet)):
            return i
        else:
            packet = []
            start_index += 1

  
def part2(input):
    packet = []
    start_index = 0
    
    for i in range(14, len(input) - 3):
        packet += input[start_index:i]
        
        if len(packet) == len(set(packet)):
            return i
        else:
            packet = []
            start_index += 1
      

input = get_input()
print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
