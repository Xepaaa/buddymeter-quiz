'''
Questions/Answers/Clues:

Question 1: What is his all-time favourite Food?
Answer: Spring Rolls
Riddle: The east asian version of a Samosa - Has the potential to roll - But not the potential to spring...

Question 2: What brand Shoes is he always wearing?
Answer: Adidas
Riddle: Who sponsors Real Madrid - Is in close competition with Nike - Always boasts too many stripes

Question 3: How many siblings does he have? 
Answer: 5
Riddle: Picture the number of corners in a star - Recall the number of members in one direction

Question 4: What's his favourite Colour?
Answer: Purple (purr-ple)
Riddle: A cats Favourite colour - Is associated with royalty - Comes from a the mucus of a snail

Question 5: What's his favourite Sport?
Answer: Volleyball
Riddle: What sport involves serving, but not by a waiter; and an ace but not a card

Question 6: What's his favourite TV show?
Answer: Breaking bad
Riddle: DEA - Cooking - Chemistry

Question 7: Who is his favourite superhero?
Answer: Batman
Riddle: The Riddler - The Detective - The Dark

Question 8: In what city was he born?
Answer: Rotterdam
Riddle: Has the largest port in Europe - An observation tower called the Euromast - Hosts Feyenoord
'''


def welcome_message():
	print('Heyy, welcome to my Quiz!')
	print('This Quiz will test how well you know Danish :P')
	print('\nThere are 8 questions as part of this Quiz ranging various themes so get your thinking caps ON')
	print('In the unlikely case that you have never heard of him, the quizmaster is generous enough to give you Clues!')
	print('However, dont get your hopes up too soon, in order to pass this quiz you need to get at least 6 questions right! ')
	

def player_name():
	# assign: name = player_name()

	name = ''

	while len(name) < 2:
		name = input('\nSo, to begin things off, What is your name? ')
		if len(name) < 2:
			print('\nSorry that name is too short, please try again')
	return name  


def familiarism(name):
	# assign a bool value: fam = familiarism(name)

	print('\nRighty then {}, to determine the road that lies ahead, Answer the Following ---> '.format(name))
	fam = input('\nDo you know Danish? ')

	if fam.lower()[0] == 'y':
		print('\nVery well, lets see how well you actually know him...')
		return True
	else:
		print('\nAlrighty then, it will help knowing that he is relatively BASIC.')
		return False


def initialisation():
	print('\nPlease wait while the Quiz initialises... ')
	time.sleep(3)


# Dictionary for the answers and clues to each quesiton - Format being; Q1:A1,C1
q_a_r_dict = {'Q1':['spring rolls','The East Asian version of a Samosa - Has the potential to roll, but not the potential to spring...'],
'Q2':['adidas','They sponsor Real Madrid, are in close competition with Nike, & always boasts too many stripes'],'Q3':['5','Picture the number of corners in a star & recall the number of members in One Direction'],
'Q4':['purple','A cats Favourite colour, is associated with royalty, & comes from the mucus of a snail'],
'Q5':['volleyball','What sport involves serving, but not by a waiter; and an ace but not a card'],'Q6':['breaking bad', 'The DEA, Cooking, & Chemistry'],
'Q7':['batman','The Riddler, The Detective, & The Dark'],'Q8':['rotterdam','Has the largest port in Europe, an observation tower called the Euromast, & is the home of Feyenoord']}


