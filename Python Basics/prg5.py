#Program to check whether a string is palindrome or not

s = input("Enter a word: ")

print("Palindrome") if s == s[::-1] else print("Not palindrome")
