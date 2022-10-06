from sys import stdin, stdout


def solution():
    answer: list = list()
    for _ in range(int(stdin.readline().rstrip())):
        score:int = 0
        a, d, g = map(int, stdin.readline().rstrip().split())

        score = a * (d + g)
        
        if a == d+g:
            score*=2
            
        answer.append(score)



    stdout.write("%d\n" % max(answer))


if __name__ == "__main__":
    solution()