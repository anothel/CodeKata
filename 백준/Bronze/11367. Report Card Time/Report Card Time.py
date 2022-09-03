from sys import stdin, stdout


def getGrade(n: int) -> str:
    answer: str = ''

    if 97 <= n <= 100:
        answer = 'A+'
    elif 90 <= n <= 96:
        answer = 'A'
    elif 87 <= n <= 89:
        answer = 'B+'
    elif 80 <= n <= 86:
        answer = 'B'
    elif 77 <= n <= 79:
        answer = 'C+'
    elif 70 <= n <= 76:
        answer = 'C'
    elif 67 <= n <= 69:
        answer = 'D+'
    elif 60 <= n <= 66:
        answer = 'D'
    else:
        answer = 'F'

    return answer


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        name, score = map(str, stdin.readline().rstrip().split())
        stdout.write("%s %s\n" % (name, getGrade(int(score))))


if __name__ == "__main__":
    solution()
