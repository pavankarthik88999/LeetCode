class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i=0
        j=k-1
        n=len(nums)
        add=sum(nums[:k])
        avg=add/k
        while j<n-1:
            add=add-nums[i]
            i=i+1
            j=j+1
            add=add+nums[j]
            temp=add/k
            if temp>avg:
                avg=temp
        return avg


            




        