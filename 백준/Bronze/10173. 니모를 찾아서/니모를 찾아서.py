from sys import stdin, stdout


def solution():
    while True:
        find: str = stdin.readline().rstrip()
        if find == 'EOI':
            break

        if 'nemo' in find.lower():
            stdout.write("Found\n")
        else:
            stdout.write("Missing\n")


if __name__ == "__main__":
    solution()