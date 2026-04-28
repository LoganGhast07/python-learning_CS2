#Recursion Lecture Exercises Part II, Part IV and Part V

#Part II

#Excercise 2.1: 

from random import random
from unittest import result


def sum_natural(n):
    """
    Calculate sum of natural numbers from 1 to n recursively.
    Example: sum_natural(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    # TODO: Implement this
    # Hint: What's the base case? When n = 0 or n = 1?
    # Hint: How can you express sum(n) in terms of sum(n-1)?
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

# Test cases:
# sum_natural(5) should return 15
# sum_natural(10) should return 55
# sum_natural(1) should return 1
print(sum_natural(5))  # Output: 15
print(sum_natural(10))  # Output: 55
print(sum_natural(1))  # Output: 1

print("=" * 50)

#Excercise 2.2:

def count_digits(n):
    """
    Count the number of digits in n recursively.
    Example: count_digits(1234) = 4
    Example: count_digits(7) = 1
    """
    # TODO: Implement this
    # Hint: How many digits does n // 10 have?
    # Hint: What's the base case? Single digit number?
    if n < 10:
        return 1
    else:
        return 1 + count_digits(n // 10)
# Test cases:
print(count_digits(1234))  # Output: 4
print(count_digits(987654321))  # Output: 9
print(count_digits(5))  # Output: 1

print("=" * 50)

#Excercise 2.3:

def is_palindrome(s):
    """
    Check if string s is a palindrome recursively.
    Ignore case and consider only alphanumeric characters.
    Example: is_palindrome("A man a plan a canal Panama") = True
    Example: is_palindrome("race a car") = False
    """
    # Preprocess the string: remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())

    # Base cases
    if len(s) <= 1:
        return True

    # Recursive case
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Test cases:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("a"))  # Output: True



print("=" * 50)


#Part IV


#Excercise 4.1:

def power(x, n):
    """
    Calculate x raised to the power n recursively.
    Assume n is a non-negative integer.
    Example: power(2, 5) = 32
    Example: power(3, 0) = 1
    """
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return x * power(x, n - 1)
# Test cases:
print(power(2, 5))  # Output: 32
print(power(3, 0))  # Output: 1
print(power(5, 3))  # Output: 125

print("=" * 50)

#Excercise 4.2:

def generate_binary_strings(n):
    """
    Generate all binary strings of length n.
    Example: generate_binary_strings(2) = ['00', '01', '10', '11']
    Example: generate_binary_strings(3) = ['000', '001', '010', '011', '100',
    '101', '110', '111']
    """
    # TODO: Implement this
    def helper(prefix, n):
        if n == 0:
            result.append(prefix)
        else:
            helper(prefix + '0', n - 1)
            helper(prefix + '1', n - 1)
    # Hint: For each position, you can place either '0' or '1'
    # Hint: Use a helper function that builds strings character by character
    result = []
    helper("", n)
    return result
# Test cases:
print(generate_binary_strings(2))  # Output: ['00', '01', '10', '11']
print(generate_binary_strings(1))  # Output: ['0', '1']


print("=" * 50)

#Excercise 4.3:

def subset_sum(nums, target):
    """
    Check if any subset of nums adds up to target.
    Example: subset_sum([3, 34, 4, 12, 5, 2], 9) = True (3 + 4 + 2 = 9)
    Example: subset_sum([3, 34, 4, 12, 5, 2], 30) = False
    """
    # TODO: Implement this
    # Hint: For each number, you have two choices: include it or exclude it
    # Hint: Use index to track position in array
    def helper(index, current_sum):
        if current_sum == target:
            return True
        if index == len(nums):
            return False
        # Include the current number
        if helper(index + 1, current_sum + nums[index]):
            return True
        # Exclude the current number
        return helper(index + 1, current_sum)
    return helper(0, 0)
# Test cases:

print(subset_sum([3, 34, 4, 12, 5, 2], 9))  # Output: True
print(subset_sum([1, 2, 3, 4], 10))  # Output: True
print(subset_sum([1, 2, 3], 7))  # Output: False


print("=" * 50)


#Part V

#Excercise 5.1:

def recursive_sum(arr, n):
    """
    Sum first n elements of array arr recursively.
    """
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)
# Questions to answer:
# 1. Write the recurrence relation for time complexity: T(n) = T(n-1) + O(1) with base case T(0) = O(1)
# 2. What is the time complexity? O(n): each call processes one element and there are n calls until the base case is reached.
# 3. What is the space complexity? O(n): each recursive call adds a layer to the call stack, and in the worst case, there will be n layers until the base case is reached.
# 4. Draw the recursion tree for recursive_sum([1,2,3,4], 4): 
# recursive_sum([1,2,3,4], 4)
# ├── arr[3] + recursive_sum([1,2,3,4], 3)
#     ├── arr[2] + recursive_sum([1,2,3,4], 2)
#         ├── arr[1] + recursive_sum([1,2,3,4], 1)
#             ├── arr[0] + recursive_sum([1,2,3,4], 0)  

#Test
print(recursive_sum([1, 2, 3, 4], 4))  # Output: 10
print(recursive_sum([5, 10, 15], 3))  # Output: 30
print(recursive_sum([1, 2, 3], 0))  # Output: 0


print("=" * 50)

#Excercise 5.2:


def binary_search(arr, target, left, right):
    """
    Search for target in sorted array arr[left:right+1].
    Return index if found, -1 otherwise.
    """
    # TODO: Implement recursive binary search
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
    # TODO: Analyze time complexity
    # TODO: Analyze space complexity
    pass

# Requirements:
# 1. Implement the function
# 2. Write the recurrence relation
# 3. Prove time complexity is O(log n)
# 4. Compare space complexity with iterative version"""

