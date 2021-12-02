"""
https://adventofcode.com/2021/day/2
"""

DEPTH = ['increases', 'decreases']
HORIZ = ['forward']

def find_day2_dive_solution_part_1(data): 
    directions, units = data[0], data[1]
    horiz, depth = 0, 0
    for i, d in enumerate(directions): 
        if d == 'forward': horiz += units[i]
        elif d == 'down': depth += units[i]
        elif d == 'up': depth -= units[i]
        else: return NotImplementedError

    return horiz*depth

def find_day2_dive_solution_part_2(data): 
    directions, units = data[0], data[1]
    horiz, depth, aim = 0, 0, 0
    for i, d in enumerate(directions): 
        if d == 'forward': 
            horiz += units[i]
            depth += aim*units[i]
        elif d == 'down': aim += units[i]
        elif d == 'up': aim -= units[i]
        else: return NotImplementedError

    return horiz*depth