from src.scripts.utils import *
from src.scripts.day1_sonar_sweep import find_day1_sonar_sweep_solution

import unittest


class TestDay1SonarSweep(unittest.TestCase): 
    def test_find_day1_sonar_sweep_solution(self): 
        res = find_day1_sonar_sweep_solution(
            read_txt_file_into_list('test_resources/testfile_day1_sonar_sweep.txt')
        )

        self.assertEquals(
            res, 
            7
        )