def questioning_non_familiar():
    
    # assign: correct_nf,incorrect_nf = questioning_non_familiar()
    incorrect_count = 0
    correct_count = 0
    count=0

    while count < 4:
        print("\nQuestion 1: What's his all-time favourite food?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q1'][0]:
            correct_count += 1
            print('\nWell done, thats correct!')
            print('\nLoading Question 2...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q1'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNope, try again')
            
        elif answer != q_a_r_dict['Q1'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nAlso wrong!')
            
        elif answer != q_a_r_dict['Q1'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nIncorrect! The following clues may help you: {q_a_r_dict['Q1'][1]}")

        elif answer != q_a_r_dict['Q1'][0]:
            incorrect_count += 1
            print('\nUnlucky!')
            print('\nLoading Question 2...')
            time.sleep(1.5)
            break

    count = 0     
        
    while count < 4:
        print("\nQuestion 2: What brand shoes is he always wearing?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q2'][0]:
            correct_count += 1
            print("\nThat's right :)")
            print('\nLoading Question 3...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q2'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nOops, try again')
            
        elif answer != q_a_r_dict['Q2'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nWrong again!')
            
        elif answer != q_a_r_dict['Q2'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nNopes! Can you guess it with these clues: {q_a_r_dict['Q2'][1]}")

        elif answer != q_a_r_dict['Q2'][0]:
            incorrect_count += 1
            print('\nUnfortunate!')
            print('\nLoading Question 3...')
            time.sleep(1.5)
            break
                
    count = 0     
        
    while count < 4:
        print("\nQuestion 3: How many siblings does he have?")
        answer = input('\nEnter your answer here: ')

        if answer == q_a_r_dict['Q3'][0]:
            correct_count += 1
            print('\nExcellent')
            print('\nLoading Question 4...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q3'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNooo')
            
        elif answer != q_a_r_dict['Q3'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nAttempt 2.0')
            
        elif answer != q_a_r_dict['Q3'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nLast Chance, with the following clues: {q_a_r_dict['Q3'][1]}")

        elif answer != q_a_r_dict['Q3'][0]:
            incorrect_count += 1
            print('\nNot quite right')
            print('\nLoading Question 4...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 4:
        print("\nQuestion 4: What's his favourite colour?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q4'][0]:
            correct_count += 1
            print('\nReal Madrid 2017 <3')
            print('\nLoading Question 5...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q4'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNah')
            
        elif answer != q_a_r_dict['Q4'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nMaybe in another life')
            
        elif answer != q_a_r_dict['Q4'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nCan you figure it out with these clues: {q_a_r_dict['Q4'][1]}")

        elif answer != q_a_r_dict['Q4'][0]:
            incorrect_count += 1
            print('\nSorry not sorry.')
            print('\nLoading Question 5...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 4:
        print("\nQuestion 5: What's his favourite sport?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q5'][0]:
            correct_count += 1
            print('\nDug, Set, & Spiked! Well Done')
            print('\nLoading Question 6...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q5'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNo')
            
        elif answer != q_a_r_dict['Q5'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nDo you wanna lose points?')
            
        elif answer != q_a_r_dict['Q5'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nYou should figure it out now: {q_a_r_dict['Q5'][1]}")

        elif answer != q_a_r_dict['Q5'][0]:
            incorrect_count += 1
            print("\nI'm disappointed")
            print('\nLoading Question 6...')
            time.sleep(1.5)
            break
        
    count = 0     
        
    while count < 4:
        print("\nQuestion 6: What's his favourite TV show?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q6'][0]:
            correct_count += 1
            print('\nHeisenberg Approves')
            print('\nLoading Question 7...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q6'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print("\nIt's better than that")
            
        elif answer != q_a_r_dict['Q6'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nEven better...')
            
        elif answer != q_a_r_dict['Q6'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nThis should make it obvious: {q_a_r_dict['Q6'][1]}")

        elif answer != q_a_r_dict['Q6'][0]:
            incorrect_count += 1
            print("\nDon't talk to me no mo.")
            print('\nLoading Question 7...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 4:
        print("\nQuestion 7: Who's his favourite superhero?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q7'][0]:
            correct_count += 1
            print(""" \n"It's not who I am underneath, but what I do that defines me" """)
            print('\nLoading Question 8...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q7'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print("\nYou got this")
            
        elif answer != q_a_r_dict['Q7'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nTry again')
            
        elif answer != q_a_r_dict['Q7'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nRead and think: {q_a_r_dict['Q7'][1]}")

        elif answer != q_a_r_dict['Q7'][0]:
            incorrect_count += 1
            print("\nTsk,Tsk,Tsk")
            print('\nLoading Question 8...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 4:
        print("\nQuestion 8: In what city was he born?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q8'][0]:
            correct_count += 1
            print("\nI can show you around :D")
            break
            
        elif answer != q_a_r_dict['Q8'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print("\nI don't blame you")
            
        elif answer != q_a_r_dict['Q8'][0] and count == 1:
            count += 1
            incorrect_count += 1
            print('\nClue incoming... if you get it wrong now')
            
        elif answer != q_a_r_dict['Q8'][0] and count == 2:
            count += 1
            incorrect_count += 1
            print(f"\nDoes this help: {q_a_r_dict['Q8'][1]}")

        elif answer != q_a_r_dict['Q8'][0]:
            incorrect_count += 1
            print("\nEat more cheese!")
            break
    
    return correct_count, incorrect_count


def questioning_familiar():
    # assign: correct_f,incorrect_f = questioning_familiar()
    incorrect_count = 0 
    correct_count = 0
    count=0

    while count < 2:
        print("\nQuestion 1: What's his all-time favourite food?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q1'][0]:
            correct_count += 1
            print('\nWell done, thats correct!')
            print('\nLoading Question 2...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q1'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNope, try again')
        elif answer != q_a_r_dict['Q1'][0]:
            incorrect_count += 1
            print('\nUnlucky!')
            print('\nLoading Question 2...')
            time.sleep(1.5)
            break

    count = 0     
        
    while count < 2:
        print("\nQuestion 2: What brand shoes is he always wearing?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q2'][0]:
            correct_count += 1
            print("\nThat's right :)")
            print('\nLoading Question 3...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q2'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nOops, try again')
        elif answer != q_a_r_dict['Q2'][0]:
            incorrect_count += 1
            print('\nUnfortunate!')
            print('\nLoading Question 3...')
            time.sleep(1.5)
            break
                
    count = 0     
        
    while count < 2:
        print("\nQuestion 3: How many siblings does he have?")
        answer = input('\nEnter your answer here: ')

        if answer == q_a_r_dict['Q3'][0]:
            correct_count += 1
            print('\nExcellent')
            print('\nLoading Question 4...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q3'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNooo')
        elif answer != q_a_r_dict['Q3'][0]:
            incorrect_count += 1
            print('\nNot quite right')
            print('\nLoading Question 4...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 2:
        print("\nQuestion 4: What's his favourite colour?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q4'][0]:
            correct_count += 1
            print('\nReal Madrid 2017 <3')
            print('\nLoading Question 5...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q4'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNah')
        elif answer != q_a_r_dict['Q4'][0]:
            incorrect_count += 1
            print('\nSorry not sorry.')
            print('\nLoading Question 5...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 2:
        print("\nQuestion 5: What's his favourite sport?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q5'][0]:
            correct_count += 1
            print('\nDug, Set, & Spiked! Well Done')
            print('\nLoading Question 6...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q5'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print('\nNo')
        elif answer != q_a_r_dict['Q5'][0]:
            incorrect_count += 1
            print("\nI'm disappointed")
            print('\nLoading Question 6...')
            time.sleep(1.5)
            break
        
    count = 0     
        
    while count < 2:
        print("\nQuestion 6: What's his favourite TV show?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q6'][0]:
            correct_count += 1
            print('\nHeisenberg Approves')
            print('\nLoading Question 7...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q6'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print("\nIt's better than that")
        elif answer != q_a_r_dict['Q6'][0]:
            incorrect_count += 1
            print("\nDon't talk to me no mo")
            print('\nLoading Question 7...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 2:
        print("\nQuestion 7: Who's his favourite superhero?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q7'][0]:
            correct_count += 1
            print(""" \n"It's not who I am underneath, but what I do that defines me" """)
            print('\nLoading Question 8...')
            time.sleep(1.5)
            break
            
        elif answer != q_a_r_dict['Q7'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print("\nC'mon, you got this")
        elif answer != q_a_r_dict['Q7'][0]:
            incorrect_count += 1
            print("\nTsk,Tsk,Tsk")
            print('\nLoading Question 8...')
            time.sleep(1.5)
            break
    
    count = 0     
        
    while count < 2:
        print("\nQuestion 8: In what city was he born?")
        answer = input('\nEnter your answer here: ').lower()

        if answer == q_a_r_dict['Q8'][0]:
            correct_count += 1
            print("\nI can show you around :D")
            break
            
        elif answer != q_a_r_dict['Q8'][0] and count == 0:
            count += 1
            incorrect_count += 1
            print("\nI don't blame you")
        elif answer != q_a_r_dict['Q8'][0]:
            incorrect_count += 1
            print("\nEat more cheese!")
            break
    
    return correct_count, incorrect_count


def answers_list():
    
    print('\n')
    print("\nAfter having completed this project, i realised that this is quite a sophisticated method of giving away information which may possibly answer secret questions haha.")
    print("\nThe following lists all the answer's incase you got them wrong and were curious: ")
    print("\nQ1: Spring Rolls")
    print("Q2: Adidas")
    print("Q3: 5")
    print("Q4: Purr-ple")
    print("Q5: Volleyball")
    print("Q6: Breaking Bad")
    print("Q7: Batman")
    print("Q8: Rotterdam")


# So to run the Quiz >>>>

import time

welcome_message() # Just explains what the quiz is about - lays out the structure

name = player_name() # Returns the players name - for ref later

fam = familiarism(name) # Returns a bool value - determines which set of questions will be asked

initialisation() # For pacing - slows down the game before the questions are presented

if fam == True:
    correct_f,incorrect_f = questioning_familiar()
else:
    correct_nf,incorrect_nf = questioning_non_familiar()

if fam == True and correct_f >= 6:
    print('\n')
    print("\nRight then {}, let's have a look at your performance!".format(name))
    print('You scored {}/8 on the Quiz, making {} errors, and have therefore passed!'.format(correct_f,incorrect_f))
    print('\nGreat work and thanks alot for playing <3')
elif fam == True and correct_f < 6:
    print('\n')
    print("\nRighttyy then {}, let's have a look at your performance!".format(name))
    print('You scored {}/8 on the Quiz, making {} mistakes, and have therefore failed :('.format(correct_f,incorrect_f))
    print(f"If only you had scored {6-correct_f} more points you would have passed :O")
    print('\nThanks for playing <3 and have a good day :)')
elif fam == False and correct_nf >= 6:
    print('\n')
    print("\nOkiee then {}, let's have a look at your score".format(name))
    print('You scored {}/8 in this Quiz, making {} mistakes, and have therefore succeeded!'.format(correct_nf,incorrect_nf))
    print('\nWell done, and thanks alot for playing <3')
elif fam == False and correct_nf < 6:
    print('\n')
    print("\nSo {}, let's have a look at your score!".format(name))
    print('You scored {}/8 in this Quiz with a whopping {} errors, and have therefore failed :('.format(correct_nf,incorrect_nf))
    print(f"If only you had scored {6-correct_nf} more points you would have passed :O")
    print('\nThanks for playing <3 and have a good day :)') 

time.sleep(3.5)
answers_list() 







