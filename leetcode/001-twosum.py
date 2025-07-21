# https://leetcode.com/problems/two-sum/

#topics - array, hash table

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

#brute force solution (O(n^2))
def two_sum(nums, target):
    cleaned_num = []
    for num in nums:
        if num <= target:
            cleaned_num.append(num)
    print('cleaned_num:', cleaned_num)

    answer = []
    for i in range(0, len(cleaned_num)):
        for j in range(i+1, len(cleaned_num)):
            if cleaned_num[i] + cleaned_num[j] == target:
                answer.append(i)
                answer.append(j)
        
    return answer


nums1 = [2,7,11,15]
target1 = 9
print(two_sum(nums1, target1))

nums2 = [3,2,4]
target2 = 6
print(two_sum(nums2, target2))

nums3 = [3,3]
target3 = 6
print(two_sum(nums3, target3))

nums4 = [0,4,3,0]
target4 = 0
print(two_sum(nums4, target4))

##issue! if you cleaned the number array the indices changes! (see num4 and target4, expected answer is [0,3])!!!

#improved brute force solution (O(n^2))
def two_sum(nums, target):
    cleaned_num = {}
    for index, num in enumerate(nums):
        if num <= target:
            cleaned_num[num] = index
    keys_list = list(cleaned_num.keys())
    print('cleanednum:', cleaned_num)
    print('keys_list', keys_list)
    answer = []
    for i in range(0, len(keys_list)):
        for j in range(i+1, len(keys_list)):
            if keys_list[i] + keys_list[j] == target:
                answer.append(cleaned_num[keys_list[i]])
                answer.append(cleaned_num[keys_list[j]])
        
    return answer

#tests
nums1 = [2,7,11,15]
target1 = 9
print(two_sum(nums1, target1))

nums2 = [3,2,4]
target2 = 6
print(two_sum(nums2, target2))

nums3 = [3,3]
target3 = 6
print(two_sum(nums3, target3))

nums4 = [0,4,3,0]
target4 = 0
print(two_sum(nums4, target4))