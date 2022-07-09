from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        w, k = map(int, stdin.readline().rstrip().split())
        if w == 1 and k == 1:
            stdout.write("0\n")
            continue
        stdout.write("%d\n" % (w * k // 2))


if __name__ == "__main__":
    solution()
