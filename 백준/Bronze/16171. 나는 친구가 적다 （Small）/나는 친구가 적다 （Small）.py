from sys import stdin, stdout


def solution():
    lInput: str = stdin.readline().rstrip()
    lMine: str = stdin.readline().rstrip()
    cur: str = ''

    for i in lInput:
        if (65 <= ord(i) and ord(i) <= 90) or (97 <= ord(i) and ord(i) <= 122):
            cur += i

    stdout.write("1\n" if lMine in cur else "0\n")


if __name__ == "__main__":
    solution()
