from sys import stdin


def solution(a):
    v = 0
    for i in range(1, a+1):
        v += i
    print(v)

    v = 0
    for i in range(1, a+1):
        v += i
    print(v*v)

    v = 0
    for i in range(1, a+1):
        v += (i*i*i)
    print(v)


if __name__ == "__main__":
    a = int(stdin.readline().strip())
    solution(a)
