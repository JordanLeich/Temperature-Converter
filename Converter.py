# Made by Jordan Leich on 6/14/2020

import time


def restart():
    user_choice = str(input("Convert again (yes | no): "))
    print()

    if user_choice.lower() == 'yes' or user_choice.lower() == 'y':
        print("Restarting converter...")
        print()
        time.sleep(2)
        converter()

    elif user_choice.lower() == 'no' or user_choice.lower() == 'n':
        print("Ending converter...")
        print()
        time.sleep(2)
        quit()

    else:
        print("Invalid Input... Restarting Input Choice...")
        print()
        time.sleep(3)
        restart()


def converter():
    user_choice = int(
        input("Would you like to convert Celsius to Fahrenheit (1) or convert Fahrenheit to Celsius (2): "))
    print()

    if user_choice == 1:
        user_celsius = float(input("Celsius: "))
        print()
        fahrenheit = float(user_celsius * 1.8 + 32)
        print(user_celsius, "in Celsius equals", fahrenheit, "in Fahrenheit.")
        print()
        time.sleep(2)
        restart()

    elif user_choice == 2:
        user_fahrenheit = float(input("Fahrenheit: "))
        print()
        celsius = float(user_fahrenheit * 1.8 + 32)
        print(user_fahrenheit, "in Fahrenheit equals", celsius, "in Celsius.")
        print()
        time.sleep(2)
        restart()

    else:
        print("Invalid Input... Restarting Input Choice...")
        print()
        time.sleep(3)
        converter()


converter()
