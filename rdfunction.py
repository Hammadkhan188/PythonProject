import  random as rd
import sys

# City_name=["Karachi","islamabad","lahore","Swat","peshwar","Gilgit","Hyderabad","Multan","Rawalpindi","Balochistan"]
# print(rd.sample(City_name,3))
# rd.shuffle(City_name)
# print(rd.choice(City_name))
# print(City_name)




import random as rd
import sys

print("******* Random Number Guessing Game ********\n")
computer_number = rd.randint(1, 20)
lives = 3

while lives > 0:
    try:
        user_input = int(input("Enter any number between 1 - 20: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if user_input == computer_number:
        print("🎉 Congratulations! You've guessed it correctly!")
        sys.exit()
    else:
        lives -= 1
        if user_input > computer_number:
            print("* Hint: Try a lower number.")
        elif user_input < computer_number:
            print("* Hint: Try a higher number.")

        if lives == 0:
            print("❌ Lives Ended. Game Over!")
            print(f"The correct number was {computer_number}.")
        else:
            print(f"❤️ {lives} lives remaining.\n")
