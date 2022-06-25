from sys import stdin, stdout


def solution():
    answer: str = ""
    for i in range(1, 6):
        if str(stdin.readline().rstrip()).find("FBI") >= 0:
            answer += "%d " % i
    stdout.write("%s" % answer if answer != "" else "HE GOT AWAY!")


if __name__ == "__main__":
    solution()
