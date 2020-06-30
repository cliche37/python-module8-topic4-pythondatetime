import unittest
import datetime
from datetime import timedelta

from more_functions.halfbirthday import half_birthday


class FunctionTest(unittest.TestCase):

    def test_half_birthday(self):

        recent_birthday = datetime.datetime(2020, 5, 31)

        self.assertEqual("2020-11-30", half_birthday(recent_birthday))


if __name__ == "__main__":
    unittest.main()