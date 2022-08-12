from sys import stdin, stdout

if __name__ == "__main__":
    while True:
      n, m = map(int, stdin.readline().rstrip().split())
      if n == 0 and m == 0:
        break
      nums: list = list(map(int, stdin.readline().rstrip().split()))
      money: int = m // n
      answer: int = 0
      for i in nums:
        if i < money:
          answer += i
        else:
          answer += money
      stdout.write("%d\n" % answer)
      
