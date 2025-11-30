from sys import stdin


def solution(x0, N):
    xt = x0 
    for t in range(N):
        if xt % 2 == 0:
            xt = int((xt/2))^(6)
        else:
            xt = (2*xt)^(6)
    print(xt)

if __name__ == "__main__":
    x0, N = map(int, stdin.readline().strip().split())
    solution(x0, N)
