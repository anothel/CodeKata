from sys import stdin


def solution(n):

    ans = ''
    for i in range(int(n / 5)):
        ans += 'V'
    for i in range(n % 5):
        ans += 'I'
    print(ans)


if __name__ == "__main__":
    n = int(stdin.readline().strip())

    solution(n)
