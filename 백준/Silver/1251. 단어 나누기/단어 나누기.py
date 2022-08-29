from sys import stdin, stdout


def addWord(word: list) -> str:
    cur: str = ""
    for i in word:
        cur += i
    return cur


def solution():
    inputWord: str = stdin.readline().rstrip()

    bucket: list = list()

    for i in range(len(inputWord)):
        for j in range(i + 1, len(inputWord) - 1):
            tmp1: list = list(inputWord[:i + 1])
            tmp1.reverse()
            tmp2: list = list(inputWord[i + 1:j + 1])
            tmp2.reverse()
            tmp3: list = list(inputWord[j + 1:len(inputWord)])
            tmp3.reverse()
            curWord: str = addWord(tmp1)
            curWord += addWord(tmp2)
            curWord += addWord(tmp3)

            bucket.append(curWord)

            # inputWord[:i+1], inputWord[i+1:j+1], inputWord[j+1:len(inputWord)]
            # stdout.write("%s %s %s\n" % (inputWord[:i+1], inputWord[i+1:j+1], inputWord[j+1:len(inputWord)]))
    bucket.sort()

    stdout.write("%s\n" % bucket[0])


if __name__ == "__main__":
    solution()
