from sys import stdin, stdout
import datetime


def solution():
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    d, m = map(int, stdin.readline().rstrip().split())
    dt: datetime = datetime.datetime(2009, m, d)
    stdout.write("%s\n" % days[dt.date().weekday()])


if __name__ == "__main__":
    solution()
