import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for name_function.py """

    def test_first_last_name(self):
        """ Do names like Prashanth Pradeep work?"""
        fromatted_name = get_formatted_name("prashanth", "pradeep")
        self.assertEqual(fromatted_name, "Prashanth Pradeep")

    def test_first_middle_last_name(self):
        """ Do names like pandit jawaharlal nehru work?"""

        fromatted_name = get_formatted_name(
            first="pandit", middle="jawaharlal", last="nehru")
        print(fromatted_name)
        self.assertEqual(fromatted_name, "Pandit Jawaharlal Nehru")


if __name__ == '__main__':
    unittest.main()
