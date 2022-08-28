from sys import stdin, stdout


def solution():
    _ = int(stdin.readline().rstrip())
    lotto: list = list(stdin.readline().rstrip())

    count: int = 1
    curChar: str = lotto[0]
    for s in range(1, len(lotto)):
        if ord(curChar) == ord(lotto[s]) + 1 or ord(curChar) == ord(
                lotto[s]) - 1:
            count += 1
        else:
            count = 1
        curChar = lotto[s]
        if count == 5:
            break

    stdout.write("YES\n" if count == 5 else "NO\n")


if __name__ == "__main__":
    solution()
