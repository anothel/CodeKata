from sys import stdin, stdout


def main():
    sen: str = stdin.readline().rstrip()
    if len(sen) % 10 != 0:
        for _ in range(10 - len(sen) % 10):
            sen += " "
    for i in range(1, len(sen) // 10 + 1):
        for j in range((i - 1) * 10, i * 10):
            stdout.write("%s" % sen[j])
        stdout.write("\n")


if __name__ == "__main__":
    main()
