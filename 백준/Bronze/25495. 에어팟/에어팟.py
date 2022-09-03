from sys import stdin, stdout


def solution():
    curPercent: int = 0
    before: int = 0
    beforeUse: int = 0
    _ = int(stdin.readline().rstrip())
    nums: list = list(map(int, stdin.readline().rstrip().split()))
    
    for i in nums:
        if i != before:
          curPercent += 2
          beforeUse = 2
        else:
          curPercent += beforeUse * 2
          beforeUse *= 2
        
        before = i
        if curPercent >= 100:
          curPercent = 0
          before = 0
          
    stdout.write("%d\n" % curPercent)


if __name__ == "__main__":
    solution()
