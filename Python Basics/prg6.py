#Write a program to check if 2 words are anagram of each other or not

a = input("Enter the first word: ")
b = input("Enter the second word: ")

#Sanitizing the inputs
a = a.lower()
b = b.lower()
a = a.strip()
b = b.strip()


flag = -1
for l in a:
    if(len(a) != len(b)):
        flag = flag + 1
        break
    if l not in b:
        flag = flag + 1
        break

if(flag == -1):
    print("Anagram")
else:
    print("Not anagram")



# Enter the first word: bell
# Enter the second word: ebbl
# Anagram

