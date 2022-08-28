from sys import stdin, stdout


def solution():
    alpha: dict = {chr(i): 0 for i in range(97, 123)}

    sen: str = stdin.read().rstrip()
    result: list = list()
    for i in alpha:
        tmp: int = sen.count(i)
        alpha[i] = tmp
        result.append(tmp)
    maxCount: int = max(result)
    for i in alpha:
        if alpha[i] == maxCount:
            stdout.write("%s" % i)


if __name__ == "__main__":
    solution()
