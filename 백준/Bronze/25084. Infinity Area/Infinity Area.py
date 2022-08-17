from sys import stdin, stdout


def solution():
    for i in range(int(stdin.readline().rstrip())):
        r, a, b = map(int, stdin.readline().rstrip().split())

        area: int = 0
        currentR: int = r

        flag: bool = True
        while currentR > 0:
            area += currentR**2
            if flag == True:
                currentR *= a
            else:
                currentR //= b
            flag = not flag

        stdout.write("Case #%d: %f\n" % (i + 1, area * 3.14159265359))


if __name__ == "__main__":
    solution()
