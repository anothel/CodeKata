from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        n: int = int(stdin.readline().rstrip())
        
        door:list = [True for _ in range(n)]
        
        for i in range(2, n + 1):
            addValue: int = 1
            while i * addValue <= len(door):
                if door[i * addValue - 1] == True:
                    door[i * addValue - 1] = False
                else:
                    door[i * addValue - 1] = True
                addValue += 1
        stdout.write("%d\n" % door.count(True))


if __name__ == "__main__":
    solution()