num = int(input("Enter a number: "))

if num > 50:
    print(num, "is greater than 50")
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")
else:
    print(num, "is not greater than 50")
