def TwoSum(intList, target):
    hashSet = {}
    for i, n in enumerate(intList):
        difference = target - n
        if difference in hashSet:
            return (difference, intList[i])
        hashSet[n] = i

nums = list(map(int,input().strip().split()))
target = int(input())

print(TwoSum(nums,target))