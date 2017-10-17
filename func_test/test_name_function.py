import unittest
from func_test.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('alex', 'gui')
        self.assertEqual(formatted_name, "Alex Gui")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('alex', 'wang', 'gui')
        self.assertEqual(formatted_name, 'Alex Gui Wang')
