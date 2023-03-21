from sys import stdin, stdout


def solution():
    a: int = int(stdin.readline().rstrip())

    stdout.write("%.2f\n" % (a / 4))

if __name__ == "__main__":
    solution()
