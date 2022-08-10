from sys import stdin, stdout


def solution():
    temperature: int = -30
    ocean: int = 0
    oxygen: int = 0

    for _ in range(int(stdin.readline().rstrip())):
        t, v = map(str, stdin.readline().rstrip().split())
        if t == 'temperature':
            temperature += int(list(v)[1])
        elif t == 'ocean':
            ocean += int(list(v)[1])
        elif t == 'oxygen':
            oxygen += int(list(v)[1])
    stdout.write("liveable\n" if ocean >= 9 and temperature >= 8
                 and oxygen >= 14 else "not liveable\n")


if __name__ == "__main__":
    solution()
