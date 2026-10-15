# Problem 6 – Countdown. 
# Write a program using a while loop that asks the user for a non-negative integer 
# and prints a countdown from that number to zero.



number = int(input("Enter a non-negative integer: "))


if number >= 0:


    while number >= 0:
        print(number)

        
        number = number - 1

    print("Countdown finished!")

else:
    print("Please enter a non-negative integer.")
