from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        infos: list = list(map(str, stdin.readline().rstrip().split()))
        for i in range(len(infos)):
            if i == 0:
                tmpList: list = infos[0]
                for j in range(len(tmpList)):
                    if j == 0:
                        stdout.write("%s" % str(tmpList[j]).upper())
                    else:
                        stdout.write("%s" % str(tmpList[j]))
                stdout.write(" ")
            else:
                stdout.write("%s " % infos[i])
        stdout.write("\n")


if __name__ == "__main__":
    solution()
