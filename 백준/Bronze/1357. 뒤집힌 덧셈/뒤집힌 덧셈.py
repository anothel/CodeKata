from sys import stdin, stdout


def rev(n: int) -> int:
  answer: str = ''
  for i in str(n):
    answer += i
  tmp:list = list(answer)
  tmp.reverse()
  answer = ''
  for i in tmp:
    answer += i
  return int(answer) 
  

def solution():
    a, b = map(int, stdin.readline().rstrip().split())
    stdout.write("%d\n" % rev(rev(a) + rev(b)))


if __name__ == "__main__":
    solution()
