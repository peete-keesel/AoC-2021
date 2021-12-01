from os import curdir
from scripts.utils import *
from scripts.day1_sonar_sweep import find_day1_sonar_sweep_solution


if __name__ == '__main__': 

    current_day = 1

    if current_day == 1:
        data_day1 = read_txt_file_into_list(PREFIX_PATH+DAY_1_DATA)
        res_day_1 = find_day1_sonar_sweep_solution(data_day1)
        print(res_day_1)

    count = 0
    for line in data_day1: 
        count += 1
    print(f"Total # of lines: {count}")



