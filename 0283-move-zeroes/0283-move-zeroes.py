class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        # Traverse through the array with a 'right' pointer
        for right in range(len(nums)):
            if nums[right] != 0:
                # Swap the non-zero element to the 'left' position
                nums[left], nums[right] = nums[right], nums[left]
                left += 1