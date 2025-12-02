from sys import stdin



def solution(h, m):

    print(60*h + m)


if __name__ == "__main__":
    h = (int((stdin.readline().strip())))
    m = (int((stdin.readline().strip())))

    solution(h,m)
