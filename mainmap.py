import os, time, colorama
import sys, termios, tty
import game1,game2,game3
import retry 
from colorama import Fore, Back, Style
global gamemap1
global initial_pos
global illegal_attempts
global play_times
global easteregg
easteregg = {'easteregg': 0}
play_times = {'game1': 0, 'game2': 0, 'game3': 0} #storing how many times they have won the game 
illegal_attempts = {'swim': 0, 'farm': 0, 'grass': 0, 'home': 0} #storing no of attempts of commit suicide in different ways 
dialog_dict = {'swim': "In front of you is the sea, but you don't know how to swim!", 'farm1': 'You cannot step into the farm\nFarmers will be triggered if you do so!', 'farm2': "They are Realllllllllly Angryyyyyyyyyyy\nReally don't try it again!!!!!\n", 'swaps': '''This is swaps.\nLocal residents always say that it's full of poisonous snakes and insects\n-> \033[91mDO NOT ATTEMPT TO GET IN\033[0m''', 'home': "This is the home of others.\nStrongly recommend you not to disturb them\nyou will get into trouble if you bump into their home too many times", "wall":'''Don't bump into the walls!!'''}
initial_pos = [5,0]   #initial_pos[0] is y axis while initial_pos[1] is x axis
gamemap1 = [('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'),    #list that store the map 
          ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'),
          ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'),
          ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'),
          ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'),
      [' ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','┎  ','un','known'],
      ['  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','┕  ',' ',' place'],
      ['w ','w ','w ','w ','w ','  ','  ','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾''🌾','🌾'],
      ['w ','w ','w ','w ','w ','  ','  ','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾''🌾','🌾'],
      ['w ','w ','w ','w ','w ','  ','  ','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾','🌾''🌾','🌾'],
      ['w ','w ','w ','w ','w ','  ','  ','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱'],
      ['w ','w ','w ','w ','w ','  ','  ','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱','🌱'],
      ['w ','w ','w ','w ','w ','  ','  ','🌾','🌾','🌾','🌾','F ','A ','R ','M ','🌾','🌾','🌾''🌾','🌾'],
      ['w ','w ','w ','w ','w ','  ','  ','🌾','D ','O ','N ','O ','T ','T ','O ','U ','C ','H ','🌾','🌾'],
      ['w ','w ','w ','w ','w ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','👨 ',' ','  '],
      ['w ','w ','w ','w ','w ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','  ','👨 ',' ','  '],
      ['w ','w ','w ','w ','w ','  ','  ','|-','--','--','--','-|','┏ ','--','--','--','┓ ','\\','  ','//'],
      ['w ','w ','w ','w ','w ','  ','  ','||','ST','AL','L ','||','| ','H ','O ','  ','| ','\\','  ','//'],
      ['┏ ','--','--','--','┓ ','  ','  ','┏ ','--','--','--','┓ ','| ','M ','E ','  ','| ','\\','  ','//'],
      ['| ','S ','H ',' |','| ','  ','  ','| ','S ','H ','  ','| ','| ','  ','  ','  ','| ','\\','  ','//'],
      ['| ','O ','P ',' |','| ','  ','  ','| ','O ','P ','  ','| ','┕ ','--','--','--','┛ ','\\','  ','//'],
      ['| ','--','--','--','| ','  ','  ','| ','--','--','--','| ','┏ ','--','--','--','┓ ','\\','  ','//'],
      ['| ','S ','H ',' |','| ','  ','  ','| ','S ','H ','  ','| ','| ','H ','O ','  ','| ','\\','  ','//'],
      ['| ','O ','P ',' |','| ','  ','  ','| ','O ','P ','  ','| ','| ','M ','E ','  ','| ','/ ','凵',''],
      ['┕ ','--','--','--','┛ ','  ','  ','┕ ','--','--','--','┛ ','┕ ','--','--','--','┛ ','┕-','--','┛'],
      ['┏ ','--','--','--','┓ ','  ','  ','┏ ','--','--','--','┓ ','w ','w ','w ','w ','w ','w ','w ','w '],
      ['| ','S ','H ',' |','| ','  ','  ','| ','S ','H ','  ','||','w ','w ','w ','w ','w ','w ','w ','w '],
      ['| ','O ','P ',' |','| ','  ','  ','| ','O ','P ','  ','||','w ','w ','w ','w ','w ','w ','w ','w '],
      ['| ','  ','  ',' |','| ','  ','  ','| ','==','==','==','==','==','==','==','==','==','==','==','=='],
      ['┕ ','--','--','--','┛ ','  ','  ','| ','M ','A ','R ','  ','M ','A ','R ','||','M ','A ','R ','||'],
      ['┏ ','--','--','--','┓ ','  ','  ','| ','K ','E ','T ','  ','K ','E ','T ','||','K ','E ','T ','||'],
      ['| ','H ','O ','  ','| ','  ','  ','| ','M ','A ','R ','  ','M ','A ','R ','||','M ','A ','R ','||'],
      ['| ','M ','E ','  ','| ','  ','  ','| ','K ','E ','T ','  ','K ','E ','T ','||','K ','E ','T ','||'],
      ['┕ ','--','--','--','┛ ','  ','  ','| ','==','==','==','==','==','==','==','==','==','==','==','=='],
      ['==','==','==','==','==',' *',' *','| ','==','==','==','==','==','==','==','==','==','==','==','==']]

