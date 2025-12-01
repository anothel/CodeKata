from sys import stdin


def solution(v):
    v += 300

    if v <= 1800:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    v = 0
    for _ in range(4):
        v += int(stdin.readline().strip())
    solution(v)
