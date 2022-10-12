from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        name: str = stdin.readline().rstrip()
        countG: int = name.count('g') + name.count('G')
        countB: int = name.count('b') + name.count('B')

        if countG == countB:
            stdout.write("%s is NEUTRAL\n" % name)
        elif countG > countB:
            stdout.write("%s is GOOD\n" % name)
        else:
            stdout.write("%s is A BADDY\n" % name)


if __name__ == "__main__":
    solution()