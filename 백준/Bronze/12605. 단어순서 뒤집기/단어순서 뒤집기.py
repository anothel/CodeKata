from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        strs: list = list(map(str, stdin.readline().rstrip().split()))
        stdout.write("Case #%d: " % (i + 1))
        strs.reverse()
        for s in strs:
            stdout.write("%s " % s)
        stdout.write("\n")


if __name__ == "__main__":
    solution()
