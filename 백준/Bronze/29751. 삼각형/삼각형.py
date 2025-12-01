from sys import stdin


def solution(w, h):
    v = w*h*0.5
    print(v)


if __name__ == "__main__":
    w, h = map(int, stdin.readline().strip().split())
    solution(w, h)
