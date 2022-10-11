from sys import stdin, stdout


def make_Adrian(n: int) -> str:
    myAnswer: str = ''
    answerTable: list = ['A', 'B', 'C']
    i: int = 0
    for _ in range(n):
        myAnswer += answerTable[i]
        i += 1
        if i == len(answerTable):
            i = 0
    return myAnswer


def make_Bruno(n: int) -> str:
    myAnswer: str = ''
    answerTable: list = ['B', 'A', 'B', 'C']
    i: int = 0
    for _ in range(n):
        myAnswer += answerTable[i]
        i += 1
        if i == len(answerTable):
            i = 0
    return myAnswer


def make_Goran(n: int) -> str:
    myAnswer: str = ''
    answerTable: list = ['C', 'C', 'A', 'A', 'B', 'B']
    i: int = 0
    for _ in range(n):
        myAnswer += answerTable[i]
        i += 1
        if i == len(answerTable):
            i = 0
    return myAnswer


def getCorrect(my: str, problem: str) -> int:
    answer: int = 0
    for i in range(len(my)):
        if my[i] == problem[i]:
            answer += 1
    return answer


def solution():
    n: int = int(stdin.readline().rstrip())
    problem = stdin.readline().rstrip()

    answer1: str = ''
    answer2: str = ''
    answer3: str = ''
    maxCorrect: int = 0

    curCorrect: int = getCorrect(make_Adrian(n), problem)
    if maxCorrect < curCorrect:
        maxCorrect = curCorrect
        answer1 = 'Adrian'
    curCorrect = getCorrect(make_Bruno(n), problem)
    
    if maxCorrect < curCorrect:
        maxCorrect = curCorrect
        answer1 = 'Bruno'
    elif maxCorrect == curCorrect:
        answer2 = 'Bruno'
    curCorrect = getCorrect(make_Goran(n), problem)
    
    if maxCorrect < curCorrect:
        maxCorrect = curCorrect
        answer1 = 'Goran'
        answer2 = ''
    elif maxCorrect == curCorrect and answer2 == 'Bruno':
        answer3 = 'Goran'
    elif maxCorrect == curCorrect:
        answer2 = 'Goran'

    stdout.write("%d\n" % maxCorrect)
    stdout.write("%s\n" % answer1)
    if answer2 != '':
        stdout.write("%s\n" % answer2)
    if answer3 != '':
        stdout.write("%s\n" % answer3)


if __name__ == "__main__":
    solution()