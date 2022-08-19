from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())
    cur: int = int(stdin.readline().rstrip())
    answer: list = list()
    curBool: bool = False
    for _ in range(n - 1):
        tmp: int = int(stdin.readline().rstrip())
        if curBool == True:
            cur = tmp
            curBool = False
            continue

        if tmp % cur == 0:
            answer.append(tmp)
            curBool = True
    for i in answer:
        stdout.write("%d\n" % i)


if __name__ == "__main__":
    solution()
