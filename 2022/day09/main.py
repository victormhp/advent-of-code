def get_input():
    with open("./input.txt") as f:
        input_lines = f.read().splitlines()
    return input_lines

# How the position changes for each direction. Save them in a dict instead of having to check them with conditionals.
DIRECTIONS = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

def part1(input_lines):
    visited = set()
    visited.add((0, 0))
    
    hx, hy = 0, 0
    tx, ty = 0, 0
    
    for l in input_lines:
        d, s = l.split()
        dx, dy = DIRECTIONS[d]
        
        for _ in range(int(s)):
            hx += dx
            hy += dy

            if not(abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
                sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)
                
                tx += sign_x
                ty += sign_y

            visited.add((ty, tx))
        
    return len(visited)
      
        
def part2(input_lines):
    knots = [[0, 0] for _ in range(10)]
    
    visited = set()
    visited.add(tuple(knots[-1]))
    
    for l in input_lines:
        d, s = l.split()
        dx, dy = DIRECTIONS[d]
        
        for _ in range(int(s)):
            knots[0][0] += dx
            knots[0][1] += dy
            
            for i in range(1, 10):
                hx, hy = knots[i - 1]
                tx, ty = knots[i]

                if not(abs(hx - tx) <= 1 and abs(hy - ty) <= 1):
                    sign_x = 0 if hx == tx else (hx - tx) / abs(hx - tx)
                    sign_y = 0 if hy == ty else (hy - ty) / abs(hy - ty)

                    tx += sign_x
                    ty += sign_y
                    
                knots[i] = [tx, ty]

            visited.add(tuple(knots[-1]))
        
    return len(visited)

      

input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
