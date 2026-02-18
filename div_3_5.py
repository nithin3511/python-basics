n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both 3 and 5")

elif n % 3 == 0:
    print("Divisible by 3 only")

elif n % 5 == 0:
    print("Divisible by 5 only")

else:
    print("Not divisible by 3 or 5")