def entergame(new_y,new_x):
    if  (new_y == 23 and new_x == 18):        
            return(300) #return the values of y to inside the map function such that game 3 can start 
    if  (new_y == 5 and new_x == 18) or (new_y == 6 and new_x == 18):
            if play_times['game1'] == 0:    #check if whether the player has win that minigame and got the treasure box
                return(100) #return the values of y to inside the map such that game 1 can start 
            else:
                print("You have already played this game and received a treasure box. Play another game!")
                time.sleep(1)
    if  (new_y == 33 and (new_x == 5 or new_x == 6)):
        if play_times['game2'] == 0:
            print(Fore.RED+'Guards: HEY WHO ARE YOU????') #conversation between the guards and player
            time.sleep(1)
            print('Guards: STAY AWAY FROM THE CASTLE')
            time.sleep(0.5)
            print(Fore.CYAN+'Guards: Hand on.')
            print('Guards: Oh you are the guy finding treasure.')
            print("Guards: Wait a few seconds.")
            time.sleep(2)
            print('Okay You are permitted to go in, please get in.'+Style.RESET_ALL)
            time.sleep(2) 
            return(200) #return the values of y to inside the map such that game 2 can start 
        else:
            print("You have already played this game and received a treasure box. Play another game!") 
            time.sleep(1)
    if (new_y == 31 and new_x == 10):
        if easteregg['easteregg'] == 0:
            easteregg['easteregg'] += 1
            print('You discovered some rotten apples and durian heels!')
            time.sleep(1)
            print('Also')
            time.sleep(1)
            print('''There's a small paper under those rotten apples...''')
            print(Back.WHITE+Fore.BLUE + '''To the mysterious time warrior:                                                                       
                                       Remember to charge up your HP with eating durians, I've left              
                            plenty of them inside the gate of them ghost.Else you would be defeated
                            and nearly died like me in first trial.                                
                                                                    Best Regards,                  
                                                                        A handsome guy''' + Style.RESET_ALL)
            input('[Press enter to continue]')
            return(0)

def print_updated_map():
    os.system("clear") #clear up previous printed lines in terminal 
    if initial_pos[0]+5 <= 33:
        for i in range(initial_pos[0]-5, initial_pos[0]+6):  #loop the row of the map from 5 units upper to 5 units lower when 5 unit lower will not exceed the map boundary
            print(*gamemap1[i], sep='')
    if initial_pos[0]+5 > 33:                       #situation when the 5 units lower is outside the map boundary 
        for i in range(initial_pos[0]-5, initial_pos[0]+(35-initial_pos[0])):   #print up the map till the  last line of the map list 
            print(*gamemap1[i], sep='')
    print('\n_________________map_lower_boundary______________')

