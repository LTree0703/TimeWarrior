import os, time

# read the player's name, store it, and move on to the prologue
def intro():
    player_name = input("WRITE DOWN THE NAME OF YOUR CHARACTER: ")
    if not player_name: # default name
        player_name = 'Dirk'
    with open('./stories/playername.txt', 'w') as f: # save the name into the file
        f.write(player_name)
    print("\033[?25l\033[92mCommand received......\033[0m")
    time.sleep(1)

    for i in ''.join('current_year = 2022\nfor i in range(1000):\n    current_year -= i\nreturn year\n...'):
        print(i, end='', flush=True)
        time.sleep(0.02)
    os.system("clear")
    mechmove_prologue()
    story('./stories/storystart.txt')
    time.sleep(.5)
    return

# animation
def mechmove_prologue():
    distance_from_top = 20
    distance_from_leftmost = 0
    i = 0.2
    while True:
        print("\n" * distance_from_top)
        print('          //\\\            ')
        print("         ______        ")
        print("         |time|   ")
        print("         |mach|        ")
        print("         |ine |    ")
        time.sleep(i)
        os.system('clear')  
        distance_from_top -= 1
        i -= 0.008
        if distance_from_top < 0:
            break
    return

def mechmove_finale():
    distance_from_top = 20
    distance_from_leftmost = 0
    i = 0.2
    while True:
        print("\n" * distance_from_top)
        print('          //\\\            ')
        print("         ______        ")
        print("         |time|   ")
        print("         |mach|        ")
        print("         |ine |    ")
        time.sleep(i)
        os.system('clear')  
        distance_from_top -= 1
        i -= 0.008
        if distance_from_top < 0:
            break
    for i in ''.join('- - - - - - - - f l y i n g - b a c k - t o - m o d e r n - - - - - -'):
        print(i, end='', flush=True)
        time.sleep(0.007)
    print('\n')
    for i in ''.join('        - - - - - - - - f l y i n g - b a c k - t o - m o d e r n - - - - - -'):
        print(i, end='', flush=True)
        time.sleep(0.007)
    print('\n')
    for i in ''.join('                 - - - - - - - - f l y i n g - b a c k - t o - m o d e r n - - - - - -'):
        print(i, end='', flush=True)
        time.sleep(0.007)
    print('\n')
    for i in ''.join('                        - - - - - - - - f l y i n g - b a c k - t o - m o d e r n - - - - - -'):
        print(i, end='', flush=True)
        time.sleep(0.007)
    print('\n')
    for i in ''.join('                 - - - - - - - - f l y i n g - b a c k - t o - m o d e r n - - - - - -'):
        print(i, end='', flush=True)
        time.sleep(0.007)
    print('\n')
    for i in ''.join('        - - - - - - - - f l y i n g - b a c k - t o - m o d e r n - - - - - -'):
        print(i, end='', flush=True)
        time.sleep(0.007)
    print('\n')
    for i in ''.join('- - - - - - - - f l y i n g - b a c k - t o - m o d e r n - - - - - -'):
        print(i, end='', flush=True)
        time.sleep(0.007)
    os.system('clear')  
    while distance_from_leftmost<90:    
        print(' '*distance_from_leftmost+'------\\')
        print(' '*distance_from_leftmost+'|time  \\')
        print(' '*distance_from_leftmost+'|machine\\')
        print(' '*distance_from_leftmost+'|TIME   /')
        print(' '*distance_from_leftmost+'|FLIES /')
        print(' '*distance_from_leftmost+'------/')
        time.sleep(0.05)
        os.system('clear')
        distance_from_leftmost += 1
    return

# read story files and print it out
def story(file):
    # initiate
    with open('./stories/playername.txt', 'r') as f:
        player_name = f.read()
        input('\033[?25l\033[1m[Press enter to continue the story]\033[0m')
    os.system("clear")

    # read through the story file
    with open(file, 'r') as f:
        for i in f:
            # recognize the key in the files
            if i == '\n':
                input()
            elif '&' in i: # stands for the player
                print(player_name, end='', flush=True)
                time.sleep(.1)
            elif '@' in i: # stands for the ghost
                with open('./images/ghost.txt', 'r') as g:
                    for j in g:
                        print(j, end='')
            elif '*' in i: # stands for treasure box
                with open('./images/treasurebox.txt', 'r') as tb:
                    for j in tb:
                        print(j, end='')
            elif '^' in i: # stands for another treasure box
                with open('./images/treasurebox2.txt', 'r') as tb2:
                    for j in tb2:
                        print(j, end='')
            elif '∫' in i: # stands for the time machine
                with open('./images/timemachine.txt', 'r') as tm:
                    for j in tm:
                        print(j, end='')
            else:
                print(i, end='', flush=True)
                time.sleep(.1)

