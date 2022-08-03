from sys import stdin, stdout


def getAnswer(answer: list):
    x: int = 1
    n: int = answer[-1]
    while n > 0:
        x *= n % 10
        n //= 10
    answer.append(x)


def solution():
    answer: list = list()
    while True:
        answer.clear()
        num: int = int(stdin.readline().rstrip())
        if num == 0:
            break
        answer.append(num)
        while answer[-1] >= 10:
            getAnswer(answer)
        for i in answer:
            stdout.write("%d " % i)
        stdout.write("\n")


if __name__ == "__main__":
    solution()
