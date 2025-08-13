#arrays #stacks

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

def valid_parentheses(s):
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if char == ")" and stack[-1] == "(" :
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(char)
    return len(stack) == 0

string1 = "()"
string2 = "()[]{}"
string3 = "()]"

print(valid_parentheses(string1))
print(valid_parentheses(string2))
print(valid_parentheses(string3))

