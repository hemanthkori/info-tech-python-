import random
#assing stating value 0 for both players
player=0
computer=0
dic={1:'r',2:'p',3:'s'}
while True:
	p=input("press r for rock, p for paper ,s for scissor")
	c=dic[random.randint(1,3)]
	print('you choose',p,'comp choose:',c)
	if p==c:
		print("tie")
	elif p=='r':
		if c=='p':
			print("computer wins")
			computer=computer+1
		else:
			print("Player wins")
			player=player+1	
	elif p=='p':
		if c=='s':
			print("computer wins")
			computer=computer+1
		else:
			print("player wins")
			player=player+1	

	elif p=='s':
		if c=='r':
			print("computer wins")
			computer=computer+1
		else:
	 		print("you win")
	 		player=player+1
	if(player==3):
		print("you win")
		break
	elif(computer==3):
		print("computer wins")
		break	 	
	 
