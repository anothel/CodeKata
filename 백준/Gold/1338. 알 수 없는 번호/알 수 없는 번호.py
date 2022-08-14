from sys import stdin, stdout


def solution():
    a, b = map(int, stdin.readline().rstrip().split())
    x, y = map(int, stdin.readline().rstrip().split())
    if a > b:
        a, b = b, a

    x = abs(x)

    if y < 0 or y >= x:
        stdout.write("Unknwon Number\n")
        return

    answer: list = list()
    second: bool = False

    value: int = x * (a // x) + y
    while value <= b:
        if a <= value <= b:
            if answer:
                second = True
                break
            answer.append(value)
        value += x
    stdout.write(
        "%d\n" %
        answer[0] if answer and second == False else "Unknwon Number\n")


if __name__ == "__main__":
    solution()
