import os, random, time
import colorama
from story import story, mechmove_finale
from fixing import fixing

class Battle: # constructing a new data containing all the necessary information of game 3
    def __init__(self, playerHP, playerMP, ghostHP) -> None:
        self.playerHP = playerHP
        self.playerMP = playerMP
        self.ghostHP = ghostHP
        self.player_isDefending = False

# skills of the player
def playermove(b, move):
    if move == 1: #if player choosed first skill
        os.system("clear") #clear the screen
        print("\033[1mYOUR TURN\033[0m\nYou have chosen:", move) #print the bold name of skill to emphasize
        b.ghostHP -= 2

        print('             ')
        print('Glad to put sharp fork in my bag!') #skill explanation
        print('           ')
        print(' ||||      ')
        print(' ||||      ')
        print(' \__/      ') 
        print('  II       ')
        print('  II       ')
        print('  II       ')
        print('  II       ')
        print('  II       ')
        print('             ')
        print('Damage: 2 / used MP: 0') #values of skill
        
    elif move == 2: #if player choosed second skill
        if b.playerMP < 2: #make player cannot use this skill if player has MP less than 2
            return False
        else:
            os.system("clear")
            print("\033[1mYOUR TURN\033[0m\nYou have chosen:", move) 
            b.ghostHP -= 4 #decrease the HP of Ghost
            b.playerMP -= 2 #decrease the MP of Player

            print('Smells bad.....')
            print('                         ')
            print('  ,--./,-.       ')
            print(' / #      \'     ')
            print(' |     #  |     ')
            print(' \        /      ')
            print('  `._,._,''      ')   
            print('                         ')
            print('                         ')
            print('Damage: 4 / used MP: 2') 
            
            
    elif move == 3:
        if b.playerMP < 5:
            return False
        else:
            os.system("clear")
            print("\033[1mYOUR TURN\033[0m\nYou have chosen:", move)
            b.ghostHP -= 6
            b.playerMP -= 5
            print('                         ')
            print('   It looks cool!   ')
            print('                         ')
            print(' >>>>>>>_____________________\`-._ ')
            print(' >>>>>>>                     /.-'' ')
            print('                         ')
            print('Damage: 6 / used MP: 5')
            
            
    elif move == 4:
        if b.playerMP < 9: 
            return False
        else:   
            os.system("clear")
            print("\033[1mYOUR TURN\033[0m\nYou have chosen:", move)
            b.ghostHP -= 7
            b.playerMP -= 9

            print('                         ')
            print('     +--------------+    ')
            print('     |.------------.|    ')
            print('     ||pythonpython||    ')
            print('     ||pythonnomore||    ')
            print('     ||nomorepython||    ')
            print('     |+------------+|    ') 
            print('     +-..--------..-+    ')
            print('    / /============\ \   ')
            print('   / /==============\ \  ')
            print('  /____________________\ ')
            print('                         ')
            print('                         ') 
            print('Damage: 7 / used MP: 9') 
            
    elif move == 5:
        os.system("clear")
        print("\033[1mYOUR TURN\033[0m\nYou have chosen:", move)
        b.playerHP += 3
        b.playerMP += 3
        print('  OOPS.. smell is too strong... ')
        print('                         ')
        print('                          ')
        print('          ,^-"-^.         ')
        print('         /  ,-.  \\        ')
        print('        <  (:::)  >       ')
        print('        |  (:::)  |       ')
        print('         < `-\\/  /        ')
        print('          `-.--.>         ')
        print('                          ')
        print('Damage: 0 / added HP: 3 / added MP: 3 ')
    
    elif move == 6:
        if b.playerMP < 2:
            return False
        else:
            os.system("clear")
            print("\033[1mYOUR TURN\033[0m\nYou have chosen:", move)
            b.player_isDefending = 2
            b.playerMP -= 2
            print("You will withstand the attack in the following turn.")
            print(' __________________')
            print('|       | |       |')
            print('|       | |       |')
            print('|_______| |_______|')
            print('|_______   _______|')
            print('|       | |       |')
            print(' \      | |      /') 
            print('  \     | |     / ')
            print('   \    | |    /  ')
            print('    \   | |   /   ')
            print('     ---------    ') 
            print('                     ')
    return True

