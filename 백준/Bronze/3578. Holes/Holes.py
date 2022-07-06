from sys import stdin, stdout


def countHoles(s: str) -> int:
    answer: int = 0
    if s == "0" or s == "4" or s == "6" or s == "9":
        return 1
    elif s == "8":
        return 2
    else:
        return 0


def solve():
    h: int = int(stdin.readline().rstrip())

    if h == 0:
        stdout.write("1\n")
        return
    elif h == 1:
        stdout.write("0\n")
        return

    answer: str = ""
    if h % 2 == 0:
        for _ in range(h // 2):
            answer += "8"
    else:
        answer += "4"
        for _ in range(h // 2):
            answer += "8"

    stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solve()
