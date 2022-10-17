from sys import stdin, stdout


def solution():
    while True:
        checker: list = [chr(i) for i in range(97, 123)]
        sen: str = stdin.readline().rstrip()
        if sen == '*':
            break
        for i in list(sen):
            if i.lower() in checker:
                checker.remove(i)
        if len(checker) == 0:
            stdout.write("Y\n")
        else:
            stdout.write("N\n")


if __name__ == "__main__":
    solution()