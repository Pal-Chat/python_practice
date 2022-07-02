from traceback import print_tb


winning_number = 14
number= int(input("Enter the number between 1-100 : "))
if winning_number == number:
    print("YOU WIN !!!")
else:
    if number <= winning_number:
        print("Too low")
    else:
        print("too high")
