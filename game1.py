import os, random, time
import sys, termios, tty

from story import story

class Cave: # constructing a new data containing all the necessary information of game 1
    def __init__(self, height, width):
        self.height = height # height of the cave
        self.width = width # width of the cave
        self.walls = [(y, x) for x in range(width) for y in range(height) if x == 0 or x == width-1 or y == 0 or y == height-1]
        self.blocks = []
        self.traps = []
        self.player = (1, 1)
        self.start = (1, 1)
        self.finish = (height-2, width-2)
        self.restricted_area = (self.finish, self.player, (1, 2), (2, 1), (height-2, width-1), (height-1, width-2)) # area that should not be putting blocks or traps 
    
    def move_player(self, move): # determine the outcome according to each movement of the player
        x = self.player[0]
        y = self.player[1]
        pos = None

        # check for input
        if len(move) != 1:
            print("->\033[91mInvalid move, please try again.\033[0m")
            input("(Press enter if you are ready)")
            return
        if move[0] == 'w': pos = (x - 1, y)
        elif move[0] == 'a': pos = (x, y - 1)
        elif move[0] == 's': pos = (x + 1, y)
        elif move[0] == 'd': pos = (x, y + 1)
        else: pos = (x, y) 

        # determine the outcome of this position
        if pos in self.walls or pos in self.blocks:
            return
        elif pos in self.traps:
            self.player = pos
            os.system("clear")
            make_map(self)
            print("-> \033[91mYou have stepped on a trap:(\033[0m")
            input("-------- (Press enter to try again) --------")
            self.player = self.start
        else: 
            self.player = pos
            
def generate_blocks(map: Cave):
    blocks = []
    for x in range(0, map.height):
        for i in range(2, random.randint(map.height-9, map.height-4)):
            y = random.randint(1, map.width-1)
            if (x, y) not in map.restricted_area:
                blocks.append((x, y))
    return blocks

def generate_traps(map):
    traps = []
    for x in range(0, map.height-1, 2):
        for i in range(2, random.randint(map.height-8, map.height-2), 2):
            y = random.randint(1, map.width-1)
            if (x, y) not in map.blocks and (x, y) not in map.restricted_area:
                traps.append((x, y))
    return traps

def make_map(map): 
    # to generate/update the maze and store it into a file
    with open("./images/game1map.txt", "w") as f:
        for i in range(map.height):
            if i == 0 or i == map.height-1:
                f.write('+')
            elif i == 1:
                f.write('>')
            else:
                f.write('|')
            for j in range(1, map.width-1):
                f.write(' ')
                if (i, j) == map.player and (i, j) in map.traps:
                    f.write('\033[91m*\033[0m')
                elif (i, j) == map.player:
                    f.write('\033[95m@\033[0m')
                elif i == 0 or i == map.height-1:
                    f.write('-')
                elif (i, j) in map.blocks:
                    f.write('ඞ')
                else:
                    f.write(' ')
            f.write(' ')
            if i == 0 or i == map.height-1:
                f.write('+')
            elif i == map.height - 2:
                f.write('\033[92m⚑\033[0m')
            else:
                f.write('|')
            f.write('\n')

    # read input from file and print it out
    with open("./images/game1map.txt", "r") as f:
        for i in f:
            print(i, end='')

def tutorial():
    os.system("clear")
    input('''
------------------- Getting started --------------------

\033[95m@\033[0m --> the player
\033[92m⚑\033[0m --> the goal
ඞ --> blocks (which you cannot go through)
\033[91m*\033[0m --> traps (that will take your life)
\033[1mPress w, a, s, d to move up, left, down, right respectively \033[0m

Guideline:
                   *THIS IS A CAVE*
In this cave, you need to arrive at the green flag ⚑, but 
on the journey you will encounter lots of hidden traps *.
If you step on the trap, you will have to start at the
starting point again. So in this game, try your best to 
remember all the traps in the cave and reach the goal!

* Please note that the cave is randomly generated.
-------- (Press enter if you are feeling great) ---------''')
    return

# main function
def start_game_one():
    # initiate
    os.system("clear")
    with open('./stories/entergame1.txt', 'r') as f:
        for i in f:
            for j in i:
                print(j, end='', flush=True)
                time.sleep(.002)
    time.sleep(0.5)
    tutorial()
    start_time = time.time()
    stdin = sys.stdin.fileno()
    tattr = termios.tcgetattr(stdin)
    
    map = Cave(15, 35) 
    map.blocks = generate_blocks(map)
    map.traps = generate_traps(map)
    # loop
    try:
        tty.setcbreak(stdin, termios.TCSANOW)
        while True:
            os.system("clear")
            make_map(map)
            end_time = time.time()
            print('--> Time elapsed:', "%.2f"%(end_time-start_time))
            print("(type h for tutorial of the cave, type q to return to menu)")
            print('--> Choose your way...\033[?25l')
            move = sys.stdin.read(1) # 
            if move == 'h':
                tutorial()
                continue
            elif move == 'q':
                return
            map.move_player(move)
            if map.player == map.finish:
                os.system("clear")
                make_map(map)
                print('--> Time elapsed:', "%.2f"%(end_time-start_time)) # to show the time elapsed using the time module
                print('\033[1mCongratulations, you have reached the flag!!\033[0m\033[?25h')
                story('./stories/story1.txt')
                return('WIN')
    except KeyboardInterrupt: 
        print('\nInterrupted by player, exiting game...\033[?25h')
        sys.exit()
        termios.exit()
    finally:
        termios.tcsetattr(stdin, termios.TCSANOW, tattr)

#start_game_one()
