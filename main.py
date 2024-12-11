from ourpackage import barcelos, veslino, consultado, andaya
import os

while True:
    os.system('cls')
    print("===============> Fire Ram <===============")
    print("(1) Kevin Joseph V. Barcelos")
    print("(2) Marc D. Veslino")
    print("(3) Kirby G. Consultado")
    print("(4) Gener A. Andaya")
    print("(5) Edriane O. Piadozo")
    print("(0) Exit ")
    user_choice = input("Enter your choice: ")

    if user_choice == '0':
        break
    
    match user_choice:
        case '1':
            barcelos.kevin()
        case '2':
            veslino.marc()
        case '3':
            consultado.kirby()
        case '4':
            andaya.gener()
        case '5':
            pass