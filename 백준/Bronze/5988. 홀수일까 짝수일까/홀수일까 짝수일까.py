from sys import stdin, stdout


def main():
    for _ in range(int(stdin.readline().rstrip())):
        if int(stdin.readline().rstrip()) % 2 == 0:
            stdout.write("even\n")
        else:
            stdout.write("odd\n")


if __name__ == "__main__":
    main()
