"""
https://adventofcode.com/2021/day/1
"""

def find_day1_sonar_sweep_solution(data): 
    """Returns number of times depth measurement increases."""
    res, prev = 0, None
    for curr in data: 
        if prev and curr > prev: 
            res += 1
        prev = curr        
    return res