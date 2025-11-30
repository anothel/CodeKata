from sys import stdin


def solution(N):
    if N == "SONGDO":
        ans = "HIGHSCHOOL"
    elif N == "CODE":
        ans = "MASTER"
    elif N == "2023":
        ans = "0611"
    elif N == "ALGORITHM":
        ans = "CONTEST"
    else :
        ans = "UNKNOWN"
    print(ans)


if __name__ == "__main__":
    N = stdin.readline().strip()
    solution(N)
