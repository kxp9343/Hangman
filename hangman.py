import randmon 
possible = ["CUCUMBER", "JICANA", "SPIDERMAN", "BANANA", "CATAPULT"]
random.shuffle(possible)
answer = list(possible[1])

display = []
display.extend(answer)
for i in range(len(display)):
		display[i] = "_"

#lets start the game!
print("Welcome to hangman!")
print("Hang out with us!")
print(''.join(display))
print("\n\n\n\n")
count = 0
while count < len(answer):
	guess = input("Guess a letter: ")
	guess = gues.upper()
	for i in range(len(answer)):
		if answer[i]== guess:
			dislplay[i]== guess
			count+=1
	print(''.join(display))
	print("You guessed the word!")
	print(''.join(display))
	