from sys import stdin, stdout


def solution():
    while True:
        a: int = int(stdin.readline().rstrip())
        if a == 0:
            break

        while True:
            tmp: int = 0
            while a > 0:
                tmp += a % 10
                a //= 10
            if tmp >= 10:
                a = tmp
            else:
                break

        stdout.write("%d\n" % tmp)


if __name__ == "__main__":
    solution()