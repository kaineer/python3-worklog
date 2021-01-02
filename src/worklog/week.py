from datetime import date

MONTHS_UNIQ_LETTERS = 'JFMAYNLGSOVD'

def week_id(month, week_number):
    return ''.join(list(map(str, [
        MONTHS_UNIQ_LETTERS[month - 1],
        week_number % 10
    ])))

class Week:
    def __init__(self,
            year = date.today().year,
            month = date.today().month,
            day = date.today().day):
        t = date(year, month, day)
        self.year = year
        week_number = t.isocalendar()[1]
        # No worklogging on holydays
        if week_number > 52:
            week_number = 0
        self.id = week_id(month, week_number)
        self.dirname = f"{year}/{week_number:02d}"
