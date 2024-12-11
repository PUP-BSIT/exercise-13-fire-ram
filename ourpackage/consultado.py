from colorama import Fore
import os

def kirby():
    while True:
        os.system("cls")
        print(Fore.GREEN + "    SOMETHING ABOUT ME")
        print(Fore.RESET + "\n 1. Personal information")
        print(" 2. My Favorite Quotes")
        print(" 3. Motivational Story")
        print(" 4. Comment from Barcelos")
        print(" 5. Comment from Veslino")
        print(Fore.RED + "\n                    0 - Exit")
        print(Fore.RESET + "------------------------------")
        
        choice = input(" Enter your choice: ")
        if choice == '0':
            break
        
        match(choice):
            case '1':
                os.system("cls")
                print(" Hi there! I am Kirby Gonzales Consultado.")
                print(" Currently studying at Polytechnic University")
                print(" of the Philippines, Taguig Branch.")
                print(" Taking a Diploma Course in Information Technology.")
                print(Fore.CYAN + "\n--- More Info -----------------------------------------\n")
                print(" Age\t\t|  19 Years Old")
                print(" Birthdate\t|  September 10, 2005")
                print(" Email Address\t|  kirbyconsultado@gmail.com")
                print(" GitHub\t\t|  https://github.com/consultado-kirby")
                input(Fore.RESET + "\n Press enter to continue.")
            case '2':
                os.system("cls")
                print("\n -- Quote 1 -------------------------------\n")
                print(Fore.YELLOW + "\t   Start where you are.")
                print("\t    Use what you have.")
                print("\t     Do what you can.")
                print(Fore.RESET + "\n                   - Arthur Ashe")
                print("\n -- Quote 2 -------------------------------\n")
                print(Fore.YELLOW + "\tIf you can change your mind,")
                print("\t you can change your life.")
                print(Fore.RESET + "\n                   - Williams James")
                print("\n -- Quote 3 -------------------------------\n")
                print(Fore.YELLOW + "\t   My mission in life is not")
                print("\tmerely to survie, but to thrive.")
                print(Fore.RESET + "\n                   - Maya Angelo")
                print("\n -- Quote 4 -------------------------------\n")
                print(Fore.YELLOW + "\tDo not wait for opportunity.")
                print("\t        Create it.")
                print(Fore.RESET + "\n                   - Arthur Ashe")
                print("\n -- Quote 5 -------------------------------\n")
                print(Fore.YELLOW + "\t  Don't talk, just act.")
                print("\t  Don't say, just show.")
                print("\tDon't promise, just prove.")
                print(Fore.RESET + "\n                   - Don Hornsby")
                print("\n -- Quote 6 -------------------------------\n")
                print(Fore.YELLOW + "\t    I never lose.")
                print("\tEither I win or learn.")
                print(Fore.RESET + "\n                   - Nelson Mandela")
                input("\n Press enter to continue.")
            case '3':
                os.system("cls")
                print(Fore.GREEN + " A short story that built my motivation to thrive and become successful.")
                print(Fore.RESET + "\n----------------------------------------------------------------------------------------------------------\n")
                print(Fore.MAGENTA + "                                          The Star Student\n")
                print(Fore.RESET + "      A boy named Thomas struggled with his studies and was often scolded by teachers for being slow.")
                print(" One day, his teacher told him he was too dumb to learn anything. Heartbroken, Thomas went home and")
                print(" told his mother. She removed him from school and taught him herself.")
                print("\n      Years later, Thomas Edison became one of the greatest inventors in history, credited with the")
                print(" invention of the light bulb. His mother’s belief in him and his own determination to learn proved that")
                print(" hard work and persistence could overcome any obstacle.")
                print("\n-------------------------------------------------- This story is based on the life of Thomas Edison. -----")
                input("\n Press enter to continue.")
            case '4':
                print("Nice codes. Keep up the good work. - Barcelos")
                input("\n Press enter to continue.")
            case '5':
                print("I like the functionalities of your code. - Veslino")
                input("\n Press enter to continue.")
            case _:
                input("\n Invalid choice. Try again.")
    return ""