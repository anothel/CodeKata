from sys import stdin, stdout


def solution():
    alpha: dict = {chr(i): i for i in range(65, 91)}
    for _ in range(int(stdin.readline().rstrip())):
        answer: int = 0
        mine: set = set()
        s: list = stdin.readline().rstrip()
        for i in s:
            mine.add(i)
        for i in alpha:
            if i in mine:
                continue
            answer += alpha[i]
        stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()