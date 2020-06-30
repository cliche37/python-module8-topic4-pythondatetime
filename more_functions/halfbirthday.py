from datetime import timedelta
import datetime


def half_birthday(input_date):
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