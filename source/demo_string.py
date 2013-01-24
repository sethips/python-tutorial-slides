import datetime
import time
import random


def demo_strip():
    print('This takes {:d} mins to do'.format(10))
    print('This takes {:010d} mins to do'.format(1))


def strTime(dt=None,
            str_format=None):
    if not dt:
        dt = datetime.datetime.today()
    if not str_format:
        str_format = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:02.0f}'

    return str_format.format(
        dt.year, dt.month, dt.day,
        dt.hour, dt.minute, dt.second,
        dt.microsecond/10000)


def strDiffTime(d_start, d_end, human=True):
    delta = d_end - d_start

    if human:
        time_str = ""
        if delta.days < 0:
            print('Negative value when computing time difference of')
            print('start:', strTime(d_start), 'end:', strTime(d_end))
            time_str = "-"
            delta = d_start - d_end

        h = (delta.days * 24) + (delta.seconds // 3600)
        m = delta.seconds % 3600 // 60

        if h:
            time_str += "{:0.0f}h".format(h)
            time_str += "{:0.0f}m".format(m)
        elif m:
            time_str += "{:0.0f}m".format(m)

        time_str += "{:0.2f}s".format(delta.seconds % 60 +
                                      delta.microseconds/1000000)
        return time_str
    else:
        return delta.total_seconds()


def rand_sleep():
    start = datetime.datetime.today()
    time.sleep(random.random() * 1.5)
    end = datetime.datetime.today()
    print('Random sleep', strDiffTime(start, end))

if __name__ == '__main__':
    demo_strip()
    print('Now is', strTime())
    rand_sleep()
