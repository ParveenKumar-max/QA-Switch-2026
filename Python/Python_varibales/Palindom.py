def palindom(string):
    if string == string[::-1]:
        return True
    else:
        return False

palindrome_string = input("Enter a string to check if it is a palindrome: ")
if palindom(palindrome_string):
    print(f"{palindrome_string} is a palindrome.")
else:
    print(f"{palindrome_string} is not a palindrome.")

# Another way to check for palindrome
def is_palindrome(s):
    return s == s[::-1] 

PalindomSecond = input("Enter a string to check if it is a palindrome (second method): ")
if is_palindrome(PalindomSecond):
    print(f"{PalindomSecond} is a palindrome.")
else:
    print(f"{PalindomSecond} is not a palindrome.")

# Another way to check for palindrome
def check_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Another way to check for palindrome
def palindrome_check(s):
    return s == ''.join(reversed(s)) 

PalindomThird = input("Enter a string to check if it is a palindrome (third method): ")
if check_palindrome(PalindomThird):
    print(f"{PalindomThird} is a palindrome.")
else:
    print(f"{PalindomThird} is not a palindrome.")   