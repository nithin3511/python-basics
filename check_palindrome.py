s= input("enter the string ")

rev=""
for ch in s:
  rev=ch+rev


if(rev==s):
  print("given string is palindrome")
else:
  print("not a palindrome ")