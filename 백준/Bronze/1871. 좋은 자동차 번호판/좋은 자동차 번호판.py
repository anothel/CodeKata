from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        a, tmp = map(str, stdin.readline().rstrip().split('-'))
        num: int = int(tmp)

        answer: int = 0
        for i in range(3):
            answer += (ord(a[i]) - 65) * 26**(2 - i)

        if abs(answer - num) <= 100:
            stdout.write("nice\n")
        else:
            stdout.write("not nice\n")


if __name__ == "__main__":
    solution()