def move(move_x, move_y):
    new_pos_x, new_pos_y = None, None   #to ensure the previous temp store up location is cleared up
    if move_x == 0 and move_y == -1:   #W
        new_pos_y = initial_pos[0]-1; new_pos_x = initial_pos[1]        #temp store up the new position 
        initial_pos[0] = new_pos_y; initial_pos[1]=new_pos_x            #store up the new position 
        gamemap1[initial_pos[0]][initial_pos[1]], gamemap1[initial_pos[0]+1][initial_pos[1]] =' •', '  '      #changing the position of the player 

    if move_x == -1 and move_y == 0:        #A
        new_pos_y = initial_pos[0]; new_pos_x = initial_pos[1]-1
        initial_pos[0] = new_pos_y; initial_pos[1] = new_pos_x
        gamemap1[initial_pos[0]][initial_pos[1]], gamemap1[initial_pos[0]][initial_pos[1]+1] = ' •', '  '

    if move_x == 1 and move_y == 0:         #S
        new_pos_y = initial_pos[0]; new_pos_x = initial_pos[1]+1
        initial_pos[0] = new_pos_y; initial_pos[1] = new_pos_x
        gamemap1[initial_pos[0]][initial_pos[1]], gamemap1[initial_pos[0]][initial_pos[1]-1] = ' •', '  '

    if move_x == 0 and move_y == 1:         #D
        new_pos_y = initial_pos[0]+1; new_pos_x = initial_pos[1]
        initial_pos[0] = new_pos_y; initial_pos[1] = new_pos_x
        gamemap1[initial_pos[0]][initial_pos[1]], gamemap1[initial_pos[0]-1][initial_pos[1]] = ' •', '  '
    return(new_pos_y,new_pos_x)

def dead_conditions(acts):
    if acts == 'swim':      
        time.sleep(0.6)                                 
        print(f'Your desire to swim was too strong')        #print out the situation when the player attempts to swim too many times 
        time.sleep(1)
        print(f'You immersed into the water............')
        time.sleep(1)
        print(f'YOU SLEPT WITH THE FISHES!!')
        time.sleep(1)
        return retry.retry()                #return to death screen and retry program 
    if acts == 'farm':
        time.sleep(0.6)                             
        print(f'Farmers were really triggered')         #print out the situation when the player attempts to GET INTO THE FARM  too many times 
        time.sleep(0.6)
        print(f'You were hit by the very sharp rake')
        time.sleep(0.6)
        print(f'You felt very dizzy and the severe bleed did not stop')
        time.sleep(1)
        return retry.retry()
    if acts == 'Swaps':
        print('You bravely step into the swaps')                #print out the situation when the player attempts to get into swaps too many times 
        time.sleep(0.5)
        print('BUT YOUR BRAVERY DID NOT PAY OFF')
        time.sleep(0.4)
        print('You are bitten by the poisonous snakes and insects at the same time')
        print('ALSO, YOU ARE BEATEN BY THE SHREK (THE ONLY LEGENDARY SHREK ON THIS ISLAND)')
        time.sleep(2)
        return retry.retry()
    if acts == 'home':
        print('You annoyed the family in this home')            #print out the situation when the player attempts to annoy the resident too many times 
        time.sleep(1)
        print("\033[1mBANG BANG Shiu Shiu Shiu BANG BANG\033[0m")
        time.sleep(0.5)
        print('You are bitten by cooking Utensils')
        time.sleep(0.5)
        return retry.retry()

