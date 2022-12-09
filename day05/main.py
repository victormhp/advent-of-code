def get_input():
    with open("./input.txt") as f:
        input = f.read()
    return input


def part1(input):
    boxes, movements = input.split("\n\n")
    
    letters = []
    for line in boxes.split("\n"):
        letters.append([line[i:i+3] for i in range(0, len(line), 4)])

    columns = [col[::-1] for col in map(list, zip(*letters))]
    columns = [list(filter(lambda x: x != "   ", col)) for col in columns]

    for move in movements.split("\n"):
        x, y, z = [int(i) for i in move.split() if i.isdigit()]
        
        m = columns[y-1][-x:]
        columns[y-1][-x:] = []
        columns[z-1].extend(m[::-1])     
    

    last = [x[-1].replace("[","").replace("]","") for x in columns]
    return "".join(last)

    
      
        
def part2(input):
    boxes, movements = input.split("\n\n")
    
    letters = []
    for line in boxes.split("\n"):
        letters.append([line[i:i+3] for i in range(0, len(line), 4)])

    columns = [col[::-1] for col in map(list, zip(*letters))]
    columns = [list(filter(lambda x: x != "   ", col)) for col in columns]

    for move in movements.split("\n"):
        x, y, z = [int(i) for i in move.split() if i.isdigit()]
        
        m = columns[y-1][-x:]
        columns[y-1][-x:] = []
        columns[z-1].extend(m) # Only removed the [::-1] that reversed the list order xD.    
    

    last = [x[-1].replace("[","").replace("]","") for x in columns]
    return "".join(last)
   
            
input = get_input()
print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
