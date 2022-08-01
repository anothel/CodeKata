from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        infos: list = list(map(str, stdin.readline().rstrip().split()))
        if infos[1] == "kg":
            stdout.write("%.4f lb\n" % (float(infos[0]) * 2.2046))
        elif infos[1] == "lb":
            stdout.write("%.4f kg\n" % (float(infos[0]) * 0.4536))
        elif infos[1] == "l":
            stdout.write("%.4f g\n" % (float(infos[0]) * 0.2642))
        elif infos[1] == "g":
            stdout.write("%.4f l\n" % (float(infos[0]) * 3.7854))
        else:
            stdout.write("%.4f %s\n" % (float(infos[0]), infos[1]))


if __name__ == "__main__":
    solution()