def check_conditions(char):  
    if char == 'w':
        if initial_pos[0]-1 < 5:            #check the postion of player after they moved  to see whether it is possible to move
                illegal_attempts['swim'] += 1               #record the illegal attmepts of the player into the dictionary storing the values 
                if  illegal_attempts['swim']  <3:               #check if player has exceed the limits or not 
                    print(dialog_dict['swim'])                  #print out the dialog stored in another dialog disctionary correspond to different situation 
                    return(1)                                   #return back to inside the map such that the player can not perform the movement in the map 
                if  illegal_attempts['swim'] == 3:              #situation when the player exceeds the limit 
                    return(2)                                   #reutrning the correspond value such that the correspond death sitaution can be run
        if 13 >= initial_pos[0]-1 >= 7 and initial_pos[1] > 6:
                illegal_attempts['farm'] += 1
                if illegal_attempts['farm'] < 3:                    #similar mechanism as upper 
                    print(dialog_dict['farm1'])
                    return(1)
                if 2 < illegal_attempts['farm'] < 5:
                    for i in dialog_dict['farm2']:
                        print(i, end='', flush=True)
                        time.sleep(.01)
                    return(1)
                if illegal_attempts['farm'] == 5:
                    return(3)
        if initial_pos[0]-1 == 28 and initial_pos[1]>=7:
            print(dialog_dict['wall'])
            time.sleep(0.5)
            return(1)
        return(0)   

    if char == 'a':  
        if initial_pos[0] < 7 and initial_pos[1]-1 < 0:
            print("-> \033[91mInvalid move, please try again.\033[0m")   #similar methodology is used as upper
            return(1)
        if initial_pos[1]-1 < 5:
            if 18 > initial_pos[0] >= 7:
                illegal_attempts['grass'] += 1
                if illegal_attempts['grass'] < 4:
                    print(dialog_dict['swaps'])
                    return(1)
                if illegal_attempts['grass'] == 4:
                    return(4)
            if 30 > initial_pos[0] > 17:
                print('This is the shop')
                time.sleep(1)
                print('BUT')
                time.sleep(0.75)
                print("You have nothing to trade!")
                return 1
        if 30 <= initial_pos[0] <= 33:
            if initial_pos[1]-1 <= 4:
                illegal_attempts['home'] += 1
                if  illegal_attempts['home'] < 3:
                    print(dialog_dict['home'])
                    return(1)
                if  illegal_attempts['home'] == 3:
                    return(5)
        if  16 <= initial_pos[0] <= 22 and initial_pos[1]-1 == 17 :
                return(6) 
        return(0)  

    if char == 's':
        if initial_pos[0]+1 > 6 and initial_pos[1] < 5:
            illegal_attempts['grass'] += 1
            if illegal_attempts['grass'] < 4:
                print(dialog_dict['swaps'])
                return(1)
            if illegal_attempts['grass'] == 4:
                return(4)
        if 12 > initial_pos[0]+1 >= 7: 
            if initial_pos[1] > 6:
                illegal_attempts['farm'] += 1
                if illegal_attempts['farm'] < 3:
                    print(dialog_dict['farm1'])
                    return(1)
                if 2 < illegal_attempts['farm'] < 5:
                    for i in dialog_dict['farm2']:
                        print(i, end='', flush=True)
                        time.sleep(.01)
                    return(1)
                if illegal_attempts['farm'] == 5:
                    return(3)
        if 6 < initial_pos[1] < 12:
            if initial_pos[0]+1 == 16: #when player attempts to approach the pizza stall
                print('This is the little stall selling illegal PINEAPPLE PIZZA.')
                time.sleep(0.5)
                print('Luckily (maybe), you got no coins to buy it lol.')
                time.sleep(1)
                return(1)
        if 11 < initial_pos[1] < 17:
            if 26 > initial_pos[0]+1 >= 16:
                illegal_attempts['home'] += 1
                if  illegal_attempts['home'] < 3:
                    print(dialog_dict['home'])
                    return(1)
                if  illegal_attempts['home'] == 3:
                    return(5)
        if initial_pos[0]+1 == 34:
            print("-> \033[91mInvalid move, please try again.\033[0m")     
            return(1)       
        if  16 <= initial_pos[0]+1 <= 22 and initial_pos[1] == 17 :
            return(6)
        if initial_pos[0]+1 == 33 and initial_pos[1] >= 7:
            print(dialog_dict['wall'])
            time.sleep(0.5)
            return(1)
        return(0)

    if char == 'd': 
            if 13 >= initial_pos[0] >= 7:
                if initial_pos[1]+1 >= 7:
                    illegal_attempts['farm']+=1
                    if illegal_attempts['farm']<3:
                            print(dialog_dict['farm1'])
                            return(1)
                    if 2 < illegal_attempts['farm'] < 5:
                            for i in dialog_dict['farm2']:
                                print(i, end='', flush=True)
                                time.sleep(.01)
                            return(1)
                    if illegal_attempts['farm']==5:
                            return(3)
            if 17 < initial_pos[0] < 29:
                if 17 > initial_pos[1]+1 >= 7:         #check whether player are trying to enter the shop or not 
                    print('This is the shop')
                    time.sleep(1)
                    print('BUT')
                    time.sleep(0.75)
                    print("You have nothing to trade!")
                    return 1
            if 28 < initial_pos[0] <= 32:       #situation when the player attempts to go more inside of the market
                if initial_pos[1]+1 > 11:
                    print('''It's too crowded, you can't go any further''') 
                    return(1)
            if initial_pos[1]+1 > 19:
                    print("-> \033[91mInvalid move, please try again.\033[0m")
                    return(1)
            if 16 <= initial_pos[0] <= 17 and initial_pos[1]+1 == 7: #check if player attempts to reach the pizza stall 
                print('This is the little stall selling illegal PINEAPPLE PIZZA.')
                time.sleep(0.5)
                print('Luckily(Maybe) you got no coins to buy it lol.')
                time.sleep(1)
                return(1)
            if 14 <= initial_pos[0] <= 15 and initial_pos[1]+1 == 17 :  #check if player has approach the farmers 
                if play_times['game1'] == play_times['game2'] == 1: #check whether the player has gathered two treasure boxes and magic arrows
                    print('Farmers:you have the magic arrow and two treasure boxes, you can go in to have your trial now.')
                    time.sleep(0.5)
                    return(0)
                else:
                    print('Farmers: You do not get two treasure boxes.') 
                    time.sleep(0.4)
                    print('Farmers: Show us two treasure boxes. Else, go back!!')
                    time.sleep(0.4)
                    return(1)
            if  16<=initial_pos[0] <= 22 and initial_pos[1]+1 == 19 :
                return(6)
            if  initial_pos[0]==33 and initial_pos[1]+1==7:
                print(dialog_dict['wall'])
                time.sleep(0.5)
                return(1)     
            return(0)

