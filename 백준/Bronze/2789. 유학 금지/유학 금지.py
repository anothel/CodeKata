from sys import stdin, stdout


def solution():
    checker: list = list('CAMBRIDGE')
    s: list = stdin.readline().rstrip()
    answer: str = ''
    for i in s:
        if i in checker:
            continue
        answer += i
    stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solution()