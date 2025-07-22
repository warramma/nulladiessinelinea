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

##issue! ⬆️⬆️⬆️⬆️ if you cleaned the number array the indices changes! (see num4 and target4, expected answer is [0,3])!!!

#working brute force solution (O(n^2)) ⬇️⬇️⬇️
def two_sum(nums, target):
    print("working two sum solution")
    answer=[]
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                answer.append(i)
                answer.append(j)
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


#solution less than O(n^2)
#approach - use a dictionary to map values to indices (in a list)
#go through the nums list and find the complement needed to get up to the target number. 
def optimized_two_sum(nums, target):
    nums_dict = {}
    for index, num in enumerate(nums):
        if num in nums_dict:
            nums_dict[num].append(index)
        else:
            nums_dict[num] = [index]
    
    print("optimized:", nums_dict)
    answer = []
    for num in nums:
        complement = target - num
        print("complement:", complement, " num:", num)
        print("length:", len(nums_dict[num]))
        if len(nums_dict[num]) < 2:
            if complement!=num and complement in nums_dict:
                answer.append(nums_dict[num][0])
                answer.append(nums_dict[complement][0])
                break
        elif len(nums_dict[num]) >=2:
            if complement == num:
                answer.append(nums_dict[num][0])
                answer.append(nums_dict[num][1])
                break
            
    return answer
        
#tests
nums1 = [2,7,11,15]
target1 = 9
print(optimized_two_sum(nums1, target1))

nums2 = [3,2,4]
target2 = 6
print(optimized_two_sum(nums2, target2))

nums3 = [3,3]
target3 = 6
print(optimized_two_sum(nums3, target3))

nums4 = [0,4,3,0]
target4 = 0
print(optimized_two_sum(nums4, target4))