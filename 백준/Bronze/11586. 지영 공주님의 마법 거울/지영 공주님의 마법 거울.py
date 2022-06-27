from sys import stdin, stdout


def main():
    ji: list = list()
    for _ in range(int(stdin.readline().rstrip())):
        ji.append(stdin.readline().rstrip())
    k: int = int(stdin.readline().rstrip())
    if k == 1:
        for i in range(len(ji)):
            stdout.write("%s\n" % ji[i])
    elif k == 2:
        for i in range(len(ji)):
            tmp: list = list(ji[i])
            tmp.reverse()
            for s in tmp:
                stdout.write("%s" % s)
            stdout.write("\n")
    elif k == 3:
        for i in range(len(ji) - 1, -1, -1):
            stdout.write("%s\n" % ji[i])


if __name__ == "__main__":
    main()
