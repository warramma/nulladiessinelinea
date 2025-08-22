#O(n) time and space complexity
#uses a set due the set's characteristic of only having unique elements.

def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        result = False
        for num in nums:
            if num in my_set: 
                result = True
            else:
                my_set.add(num)

# alternate solution also O(n) but uses a frequency dictionary instead
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                return True
            else:
                freq_dict[num] = 1
        
        return False