# Test cases:
print(binary_search([1, 2, 3, 4, 5], 3, 0, 4))  # Output: 2
print(binary_search([1, 2, 3, 4, 5], 6, 0, 4))  # Output: -1
print(binary_search([1, 2, 3, 4, 5], 1, 0, 4))  # Output: 0


print("=" * 50)

#Excercise 5.3:

def edit_distance(s1, s2):
    """
    Find minimum edit distance between s1 and s2.
    Operations allowed: insert, delete, replace
    Example: edit_distance("cat", "cut") = 1 (replace 'a' with 'u')
    Example: edit_distance("sunday", "saturday") = 3
    """
    # TODO: Design recursive solution
    def helper(i, j):
        if i == 0:
            return j  # Need to insert all remaining characters of s2
        if j == 0:
            return i  # Need to delete all remaining characters of s1
        if s1[i - 1] == s2[j - 1]:
            return helper(i - 1, j - 1)  # No operation needed
        else:
            insert_op = helper(i, j - 1) + 1    # Insert a character
            delete_op = helper(i - 1, j) + 1    # Delete a character
            replace_op = helper(i - 1, j - 1) + 1  # Replace a character
            return min(insert_op, delete_op, replace_op)
    # TODO: Identify overlapping subproblems
    # TODO: Optimize with memoization
    # TODO: Analyze time complexity (both versions)

    return helper(len(s1), len(s2))
# Tasks:
# 1. Write naive recursive solution
# 2. Identify why it's inefficient
# 3. Add memoization
# 4. Compare complexities

# Test cases:
print(edit_distance("cat", "cut"))  # Output: 1
print(edit_distance("sunday", "saturday"))  # Output: 3
print(edit_distance("kitten", "sitting"))  # Output: 3

print("=" * 50)


#PART 2:

"""""
Copy and run merge sort on a randomly generated list of 1000000 integers, 
and explain what's the complexity of the algorithm and why it is fast.
"""

import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Generate a list of 1000000 random integers
random_list = [random.randint(0, 1000000) for _ in range(1000000)]

# Sort the list using merge sort
sorted_list = merge_sort(random_list)

#Test the sorted list
print(sorted_list[:10])  # Print the first 10 elements of the sorted list



"""""
The complexity of merge sort is O(n log n) because it divides the list into halves recursively 
(log n divisions) and merges them back (n operations per level). It is fast because it consistently performs O(n log n) 
operations regardless of the initial order of elements.
"""""
