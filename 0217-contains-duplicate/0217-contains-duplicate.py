class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        for j in count.values():
            if j>1:
                return True
         
        return False
                
       

               
        
        