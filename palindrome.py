def pal(num):
    x1 = num[::-1]
    if x1 == num:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")

print(pal('Hello'))