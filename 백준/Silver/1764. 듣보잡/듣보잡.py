from sys import stdin, stdout


def solution():
    n, m = map(int, stdin.readline().rstrip().split())

    ears: set = set()

    for _ in range(n):
        ears.add(stdin.readline().rstrip())

    answer: int = 0
    answers: list = list()
    
    for _ in range(m):
        eye: str = stdin.readline().rstrip()
        if eye in ears:
            answer += 1
            answers.append(eye)

    stdout.write("%d\n" % answer)
    answers.sort()
    for i in answers:
        stdout.write("%s\n" % i)


if __name__ == "__main__":
    solution()