# skills of the ghost
def ghostmove(b, move):
    os.system("clear")
    print("\033[1mTHE GHOST'S TURN\033[0m")
    if move == 1:
        print('(needles are created, surrounding the ghost) ')
        print('                                ')
        print('   ㅗㅜㅗㅜㅗㅗㅗㅗㅜㅗㅗㅗㅜㅗㅜ   ')
        print('   ㅓㅓ     \ ㅣXX ㅣ /    ㅏㅏ    ' )
        print('   ㅓㅓ      \ㅣXX ㅣ/     ㅏㅏ     '  )
        print('   ㅓㅓ     (  O  O  )    ㅏㅏ      ')
        print('   ㅓㅓ      (  鬼  )      ㅏㅏ     ')   
        print('   ㅓㅓ       XXXXXX      ㅏㅏ     ' )
        print('   ㅗㅗㅗㅗㅗㅗㅜㅜㅜㅜㅜㅜㅜㅗㅜ      ')
        print('                                     ')
        
        print('                                     ')
        if b.player_isDefending == 1: #if player used the skill "defend", make player to get 0 damage.""
            print('Your shield has protected you from the attack of the ghost.\nPlayer HP: -0')
        else:
            print('Player HP: -4')
            b.playerHP -= 4
        
    elif move == 2:
        print('(Ghost called his demon ally)')
        print('                     ')
        print('   (\-"```"-/)   ')
        print('   //^\   /^\   ')
        print('  ;/ ~_\ /_~ \; ')
        print('  |  / \\Y/ \\  | ')
        print(' (,  \\0/ \\0/  ,)')
        print('  |   /   \   | ')
        print('  | (_\\._./_) | ')
        print('   \\ \\v-.-v/ /  ')    
        print('    \\ `===` /    ')
        print('                     ')
        print('                                 ')
        if b.player_isDefending == 1:
            print('Your shield has protected you from the attack of the ghost.\nPlayer HP: -0 / Player MP: -0')
        else:
            b.playerHP -= 1
            if b.playerMP < 4:
                print(f'Player HP: -1 / Player MP: -{b.playerMP}') #This skill absorbs 5 MP from player. So,if player has MP less then 4, make players MP 0. 
                b.playerMP = 0
                print('I cannot absorb sufficient MP...Grr...')
            else:
                print('Player HP: -1 / Player MP: -4')
                b.playerMP -= 4
        
    elif move == 3:
        print('(Ghost summoning the strange spot)')
        print('           _          ')
        print('          | |         ')
        print('          | |         ')
        print('        O | | O       ')
        print('     _____| |_____    ')
        print('    |_____   _____|   ')
        print('        O | | O       ')
        print('          | |         ')
        print('          | |         ')
        print('          |_|         ')
        print('                       ')
        print('                       ')
        if b.player_isDefending == 1:
            print('Your shield has protected you from the attack of the ghost.\nPlayer HP: -0')
        else:
            print('Ghost HP: +2 /player HP: -3')
            b.playerHP -= 3
            b.ghostHP += 2 
    return

def tutorial():
    os.system("clear")
    input('''
------------------- Getting started --------------------

Guideline:
                   *THIS IS A BATTLE*
In here, you'll fight with the ghost that you met at 
the beginning of this game in order to get last treasure box.

TIP: eat durian when you are URGENT

inital You ==> HP: 13 / MP: 10
inital Ghost ==> HP: 15 / MP: ထ

You have 6 skills in total:

1. fork attack             ==>     Damage: 2 / MP required: 0

2. Throw rotten apple     ==>      Damage: 4 / MP required: 2

3. Shooting magic arrow   ==>      Damage: 6 / MP required: 5

4. Sending ENGG1330 assignment ==> Damage: 7 / MP required: 9

5. Have a bite of a durian ==>     HP: +3    / MP: +3

6. Defense ==>                                 MP required: 2 

-------- (Press enter if you are feeling great) ---------''')
    return
    
