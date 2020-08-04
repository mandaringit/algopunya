import time

timestamps = [
    "2018-12-12 01:17:31",
    "2018-12-12 02:17:31",
    "2018-12-12 06:17:31",
    "2018-11-25 07:17:31",
    "2018-11-25 11:32:31",
    "2018-11-25 12:35:31"
]


def time_format(t):
    return time.strptime(t, '%Y-%m-%d %H:%M:%S')[0:6]


timestamps.sort(key=time_format, reverse=True)
print(timestamps)

