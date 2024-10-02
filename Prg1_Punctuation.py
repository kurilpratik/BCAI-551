# Remove punctuation from user input

str = input("Enter a string ")
punct = ',.!'
newStr =""

for char in str:
    if char not in punct:
        newStr += char

print(newStr)