s = "Python is a Programming Language"

result = ' ' .join(word[::-1] for word in s.split())
print(result)