from sys import stdin, stdout


def solution():
    found: bool = False
    for _ in range(int(stdin.readline().rstrip())):
        player: str = stdin.readline().rstrip()
        if 'anj' == player:
            found = True
    stdout.write("뭐야;\n" if found else "뭐야?")


if __name__ == "__main__":
    solution()
