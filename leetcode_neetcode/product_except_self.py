
def productExceptSelf(nums):
    prefix_array = []
    product = 1
    for num in nums:
        product *= num
        prefix_array.append(product)

    postfix_array = [1] * len(nums)
    product = 1
    for i in range(len(nums)-1, -1, -1):
        product *= nums[i]
        postfix_array[i] = product
    
    output = []
    for i in range(0, len(nums)):
        if i == 0:
            output.append(postfix_array[i+1])
        elif i == len(nums) - 1:
            output.append(prefix_array[i-1])
        else:
            output.append(prefix_array[i-1] * postfix_array[i+1])
    
    return output

print("output:", productExceptSelf([1,2,3,4]))