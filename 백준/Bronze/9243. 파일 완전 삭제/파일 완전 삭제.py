from sys import stdin, stdout


def func(s: str) -> str:
    output: str = ''
    for i in s:
        if i == '0':
            output += '1'
        else:
            output += '0'
    return output


def solution():
    n: int = int(stdin.readline().rstrip())
    input1: str = stdin.readline().rstrip()
    input2: str = stdin.readline().rstrip()

    output: str = func(input1)
    for _ in range(1, n):
        output = func(output)

    if output == input2:
        stdout.write("Deletion succeeded\n")
    else:
        stdout.write("Deletion failed\n")


if __name__ == "__main__":
    solution()