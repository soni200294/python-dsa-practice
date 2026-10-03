from functools import lru_cache


def two_sum(nums, target):
    """Return indexes of two numbers that add up to target. O(n) time."""
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []


def is_valid_parentheses(s):
    """Check if brackets are balanced using a stack. O(n) time."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def is_palindrome(s):
    """Ignore case and symbols, then compare with the reverse. O(n) time."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def binary_search(nums, target):
    """Find target in a sorted list. O(log n) time."""
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def is_anagram(a, b):
    """Two words are anagrams if their sorted letters match. O(n log n) time."""
    return sorted(a.lower()) == sorted(b.lower())


def max_subarray(nums):
    """Largest sum of a continuous part of the list (Kadane's algorithm). O(n) time."""
    best = current = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best


@lru_cache(maxsize=None)
def fibonacci(n):
    """Fibonacci with memoization (saves repeated work). O(n) time."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("Two Sum [2, 7, 11, 15], target 9:", two_sum([2, 7, 11, 15], 9))
    print("Valid parentheses '{[()]}':", is_valid_parentheses("{[()]}"))
    print("Valid parentheses '([)]':", is_valid_parentheses("([)]"))
    print("Palindrome 'A man, a plan, a canal: Panama':", is_palindrome("A man, a plan, a canal: Panama"))
    print("Binary search for 23:", binary_search([2, 5, 8, 12, 16, 23, 38], 23))
    print("Anagram 'listen' and 'silent':", is_anagram("listen", "silent"))
    print("Max subarray sum:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("Fibonacci(30):", fibonacci(30))
