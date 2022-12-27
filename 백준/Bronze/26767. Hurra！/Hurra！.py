from sys import stdin, stdout


def solution():
    n = int(stdin.readline().rstrip())

    for i in range(1, n + 1):
        if i % 7 == 0 and i % 11 == 0:
            stdout.write("Wiwat!\n")
        elif i % 7 == 0:
            stdout.write("Hurra!\n")
        elif i % 11 == 0:
            stdout.write("Super!\n")
        else:
            stdout.write("%d\n" % i)


if __name__ == "__main__":
    solution()
