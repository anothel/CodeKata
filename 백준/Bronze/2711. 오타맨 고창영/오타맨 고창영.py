from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        num, typping = map(str, stdin.readline().rstrip().split())

        for i in range(len(typping)):
            if i + 1 == int(num):
                continue
            stdout.write("%s" % typping[i])
        stdout.write("\n")


if __name__ == "__main__":
    solution()
