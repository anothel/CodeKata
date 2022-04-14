from sys import stdin, stdout


def countSort(lnums: list, nfrom: int, nto: int, nmin: int, lcounts: list, nArraySize: int):
  # counting at each index
  for i in range(nfrom, nto):
    lcounts[lnums[i] - nmin] += 1

  # make sorted array
  nIdx: int = 0
  for i in range(nArraySize):
    for _ in range(lcounts[i]):
      lnums[nIdx] = i + nmin
      nIdx += 1

  return


def solution():
  n: int = int(stdin.readline().rstrip())
  nums: list = list(map(int, stdin.readline().rstrip().split()))
  m: int = int(stdin.readline().rstrip())
  mines: list = list(map(int, stdin.readline().rstrip().split()))

  nmin: int = min(nums)
  # nmax: int = max(nums)
  # nArraySize: int = nmax - nmin + 1

  lCounts: list = [0] * 20000000
  # lCounts: list = [0] * nArraySize
  countSort(nums, 0, len(nums), nmin, lCounts, 20000000)

  for i in mines:
    stdout.write("%d " % lCounts[i - nmin])


if __name__ == "__main__":
  solution()
