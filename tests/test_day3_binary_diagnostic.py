from src.scripts.utils import *
from src.scripts.day3_binary_diagnostic import (
    find_day3_binary_diagnostic_solution_part_1,
    find_day3_binary_diagnostic_solution_part_2
)
import unittest


class TestDay3BinaryDiagnostic(unittest.TestCase): 
    def test_find_day3_binary_diagnostic_solution_part_1(self): 
        res = find_day3_binary_diagnostic_solution_part_1(
            read_txt_file_into_list('test_resources/testfile_day3_binary_diagnostic.txt', 3)
        )

        self.assertEquals(res, 198)

    def test_find_day3_binary_diagnostic_solution_part_2(self): 
        res = find_day3_binary_diagnostic_solution_part_2(
            read_txt_file_into_list('test_resources/testfile_day3_binary_diagnostic.txt', 3)
        )

        self.assertEquals(res, 230)