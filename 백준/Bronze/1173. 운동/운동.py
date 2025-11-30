from sys import stdin


def solution(N,m,M,T,R):
    X=m
    cnt=0
    timeex=0
    if X+T>M:
        print(-1)
        return
    while True:
        cnt+=1
        if X+T<=M:
            timeex+=1
            X=X+T
        else:
            X=X-R
            if X<m:
                X=m
        if timeex==N:
            break
    print(cnt)
    
if __name__ == "__main__":
    N,m,M,T,R = map(int, stdin.readline().strip().split())
    solution(N,m,M,T,R)

