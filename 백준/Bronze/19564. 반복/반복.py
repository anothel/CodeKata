from sys import stdin, stdout


def solution():
    word: list = list(stdin.readline().rstrip())

    answer: int = 1
    before: int = ord(word[0])

    for i in range(1, len(word)):
        if before < ord(word[i]):
            before = ord(word[i])
            continue
        else:
            before = ord(word[i])
            answer += 1

    stdout.write("%d\n" % answer)


if __name__ == "__main__":
    solution()
