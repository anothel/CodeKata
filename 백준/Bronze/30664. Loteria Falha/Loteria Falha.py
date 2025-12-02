from sys import stdin


def solution(a, w, v):

    if w/v >= a:
        print("1")
    else:
        print("0")


if __name__ == "__main__":
    while True:
        n = int(stdin.readline().strip())
        if n == 0:
            break
        if n % 42 == 0:
            print("PREMIADO")
        else:
            print("TENTE NOVAMENTE")
