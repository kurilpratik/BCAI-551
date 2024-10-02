# Sort the words in aplhabetical order based on the first letter

str = input("Enter a string ")

lowercase = str.lower()

list = lowercase.split()

list.sort()

list = ' '.join(list)

print(list)