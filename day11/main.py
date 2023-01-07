from functools import reduce


def get_input():
    with open("./input.txt") as f:
        input = f.read().split("\n\n")
    return input


def part1(input_lines):
    def parse_monkey(lines): 
        _, items, op, div, t_true, t_false = lines.strip().split("\n")
        
        # Items list
        _, items = items.split(":")
        items = [int(i.strip()) for i in items.split(",")]

        # Operations
        _, op = op.split("=")
        op = op.strip()

        # Test
        div = int(div.split(" ")[-1])
        
        # Throws depending on test result
        t_true = int(t_true.split(" ")[-1])
        t_false = int(t_false.split(" ")[-1])

        return {
            "items": items,
            "op": lambda old: eval(op),
            "div": div,
            "t_true": t_true,
            "t_false": t_false,
            "inspections": 0
        }
    
    monkeys = list(map(parse_monkey, input_lines))
        
    for _ in range(20):
        for m in monkeys:
            for i in m["items"]:
                wl = m["op"](i) // 3
                target = m["t_true"] if wl % m["div"] == 0 else m["t_false"]
                
                monkeys[target]["items"].append(wl)
                m["inspections"] += 1
            m["items"].clear()
    
        
    first, second = sorted([m["inspections"] for m in monkeys], reverse=True)[:2]
    return first * second
    
      
def part2(input_lines):
    common_divisor = []
    def parse_monkey(lines): 
        _, items, op, div, t_true, t_false = lines.strip().split("\n")
        
        # Items list
        _, items = items.split(":")
        items = [int(i.strip()) for i in items.split(",")]

        # Operations
        _, op = op.split("=")
        op = op.strip()

        # Divisor
        div = int(div.split(" ")[-1])
        common_divisor.append(div)
        
        # Throws depending on test result
        t_true = int(t_true.split(" ")[-1])
        t_false = int(t_false.split(" ")[-1])

        return {
            "items": items,
            "op": lambda old: eval(op),
            "div": div,
            "t_true": t_true,
            "t_false": t_false,
            "inspections": 0
        }
    
    monkeys = list(map(parse_monkey, input_lines))
    D = reduce(lambda x, y: x * y, common_divisor)
    
    for _ in range(10000):
        for m in monkeys:
            for i in m["items"]:
                wl = m["op"](i) % D
                target = m["t_true"] if wl % m["div"] == 0 else m["t_false"]
                
                monkeys[target]["items"].append(wl)
                m["inspections"] += 1
            m["items"].clear()
    
        
    first, second = sorted([m["inspections"] for m in monkeys], reverse=True)[:2]
    return first * second
    

input_lines = get_input()
print(f"Part 1: {part1(input_lines)}")
print(f"Part 2: {part2(input_lines)}")
