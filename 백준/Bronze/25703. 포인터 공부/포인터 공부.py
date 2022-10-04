from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    stdout.write("int a;\n")
    stdout.write("int *ptr = &a;\n")

    for i in range(n - 1):
        stdout.write("int ")
        for _ in range(i + 2):
            stdout.write("*")
        stdout.write("ptr%d = &ptr" % (i + 2))
        if i != 0:
            stdout.write("%d;\n" % (i + 1))
        else:
            stdout.write(";\n")


if __name__ == "__main__":
    solution()