"""
https://adventofcode.com/2021/day/1
"""

def find_day1_sonar_sweep_solution_part_1(data): 
    """Returns number of times depth measurement increases."""
    res, prev = 0, None
    for curr in data: 
        if prev and curr > prev: 
            res += 1
        prev = curr        
    return res

def find_day1_sonar_sweep_solution_part_2(data): 
    """Returns number of times the sum of measurements in a
    three-measurement sliding window increases."""

    res = 0
    window = [0, 0, 0]
    prev_sum = None

    for x in data: 
        window.append(x)
        window = window[1:]
        if 0 not in window: 
            curr_sum = window[-3] + window[-2] + window[-1]
            if prev_sum and curr_sum > prev_sum:
                res += 1
            #print(f"{x}: {curr_sum} ({res})")
            prev_sum = curr_sum

    return res 