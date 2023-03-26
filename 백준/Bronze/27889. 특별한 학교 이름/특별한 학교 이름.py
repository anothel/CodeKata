from sys import stdin, stdout


def solution():
    name: str = (stdin.readline().rstrip())
    p: str = ''

    if name == 'NLCS':
        p = 'North London Collegiate School'
    elif name == 'BHA':
        p = 'Branksome Hall Asia'
    elif name == 'KIS':
        p = 'Korea International School'
    elif name == 'SJA':
        p = 'St. Johnsbury Academy'

    stdout.write("%s\n" % p)


if __name__ == "__main__":
    solution()
