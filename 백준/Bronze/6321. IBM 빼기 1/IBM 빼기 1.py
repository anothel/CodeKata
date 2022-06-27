from sys import stdin, stdout


def main():
    n: int = int(stdin.readline().rstrip())
    for i in range(1, n + 1):
        s: list = stdin.readline().rstrip()
        stdout.write("String #%d\n" % i)
        for j in s:
            if j == "Z":
                stdout.write("A")
            else:
                stdout.write("%s" % chr(ord(j) + 1))
        stdout.write("\n\n")


if __name__ == "__main__":
    main()
