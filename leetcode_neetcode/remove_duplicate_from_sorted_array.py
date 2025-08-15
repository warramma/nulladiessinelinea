#inefficient solution, constraint can only use array, no "two pointers"
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            num_count = nums.count(num)
            if num_count > 1:
                for i in range (1, num_count):
                    nums.remove(num)
        
        return len(nums)