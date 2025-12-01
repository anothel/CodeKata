from sys import stdin


def solution(s1,s2):

    if s2/2<=s1:
        print("E")
    else:
        print("H")


if __name__ == "__main__":
    s1,s2 = map(int,stdin.readline().strip().split())
    

    solution(s1,s2)
