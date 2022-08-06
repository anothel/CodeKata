from sys import stdin, stdout


def solution():
    found: bool = False
    for _ in range(int(stdin.readline().rstrip())):
        if 'anj' == stdin.readline().rstrip():
            found = True
    stdout.write("뭐야;\n" if found else "뭐야?")


if __name__ == "__main__":
    solution()
