class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        for j in range(len(count)):
            temp=max(count,key=count.get)
        return temp



        