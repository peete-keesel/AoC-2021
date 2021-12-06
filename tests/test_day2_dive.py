from src.scripts.utils import *
from src.scripts.day2_dive import (
    find_day2_dive_solution_part_1,
    find_day2_dive_solution_part_2
)
import unittest


class TestDay2Dive(unittest.TestCase): 
    def test_find_day2_dive_solution_part_1(self): 
        res = find_day2_dive_solution_part_1(
            read_txt_file_into_list('test_resources/testfile_day2_dive.txt', 2)
        )

        self.assertEquals(res, 150)

    def test_find_day2_dive_solution_part_2(self): 
        res = find_day2_dive_solution_part_2(
            read_txt_file_into_list('test_resources/testfile_day2_dive.txt', 2)
        )

        self.assertEquals(res, 900)