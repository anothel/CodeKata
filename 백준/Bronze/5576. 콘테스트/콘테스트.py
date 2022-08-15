from sys import stdin, stdout


def getScore(nums: list):
    for _ in range(10):
        nums.append(int(stdin.readline().rstrip()))
    nums.sort()
    nums.reverse()


def pilkyusAnswer():
    nums1: list = list()
    nums2: list = list()
    getScore(nums1)
    getScore(nums2)
    stdout.write("%d %d\n" % (sum(nums1[:3]), sum(nums2[:3])))


if __name__ == "__main__":
    pilkyusAnswer()
