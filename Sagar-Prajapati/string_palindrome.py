

def isPalindrome(str):
    rev_str = str[::-1]
    if rev_str == str:
     print("String is Palindrome")
    else:
        print("String is not palindrom")

str = "abba"
print(isPalindrome(str))
