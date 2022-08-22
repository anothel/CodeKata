from sys import stdin, stdout


def solution():
    while True:
        s: list = list(stdin.readline().rstrip('\n'))
        if s[0] == '*' and s[1] == '*' and s[2] == '*':
            break
        tmp: list = list()
        for i in range(len(s) - 1, -1, -1):
            tmp.append(s[i])

        for i in tmp:
            stdout.write("%s" % i)
        stdout.write("\n")


if __name__ == "__main__":
    solution()
