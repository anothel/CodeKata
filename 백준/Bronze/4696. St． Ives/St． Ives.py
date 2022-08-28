from sys import stdin, stdout


def solution():
    while True:
        n = float(stdin.readline().rstrip())
        if n == 0:
            break
        stdout.write("%.2f\n" % (1 + n + n**2 + n**3 + n**4))


if __name__ == "__main__":
    solution()
