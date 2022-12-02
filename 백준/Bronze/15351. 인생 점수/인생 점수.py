from sys import stdin, stdout


def solution():
    n: int = int(stdin.readline().rstrip())

    for _ in range(n):
        life: list = list(stdin.readline().rstrip())
        answer: int = 0
        for s in life:
            if s.isalpha() == False:
                continue
            answer += (ord(s) - 64)
        if answer == 100:
            stdout.write("PERFECT LIFE\n")
        else:
            stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
