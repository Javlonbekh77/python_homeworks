from random import randint
def GameofGuessNumber():
	guess_number = randint(1,101)
	attemps =0
	print("I guessed one number and try to find it !?")
	h= ['Y', 'YES', 'y', 'yes', 'ok']
	while True:
		answer = int(input("Input your guess... "))
		attemps+=1
		if answer == guess_number:
			print(f"You guessed it right! You have found it in {attemps} attempts")
			ok = input("Want to play again? ('Y', 'YES', 'y', 'yes', 'ok')  ")
			if ok in h:GameofGuessNumber()
			else:
				print("Thanks for attending our Game!!!")
				break
		elif answer>guess_number:
			print("Too high!")
		else :print("Too low!")
		if attemps>10:
			print(f"You guessed it right! You have found it in {attemps} attempts")
			ok = input("You lost, Want to play again? ('Y', 'YES', 'y', 'yes', 'ok')  ")
			if ok in h:GameofGuessNumber()
			else:
				print("Thanks for attending our Game!!!")
				break
GameofGuessNumber()