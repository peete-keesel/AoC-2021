from os import curdir
from scripts.utils import *
from scripts.day1_sonar_sweep import (
    find_day1_sonar_sweep_solution_part_1,
    find_day1_sonar_sweep_solution_part_2
)


if __name__ == '__main__': 

    day, part = 1, 2

    if day == 1:
        data_day1 = read_txt_file_into_list(PREFIX_PATH+DAY_1_DATA)
        if part == 1: 
            res_day_1 = find_day1_sonar_sweep_solution_part_1(data_day1)
            print(res_day_1)
        elif part == 2: 
            res_day_1_part_2 = find_day1_sonar_sweep_solution_part_2(data_day1)
            print(res_day_1_part_2)

    count = 0
    for line in data_day1: 
        count += 1
    print(f"Total # of lines: {count}")



