import time


def get_current_date(df):
    last_date = df['time'].tolist()[-1]
    return last_date


def add_date(date, plus_time):
    prev_d = time.strptime(date, '%Y-%m-%d %X')
    prev_d = time.mktime(prev_d)
    next_d = prev_d + plus_time
    next_d = time.localtime(next_d)
    next_d = time.strftime("%Y-%m-%d %X", next_d)
    return next_d


def next_hour(date):
    date = add_date(date, 60*60)
    return date
