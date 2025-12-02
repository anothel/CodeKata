from sys import stdin




def solution(N,C):
    print((N-1)*C)


if __name__ == "__main__":
    N = int(stdin.readline().strip())
    C = int(stdin.readline().strip())

    solution(N,C)
