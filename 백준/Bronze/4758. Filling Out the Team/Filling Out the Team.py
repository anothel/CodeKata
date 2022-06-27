from sys import stdin, stdout


def solve():
    while True:
        answer: str = ""
        s, w, p = map(float, stdin.readline().rstrip().split())
        if s == 0 and w == 0 and p == 0:
            break
        if s <= 4.5 and w >= 150 and p >= 200:
            answer += "Wide Receiver "
        if s <= 6.0 and w >= 300 and p >= 500:
            answer += "Lineman "
        if s <= 5.0 and w >= 200 and p >= 300:
            answer += "Quarterback "
        if answer == "":
            answer += "No positions"
        stdout.write("%s\n" % answer)


if __name__ == "__main__":
    solve()
