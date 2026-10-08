class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r=0,len(numbers)-1
        while l<r:
            c_sum=numbers[l]+numbers[r]
            if c_sum==target:
                return [l+1,r+1]
            elif c_sum<target:
                l+=1
            else:
                r-=1


