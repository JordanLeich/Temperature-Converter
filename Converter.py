# Made by Jordan Leich on 6/14/2020

import time
import restart


def converter():
    try:

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
            restart.restart()

        elif user_choice == 2:
            user_fahrenheit = float(input("Fahrenheit: "))
            print()
            celsius = float(user_fahrenheit * 1.8 + 32)
            print(user_fahrenheit, "in Fahrenheit equals", celsius, "in Celsius.")
            print()
            time.sleep(2)
            restart.restart()

        else:
            print("Invalid input... Restarting input choice...")
            print()
            time.sleep(3)
            converter()

    except:
        print()
        print("Error found... Restarting input choice...\n")
        time.sleep(3)
        converter()


converter()
