# tests/worklog.test_week.py
from unittest import TestCase, main
from worklog.week import Week

# JFMAYNLGSOVD

class TestWeek(TestCase):
    def test_without_parameters(self):
        week = Week()

        # week.year = 2020, for example
        self.assertEqual(type(week.year), int)

        # week.id = 'A1', for example
        self.assertEqual(type(week.id), str)
        self.assertEqual(len(week.id), 2)

    def test_with_year_and_date_provided(self):
        week = Week(2021, 1, 11)

        self.assertEqual(week.year, 2021)
        self.assertEqual(week.id, 'J2')
        self.assertEqual(week.dirname, '2021/02')

    def test_with_start_of_year_week(self):
        week = Week(2021, 1, 1)

        self.assertEqual(week.year, 2021)
        self.assertEqual(week.id, 'J0')
        self.assertEqual(week.dirname, '2021/00')

