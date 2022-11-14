 # ENGG1330 Project: Time Warrior

## Creators of this game (in alphabetical order)
- Chu Yan Kiu (Jason)
- Lee Dongwook (Daniel)
- Pang Tin Hei (Livear)

### This is a mini text-based game made with python.

## 1. Getting Started 
***
- (A minimum terminal size of 85 rows times 30 columns is required)
- Type `python3 main.py` on the terminal to initiate the game.
- After command is received, a message would appear on the terminal:

        Before entering the game, please enlarge your terminal to at least 85(rows)x 30(columns).
        However, full screen is recommended for more immersive experience of the game.
        [Press enter if you are feeling great]

- After pressing enter, you will arrive at the game menu:

        ---------ENGG1330 Project: Time Warrior--------

        ## Game Functions ##
        ---1. Start
        ---2. Credit
        ---3. Exit

        --------------------------------------------------
        Choose your way (type in the number):

- Type the corresponding numbers of game functions to start the game, show the credit list or exit the game respectively.

- If you have typed 1 on the terminal, you will be prompted to type in the name of your character first (default is Dirk).
  Then you will be directed to the storyline. (Press enter whenever you want to move on to the next dialogue)

- When the dialogues are printing out, please avoid typing anything or pressing enter. Otherwise, the storyline or animations will be interrupted.


## 2. Gameplays
***
- After completion of the prologue, you will be directed to our main map, the Kit's Island. The full map is shown below:

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  (as you do not know how to swim, it is not possible for them to swim in the sea as shown)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         •                                ┎  unknown 
                                          ┕    place
        w w w w w     🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
        w w w w w     🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾
        w w w w w     🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾 (you can not step into it as it will trigger farmers)
        w w w w w     🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
        w w w w w     🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱🌱
        w w w w w     🌾🌾🌾🌾F A R M 🌾🌾🌾🌾🌾
        w w w w w     🌾D O N O T T O U C H 🌾🌾
        w w w w w                         👨 X🌾
        w w w w w                         👨 X🌾
        w w w w w     |--------|┏ ------┓ //  \
        w w w w w     ||STALL ||| H O   | //  \
        ┏ ------┓     ┏ ------┓ | M E   | //  \
        | S H  ||     | S H   | |       | //  \
        | O P  ||     | O P   | ┕ ------┛ //  \
        | ------|     | ------| ┏ ------┓ //  \
        | S H  ||     | S H   | | H O   | //  \
        | O P  ||     | O P   | | M E   | / 凵
        ┕ ------┛     ┕ ------┛ ┕ ------┛ ┕---┛
        ┏ ------┓     ┏ ------┓ w w w w w w w w 
        | S H  ||     | S H   ||w w w w w w w w 
        | O P  ||     | O P   ||w w w w w w w w 
        |      ||     | ========================
        ┕ ------┛     | M A R ||M A R ||M A R ||
        ┏ ------┓     | K E T ||K E T ||K E T ||
        | H O   |     | M A R ||M A R ||M A R ||
        | M E   |     | K E T ||K E T ||K E T ||
        ┕ ------┛     | ========================
        ========== * *| ========================

        SYMBOLS: 
        • : the player (you)
        ~ : sea (cannot enter)
        w : swaps (cannot enter)
        🌾 and 🌱 : the farm (cannot enter)
        unknown place : the cave (place for entering THE CAVE)
        * * : guards outside the questioning castle  (place for entering THE TRIAL)
        凵 : the ghost's nest (place for entering THE BATTLE: the final game)
        👨:  the resting farmers who won't allow you to enter the final game unless you get the magic arrow and another two treasure boxes (from game1 and game2)
        // and \\ : slopes (cannot enter)

- There are a lot of hidden dialogues inside this map. Try to discover all of them!

- You can move up, left, down, right by pressing w, a, s, d respectively on the keyboard.

- You may also press t and f to perform special actions!

- If you attempt to enter the sea for more than 3 times/home for 3 times/swaps for 4 times/farm for 5 times, you will die and 
  will be asked to choose to return to menu or exit the game.

- You can only enter THE BATTLE after completing THE CAVE and THE TRIAL.

- If you have completed THE BATTLE, you will be directed to the finale of the story.
  After that the whole game is finished and the game will exit automatically. 

- Type `python3 main.py` on the terminal if you want to try this game again. 

***
## (Three sub-games)

- If you do not understnad how to play the sub-games, you may type .help in game 2 and 3 or press h in game 1 to check the tutorial of that sub-game.

- If you have won the sub-game, you will no longer have access to it before you quit the game. Also, after entering game 3, you will not be able to return to the Island.

- Please note that pressing "w", "a", "s", "d" button for a long time inside the map will result in rapid movement of the character.
  Consequently, you may reach the boundary unconsciously and accidentally enter the "forbidden area". 
  Thus, it is suggested to press once only for everystep to explore the whole map.

- The path towards the battle (game 3) is somewhat hidden, so please be patient to find out the pathway to enter the gate!

- Your target is to get into the cave to complete the maze, the question castle to answer questions and the final gate to fight against the ghost in order to return to modern times.

## 3. Exiting the game
***
- Press ctrl+c to force quit the game at any time. 