def inside_the_map():
    move_x, move_y = 0, 0; z = None
    attempt_swim, attempt_destroy_farm_or_grass = 0, 0
    stdin = sys.stdin.fileno()
    tattr = termios.tcgetattr(stdin)
    print_updated_map()         #print up the initial position of the player in the map when player enters 
    try:
        tty.setcbreak(stdin, termios.TCSANOW)
        while True:
            move_x, move_y = 0, 0
            char = ''
            char = sys.stdin.read(1)        #read the CHARACTER which the player clicks 
            if char == 'w':
                y = check_conditions(char)  #jump to the check_conditions function to check whether it is a possible legal move 
                if y == 0:                  #situation whne there is no problem to move 
                    move_x, move_y = 0, -1        # move_x is the movement on x axis while move_y is the movement of y-axis ##-1 of move y means move upper by 1 unit 
                    new_y, new_x = move(move_x, move_y)  #send the moving steps to change the position of the player inside the list 
                    entergame(new_y, new_x)               #check if the player is at the position to enter any games/ find out the easteregg 
                    initial_pos[0] = new_y; initial_pos[1] = new_x   #store up the position 
                    print_updated_map()             #print the updated pov of the player in the map 
                if y > 1 :
                    return(y)
            if char == 'a':
                y = check_conditions(char)
                if y == 0:
                    move_x, move_y = -1,0    # move_x for -1 means move left for one unit 
                    new_y, new_x = move(move_x, move_y)
                    initial_pos[0] = new_y; initial_pos[1] = new_x
                    z = entergame(new_y, new_x)
                    if type(z) == int:
                        if z > 0:
                            return(z)
                    print_updated_map()
                if y > 1 :
                    return(y)
            if char == 's':
                y = check_conditions(char)
                if y == 0:                    #situation when the player has a legal move
                    move_x, move_y = 0,1
                    new_y, new_x = move(move_x, move_y)
                    initial_pos[0] = new_y;initial_pos[1]=new_x
                    z = entergame(new_y, new_x)
                    if type(z) == int:
                        if z > 0:       #cheak if the player can enter anygame
                            return(z)
                    print_updated_map() #print out the updated 
                if y > 1 :
                    return(y)

            if char == 'd':
                y = check_conditions(char)
                if y == 0:
                    move_x, move_y = 1, 0
                    new_y, new_x = move(move_x, move_y)
                    z = entergame(new_y, new_x)
                    initial_pos[0] = new_y; initial_pos[1] = new_x
                    if type(z) == int:
                        if z > 0:
                            return(z)
                    print_updated_map()
                if y > 1 :
                    return(y)
            if char == 'f':         # when player press f
                print(Fore.BLUE+'You have pressed F to pray respect'+Style.RESET_ALL)
            if char == 't':
                print(Fore.GREEN+'YOU HAVE T-POSED IN THE MIDDLE OF THE PATH! LOL'+Style.RESET_ALL)
                print(Back.MAGENTA+Fore.RED+'   ◉   ')
                print(Back.MAGENTA+Fore.RED+'---|---')
                print(Back.MAGENTA+Fore.RED+'   |   ')
                print(Back.MAGENTA+Fore.RED+'  / \  '+Style.RESET_ALL)
                time.sleep(2.5)
                print_updated_map()
    except KeyboardInterrupt:
        print('Interrupted by player, exiting game...\033[?25h')
        # exit the python program
        sys.exit()
        termios.exit()
    finally:
        termios.tcsetattr(stdin, termios.TCSANOW, tattr)        

