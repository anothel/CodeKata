from sys import stdin, stdout


def solution():
    sets: list = [0 for _ in range(3)]
    for _ in range(int(stdin.readline().rstrip())):
        tmp: list = list(map(int, stdin.readline().rstrip().split()))
        for i in range(3):
            sets[i] += tmp[i]

        minValue: int = min(sets)
        if minValue < 30:
            stdout.write("NO\n")
            continue
        else:
            for i in range(3):
                sets[i] -= minValue
        stdout.write("%d\n" % minValue)


if __name__ == "__main__":
    solution()
