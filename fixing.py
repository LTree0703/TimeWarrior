import os

def fixing():
    try:
        while True:
            os.system("clear") #clear previous texts 
            x=input('\033[?25hType the following to fix the machine: I will not post any code related to this assignment on the internet or anywhere else.\n')
            if x=='I will not post any code related to this assignment on the internet or anywhere else.':
                print('Part 1 completed')
            else:
                input('error')
                continue        #loop again from the beginning when the player type it wrongly 

            x=input('Type the following to fix the machine: I will not give any assignment code to another student.\n')
            if x=='I will not give any assignment code to another student.':
                print('Part 2 completed')
            else:
                input('error')
                continue         #loop again from the beginning when the player type it wrongly 

            x=input("Type the following to fix the machine: I will not plagiarize someone else's work and turn it in as my own.\n")
            if x=="I will not plagiarize someone else's work and turn it in as my own.":
                print('Part 3 completed')
            else:
                input('error')   #loop again from the beginning when the player type it wrongly 
                continue

            x=input('Type the following to fix the machine: I promise to practice academic honesty.\n')
            if x=='I promise to practice academic honesty.':
                print('Final Part completed')
                print('loading.......')
                break           #exit the while loop and 
            else:
                input('error')  #loop again from the beginning when the player type it wrongly 
                continue  
        input('MACHINE FIXED!!  [Press enter to continue]')
    except KeyboardInterrupt:
        print('\x1b[2K'+'exiting game...') ##clearing the entire line and print exiting game when the player use KeyboardInterrupt which is Ctrl+C
