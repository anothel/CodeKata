from sys import stdin




def solution(N,C,P):
    if C*P>=N:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    C = int(stdin.readline().strip())
    P = int(stdin.readline().strip())

    solution(N,C,P)
