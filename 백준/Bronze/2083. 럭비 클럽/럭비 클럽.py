from sys import stdin, stdout


def solution():
    while True:
        infos: list = list(map(str, stdin.readline().rstrip().split()))
        if infos[0] == "#" and infos[1] == "0" and infos[2] == "0":
            break

        if int(infos[1]) > 17 or int(infos[2]) >= 80:
            stdout.write("%s Senior\n" % infos[0])
        else:
            stdout.write("%s Junior\n" % infos[0])


if __name__ == "__main__":
    solution()