# the main function
def start_game_three():
    # initiate the game
    os.system("clear")
    try:
        with open('./stories/entergame3.txt', 'r') as f: #opening the picture of gate while enter the game3
            for i in f:
                for j in i:
                    print(j, end='', flush=True)
                    time.sleep(.002) 
        time.sleep(0.5)
        b = Battle(13, 10, 15)  
        turn = 0
        tutorial()
        # loop
        while True:
            os.system("clear")
            print('\033[1mFIGHT!\033[0m')
            print(f"\n\033[1mPlayer HP: {b.playerHP} \tPlayer MP: {b.playerMP} \tGhost HP: {b.ghostHP}\033[0m")
            if turn == 0: # player's turn
                try: #below is the skill set
                    print('''
\033[1mYOUR TURN\033[0m 
     *Choose your way*                  
1. [Normal attack with fork] 

2. [Throwing rotten apple]

3. [Shooting magic arrow]

4. [Sending ENGG1330 assignments]

5. [Have a bite of Durian]

6. [Defense]

(type .help for tutorial of the battle, or .quit to return to menu)
Choose your skill: ''', end='')
                    player_move = input()
                    if player_move == '.help':
                        tutorial()
                        continue
                    elif player_move == '.quit':
                        break
                    if int(player_move) > 6 or int(player_move) < 1:
                        print('--> \033[91mInvalid input, please try again\033[0m')
                        input('-------- (Press enter if you are feeling great) --------')
                        continue
                    if not playermove(b, int(player_move)):
                        print('\033[91mI need more MP to use this skill!\033[0m')
                        input('-------- (Press enter to continue) --------')
                        continue
                except ValueError:
                    print('--> \033[91mInvalid input, please try again\033[0m')
                    input('-------- (Press enter if you are feeling great) --------')
                    continue

            else: # the ghost's turn
                print("\n\033[1mTHE GHOST'S TURN\033[0m")
                print("The ghost is deciding his moves. (Do not type anything)")
                for i in '......':
                    print(i, end='', flush=True)
                    time.sleep(.5)
                print()
                ghost_move = random.randint(1,3) # boss's skill is randomly generated
                ghostmove(b, ghost_move)
            input("\n-------- (Press enter to continue) --------")

            # check winning/losing conditions
            if b.playerHP < 1:
                print("You lose:(")
                while True:
                    with open("./images/death.txt", 'r') as f: #open dead image
                        os.system("clear")
                        for i in f:
                            print(i, end='')
                        print()
                    time.sleep(0.5)
                    retry = input('Retry? (y/n): ')
                    if retry == 'y':
                        b = Battle(13, 10, 15)   # restart the battle with resetting the hp of player , mp of player,hp of enemies respectively
                        turn = 1
                        break
                    elif retry == 'n': return
                    else: continue
            elif b.ghostHP < 1:
                print('*The ghost was defeated...*')
                story('./stories/story3.txt')
                fixing()                       #starts the final task which is fixing the time machine 
                mechmove_finale()                     #show out the animation of the time machine 
                print("Congratulations! You have already completed the adventure. Looking forward to seeing you next time:-D")
                print('''   ******    *******   ****     **   ********  *******       **     ********** **     ** **           **     ********** **   *******   ****     **  ********
  **////**  **/////** /**/**   /**  **//////**/**////**     ****   /////**/// /**    /**/**          ****   /////**/// /**  **/////** /**/**   /** **////// 
 **    //  **     //**/**//**  /** **      // /**   /**    **//**      /**    /**    /**/**         **//**      /**    /** **     //**/**//**  /**/**       
/**       /**      /**/** //** /**/**         /*******    **  //**     /**    /**    /**/**        **  //**     /**    /**/**      /**/** //** /**/*********
/**       /**      /**/**  //**/**/**    *****/**///**   **********    /**    /**    /**/**       **********    /**    /**/**      /**/**  //**/**////////**
//**    **//**     ** /**   //****//**  ////**/**  //** /**//////**    /**    /**    /**/**      /**//////**    /**    /**//**     ** /**   //****       /**
 //******  //*******  /**    //*** //******** /**   //**/**     /**    /**    //******* /********/**     /**    /**    /** //*******  /**    //*** ******** 
  //////    ///////   //      ///   ////////  //     // //      //     //      ///////  //////// //      //     //     //   ///////   //      /// ////////  ''')
                time.sleep(3)
                quit()

            # switching turns
            if turn == 0: turn = 1
            else: turn = 0
            if b.player_isDefending > 0: b.player_isDefending -= 1
    except KeyboardInterrupt:
        print('\nInterrupted by player, exiting game...\033[?25h')
        quit()


