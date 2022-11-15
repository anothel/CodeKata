from sys import stdin, stdout


def solution():
    a: list = stdin.readline().rstrip()
    b: list = stdin.readline().rstrip()

    for i in range(len(a)):
        stdout.write("%d" % (int(a[i]) & int(b[i])))
    stdout.write("\n")
    for i in range(len(a)):
        stdout.write("%d" % (int(a[i]) | int(b[i])))
    stdout.write("\n")
    for i in range(len(a)):
        stdout.write("%d" % (int(a[i]) ^ int(b[i])))
    stdout.write("\n")
    for i in range(len(a)):
        stdout.write("%d" % (not int(a[i])))
    stdout.write("\n")
    for i in range(len(b)):
        stdout.write("%d" % (not int(b[i])))
    stdout.write("\n")


if __name__ == "__main__":
    solution()