def main():
    initialize()
    while True:
        y = inside_the_map()
        if y == 2:
            gamemap1[initial_pos[0]][initial_pos[1]] = '  ' #first clear the original position 
            dead_conditions('swim')
            break
        elif y == 3:
            gamemap1[initial_pos[0]][initial_pos[1]] = '  ' #first clear the original position 
            dead_conditions('farm')
            break 
        elif y == 4:
            gamemap1[initial_pos[0]][initial_pos[1]] = '  ' #first clear the original position 
            dead_conditions('Swaps')
            break
        elif y==5:
            gamemap1[initial_pos[0]][initial_pos[1]] = '  ' #first clear the original position 
            dead_conditions('home')
            break
        elif y == 6:
            print('THE SLOPE IS TOO STEEP,YOU CAN NOT CLIMB UP!')       #show can not climb up the slope 
            time.sleep(1)
        elif y == 100:
            g1condition = game1.start_game_one()
            if g1condition == 'WIN':
                play_times['game1'] = 1               #change the play times in which it will make the player impossible to access to the game minigame again 
        elif y == 200:
            g2condition = game2.start_game_two()
            if g2condition == 'WIN':
                play_times['game2'] = 1               #change the play times in which it will make the player impossible to access to the game minigame again 
        elif y == 300:
            g3condition = game3.start_game_three()
            if g3condition == 'WIN':
                play_times['game3'] = 1
def initialize(): #function that reset all values when player dies
    gamemap1[initial_pos[0]][initial_pos[1]] = '  '    
    initial_pos[0], initial_pos[1] = 5,0         #reset to the original position 
    play_times['game1'] = 0; play_times['game2'] = 0; play_times['game3'] = 0; easteregg['easteregg'] = 0
    illegal_attempts['swim'] = 0; illegal_attempts['farm'] = 0; illegal_attempts['grass'] = 0; illegal_attempts['home'] = 0  #reset all other values and illegal attempts
    gamemap1[5][0] = ' •'
    return
