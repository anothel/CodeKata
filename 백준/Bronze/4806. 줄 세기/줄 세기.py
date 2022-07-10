from sys import stdin, stdout


def solution():
    answer: int = 0
    while True:
        try:
            _ = input()
            answer += 1
        except EOFError:
            break
    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
