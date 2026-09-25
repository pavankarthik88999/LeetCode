class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        add=0
        new=[]
        for i in range(len(nums)):
            add+=nums[i]
            new.append(add)
        return new
        