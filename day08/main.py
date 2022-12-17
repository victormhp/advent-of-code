def get_input():
    with open("./input.txt") as f:
        input = f.read().splitlines()
    return input


def part1(input):
    rows = [[int(n) for n in l] for l in input]
    
    perimeter = (len(rows) * 4) - 4
    visible = 0
    
    col = 1
    for i in range(1, len(rows) - 1):
        for j in range(1, len(rows[i]) - 1):
            columns = [x[j] for x in rows]
            
            left  = max(rows[i][:j])
            right = max(rows[i][j+1:])
            up    = max(columns[:col])
            down  = max(columns[col+1:])
            
            directions = [left, right, up, down]
            
            if any(direction < rows[i][j] for direction in directions):
                visible += 1
            
        col += 1

    return visible + perimeter
      
        
def part2(input):
    rows = [[int(n) for n in l] for l in input]
    directions = []
    nums  = []
    
    
    col = 1
    for i in range(1, len(rows) - 1):
        for j in range(1, len(rows[i]) - 1):
            columns = [x[j] for x in rows]
            
            left  = list(reversed(rows[i][:j]))
            right = rows[i][j+1:]
            up    = list(reversed(columns[:col]))
            down  = columns[col+1:]
            
            directions.append([left, right, up, down])
            nums.append(rows[i][j])       

        col += 1
    
    
    scenic_score = []
    view = []
    curr = 0
    for d in directions:
        n = nums[curr]
        
        for e in d:
            idx = next((i for i, elem in enumerate(e) if elem >= n), None)
            if idx != None:
                # print(len(e))
                view.append(idx + 1)
                
            else:
                # print(x + 1)
                view.append(len(e))

        curr += 1
        score = 1
        for v in view:
            score *= v
        scenic_score.append(score)
        
        view.clear()
    
    return max(scenic_score)

      

input = get_input()
print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")
