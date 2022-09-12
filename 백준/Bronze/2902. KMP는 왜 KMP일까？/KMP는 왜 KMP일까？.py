from sys import stdin, stdout


def solution():
    name: str = stdin.readline().rstrip()

    stdout.write("%s" % name[0])

    for i in range(len(name)):
        if '-' == name[i] and i + 1 < len(name):
            stdout.write("%s" % name[i + 1])


if __name__ == "__main__":
    solution()
