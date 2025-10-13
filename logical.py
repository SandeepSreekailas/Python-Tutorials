def is_palindrome(s):
    s = s.replace(" ", "").lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


input_string = "Madam"
if is_palindrome(input_string):
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")


# n = 5

# # Upper half
# for i in range(1, n + 1):
#     spaces = " " * (n - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)

# # Lower half
# for i in range(n - 1, 0, -1):
#     spaces = " " * (n - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)