import datetime as dt


def get_today():
    date_now = dt.datetime.today().strftime('%A, %d %B %Y, %I:%M%p')
    return date_now
