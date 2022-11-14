import time, os, random
from story import story

def tutorial():
    os.system("clear")
    input('''
------------------- Getting started --------------------

Guideline:
                    *THIS IS A TRIAL*
In here, you'll have to answer several questions regard-
ing to ancient affairs to prove that you have sufficient 
knowledge about us. If you could answer all the questions
correctly, you'll be honoured a treasure loot, containing
one of our most proud work.
(Answers in both capital and small letters are acceptable)

-------- (Press enter if you are feeling great) ---------''')
    return

# main function
def start_game_two():
    # initiate
    os.system("clear")
    try:
        with open('./stories/entergame2.txt', 'r') as f:
            for i in f:
                for j in i:
                    print(j, end='', flush=True)
                    time.sleep(.002)
        time.sleep(0.5)
        tutorial()

        # structure of the question bank:
        # questions = {question_number: [question, answer, hint]}
        questions = {1: ['What famous structure was built during the old kingdom in Egypt?', 'sphinx', 'A Human Face and Lion body'],
                 2: ['What destroyed the ancient Roman city of Pompeii?', 'volcano', 'MAGMA COMES OUT FROM THIS'],
                 3: ['Which of the following is the place of having earliest written approximations of π \n(write down the alphabet of the answer)\na. Egypt \nb. Maya civilization  \nc. China \nd. Roman Empire ', 'a', 'ANSWER APPEARED IN OTHER QUESTION'],
                 4: ['Ancient Rome began growing in the area that is now ____?', 'italy', 'PLACE OF PIZZA AND SPAGHETTI'],
                 5: ['The Greeks had a lot of Gods. Who did they believe was the king of the Gods?', 'zeus','THUNDER USER'],
                 6: ['There is a palace nearby facing the sea, and there are 5 stairs between the palace and the entrance.\nIf one person can only take either one step or prime number of steps,\nhow many permutation of moves can one reach the palace from the entrance?', '14' , 'Take your time to find out:)']}
        answered = []
        num = 1
        onemoretime = False 
        # loop
        while True:
            os.system("clear")
            isCorrect = False
            # Printing out the question
            print(f"\033[?25hHere is question {num}. 😈")
            if onemoretime:
                print(f"\033[1m{questions[i][0]}\033[0m", end='')
            else:
                # randomly pick one question from the dictionary
                i = random.randint(1, len(questions))
                if i not in answered:
                    answered.append(i)
                else:
                    continue
                # print out the question
                time.sleep(0.5)
                for j in questions[i][0]:
                    print(f"\033[1m{j}\033[0m", end='', flush=True)
                    time.sleep(.015)
            # Ask for input
            print('\n\n(type .help for tutorial of the trial, or .quit to return to menu)')
            x = input("Your answer: ").lower()
            if x == '.help':
                onemoretime = True
                tutorial()
                continue
            elif x == '.quit':
                print('\033[?25l')
                return

            if x == questions[i][1]:
                isCorrect = True
            else:
                print("\033[91mWrong, try again.\033[0m")
                print(f"Here is the hint, ({questions[i][2]})")
                input("-------- (Press enter if you are feeling great) --------")
            if isCorrect: 
                onemoretime = False
                num += 1
                if len(answered) == 5: 
                    input('\033[1mExcellent work. Here is the TREASURE BOX.\033[0m')
                    break
                else:
                    print("\033[92mGood job. Lets move to next question.\033[0m")
                    input('-------- (Press enter to continue) --------')
            else:
                onemoretime = True
            # check if the enough questions were answered
        with open('./images/treasurebox.txt', 'r') as f:
            for i in f:
                print(i, end='', flush=True)
                time.sleep(.02)
        story('./stories/story2.txt')
        return('WIN')
    except KeyboardInterrupt:
        print('\nInterrupted by player, exiting game...')
        quit()
        
#start_game_two()
