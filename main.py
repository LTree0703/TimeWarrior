import time, os

import mainmap, story

def menu():
    while True:
        os.system("clear")
        with open("intro/intro.txt", 'r') as intro:
            for i in intro:
                print(i, end='')
        n = input("Choose your way (type in the number): ")
        # start
        if n == '1':
            story.intro()
            mainmap.main() 
        # credit            
        elif n == '2':
            os.system("clear")
            with open("intro/credit.txt", "r") as f:
                for i in f:
                    print(i, end='')
            input()
        # exit
        elif n == '3':
            print("--------Goodbye:) Hope you will embark on this wonderful adventure once again.--------")
            time.sleep(1.25)
            os.system("clear")
            quit()
            
        else:
            os.system("clear")
            print("--------\033[91mThere is no such way, please choose again.\033[0m--------")
            continue

# main function
def time_warrior():
    try:
        # initiate
        print('Before entering the game, please enlarge your terminal to at least 85(rows)x30(columns)')
        print('However, full screen is recommended for more immersive experience of the game.')
        input('[Press enter if you are feeling great]')
        # loop
        while True:
            os.system("clear")
            menu()
    except KeyboardInterrupt:
        print('\nInterrupted by player, exiting game...\033[?25h')
        quit()
        
time_warrior()

