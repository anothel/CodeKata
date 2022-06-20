from sys import stdin, stdout


def main():
    n: str = stdin.readline().rstrip()
    f: int = stdin.readline().rstrip()

    while True:
        for i in range(100):
            tmpNum: str = n[:-2]
            if i < 10:
                tmpNum += "0"
            tmpNum += str(i)
            curNum: int = int(tmpNum)
            if curNum % int(f) == 0:
                if i < 10:
                    stdout.write("0%d\n" % i)
                else:
                    stdout.write("%d\n" % i)
                return
        break


if __name__ == "__main__":
    main()
