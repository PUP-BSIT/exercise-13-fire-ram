import os
import random

def marc():
    os.system("cls")
    while True:
        print(f"\033[1;35m{'=' * 50}")
        print("Hello, I'm Marc D. Vesliño")
        print("1. Basic Information")
        print("2. Goals")
        print("3. Guessing Game")
        print("0. Exit")
        print(f"\033[1;35m{'=' * 50}")

        menu_choice = int(input("Enter your choice: "))
        
        if menu_choice == 0:
            break  

        match menu_choice:
            case 1:
                os.system("cls")
                print("Basic Information")
                print("Name: Marc D. Veslino")
                print("Age: 19")
                print("Nationality: Filipino")
                print("Status: Single")
                print("Birthday: May 4, 2005")
                input("Press enter to contiue")
            case 2:
                os.system("cls")
                print("Goals")
                print("1. Achieve stability across all aspects of life, including financial security and personal growth.")
                print("2. Maintain a healthy body and mind to ensure long-term well-being.")
                print("3. Provide for and support my family, ensuring their happiness and security.")
                print("4. Live with purpose and stay aligned with my true calling.")
                print("5. Give back to my community through acts of kindness and service.")
                print("6. Cultivate a strong and loving family bond.")
                print("7. Build a joyful and supportive family environment, where love and happiness thrive.")
                input("Press enter to continue")
            case 3:
                os.system("cls")
                print("Guessing Game")
                number = random.randint(1, 30)
                print("Guess the number between 1 and 30.")

                while True:
                    guess = int(input("Your guess: "))
                    if guess < number:
                        print("Too low")
                    elif guess > number:
                        print("Too high")
                    else:
                        print("You guessed it, Congratulation!")
                        break
                    
                input("Press enter to continue")
            case _: 
                print("Invalid Choice. Try Again.")
                input("\nPress Enter to continue.") 