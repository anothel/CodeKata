from sys import stdin, stdout


def solution():
    sr = (stdin.readline().rstrip())

    stdout.write("%d : %d\n" % (sr.count('A'), sr.count('B')))


if __name__ == "__main__":
    solution()
