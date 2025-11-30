from sys import stdin


def solution(N, A, B):
    if A < B:
        ans = 'Bus'
    elif (A > B) and (N <= B):
        ans = 'Subway'
    elif (A > B) and (N > B):
        ans = 'Bus'
    else:
        ans = "Anything"
    print(ans)


if __name__ == "__main__":
    N, A, B = map(int, stdin.readline().strip().split())

    solution(N, A, B)
