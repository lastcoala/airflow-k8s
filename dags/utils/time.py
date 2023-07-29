import pendulum

def date_jkt(year, month, day, **kwargs):
    return pendulum.datetime(year, month, day, **kwargs, tz="Asia/Jakarta")