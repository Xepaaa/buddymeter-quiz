# buddymeter-quiz
.

wrt. notes taken prior to starting this project >>>

# So we want to create a Quiz :)

'''A Quiz which questions the user about me

	1. Asks how well they know Danish
	2. Series of questions surrounding his personality
	3. Around 8 questions?
	4. Add feature to ask for name
	5. Add feature to ask if they know him
		○ If they do, do not continue with clues but instead questions only
		○ If they don't, continue in clue format alongside questions
			§ See if possible to give hint after three of wrong guesses
				□ Keep engagement by constant text
	6. Questions relating to fav TV show, sport, what phone he has, music taste etc.
	7. Reveal the Score in the end
	8. Need to reveal answers as you play due to difficulty continuing?
	9. Or just show the list of answers in the end
	10. include rationale in final upload
	11. Add a result loader?
'''

wrt. thoughts and notes after the project had been completed >>>

'''
So in summary, this quiz can two pathways, one, for the player to answer questions without clues and another with.
I think i achieved what i had envisioned in this project which was to create a quiz where i could implement attempts
before the player would move onto the next question, losing their chance to earn points.

However, this pathway format was initially an idea to create a quiz (or Quiddle) in which one pathway was to answer for riddles and one for questions
respectively, however i was finding it difficult to come up with riddles for the answers to the questions i proposed, and the "riddles" i had come up 
with were more akin to clues and hence i went with the following format. It would have been nice to use riddles as i couldve used the name i came up 
with for the initial idea which was "Quiddle".

Regarding the code:

    I had only one issue in my final run which was that i kept getting an error if the wrong answer was given for Q3,
    now to go into details, the answer in the dict was initially 5 as an int, to accomodate this i enclosed the input request for Q3 with an "int".
    An error however appeared when a wrong number was put in and the only way i could think of fixing it was to change the 5 in the dict to a str
    and remove the int(input) method.

    Additionally, i only used the name of the player in the final assesment of their score at the end of quiz, but just added those into the familiarism() function
    to make the introduction more personal.

    Furthermore, for players that were unsuccefull in their attempt to pass, i included how many points they would have required in order to pass. Initially tried
    to achieve this using this .format() method but quickly realised the f string literal method is the best.

    Lastly, i incorporated plenty of the time.sleep() method to just slow the game down between questions and not make it feel rushed.

Overall, as my second project i am pretty darn satified with :)
'''
