from os import curdir
from scripts.utils import *
from scripts.day1_sonar_sweep import (
    find_day1_sonar_sweep_solution_part_1,
    find_day1_sonar_sweep_solution_part_2
)
from scripts.day2_dive import (
    find_day2_dive_solution_part_1,
    find_day2_dive_solution_part_2
)


if __name__ == '__main__': 

    day, part = 2, 2
    res = None

    if day == 1:
        data = read_txt_file_into_list(PREFIX_PATH+DAY_1_DATA, day=1)
        if part == 1: res = find_day1_sonar_sweep_solution_part_1(data)
        elif part == 2: res = find_day1_sonar_sweep_solution_part_2(data)
    elif day == 2: 
        data = read_txt_file_into_list(PREFIX_PATH+DAY_2_DATA, day=2)
        if part == 1: res = find_day2_dive_solution_part_1(data)
        elif part == 2: res = find_day2_dive_solution_part_2(data)

    print(f"The results for day {day} part {part} is: {res}")

    count = 0
    for line in data: 
        count += 1
    print(f"Total # of lines: {count}")



