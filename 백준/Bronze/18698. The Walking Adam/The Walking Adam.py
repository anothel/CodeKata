from sys import stdin, stdout

if __name__ == "__main__":
    for _ in range(int(stdin.readline().rstrip())):
        adamStep: list = list(stdin.readline().rstrip())
        answer: int = 0
        for i in adamStep:
            if i == 'U':
                answer += 1
            else:
                break
        stdout.write("%d\n" % answer)
