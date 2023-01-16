from sys import stdin, stdout


def solution():
    a: int = int(stdin.readline().rstrip())
    b: int = int(stdin.readline().rstrip())

    while a <= b:
        stdout.write("All positions change in year %d\n" % a)
        a += 60


if __name__ == "__main__":
    solution()
