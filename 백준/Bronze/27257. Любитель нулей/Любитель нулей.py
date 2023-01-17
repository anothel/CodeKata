from sys import stdin, stdout


def solution():
    b: list = list(stdin.readline().rstrip())
    b.reverse()
    count: bool = False
    answer: int = 0
    for i in b:
        if count == False:
            if i == '0':
                continue
            else:
                count = True
        else:
            if i == '0':
                answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
