from sys import stdin, stdout


def solution():
    sen: str = stdin.readline().rstrip()

    for i in sen:
        p: str = i
        tmp: int = ord(i) + 13
        if i.islower() == True:
            if tmp > 122:
                tmp -= 26
            p = chr(tmp)
        elif i.isupper() == True:
            if tmp > 90:
                tmp -= 26
            p = chr(tmp)

        stdout.write("%s" % p)


if __name__ == "__main__":
    solution()
