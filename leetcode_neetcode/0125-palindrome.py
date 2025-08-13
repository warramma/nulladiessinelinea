# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

#stack #array

def isPalindrome(s):
    cleaned_string = []
    for char in s:
        if char.isalnum():
            cleaned_string.append(char.lower())
    
    print(cleaned_string)

    reversed_characters = cleaned_string[::-1]
    print(reversed_characters)

    return cleaned_string == reversed_characters

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("banana"))
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false