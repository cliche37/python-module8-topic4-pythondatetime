from datetime import timedelta
import datetime


def half_birthday(input_date):
    """half_birthday accepts an input date and calculates the date 6 months later.

    input_date parameter is passed into function and used to calculate date six months later.
    The input_date calculated future day, month, and year is saved into corresponding
    variables six_day, six_month, and six_year. If an exception is thrown for days not in
    calculated month, then the future month's last day is assumed to be the end of the month.


    :param input_date: the first date to be used to calculate date six months later
    :return: a string showing the date six months after input_date
    """

    six_day = input_date.day
    six_month = (input_date.month + 5) % 12 + 1
    six_year = input_date.year + ((input_date.month + 6) // 12)

    try:
        six_months_later = datetime.date(six_year, six_month, six_day)

    except ValueError:

        if (six_day == 2):

            if (six_day == 29):
                six_day -= 1

            elif (six_day == 30):
                six_day -= 2

            elif (six_day == 31):
                six_day -= 3

        else:
            six_day -= 1

        six_months_later = datetime.date(six_year, six_month, six_day)

    return str(six_months_later)