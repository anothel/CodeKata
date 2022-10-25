from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        n: str = stdin.readline().rstrip()
        data: list = list()
        result: int = 0
        for i in range(len(n)):
            if int(n[i]) not in data:
                result += 1
            data.append(int(n[i]))
        stdout.write("%d\n" % result)


if __name__ == "__main__":
    solution()