a=[1,2,3,4,5,6,7,8,9,]


def printboard():
	print(a[0],'|',a[1],'|',a[2])
	print("............")
	print(a[3],'|',a[4],'|',a[5])
	print("............")
	print(a[6],'|',a[7],'|',a[8])



playeroneturn= True

while True:
	printboard()
	p=int(input("choose ur place,player 1 >>"))
	if(p in a):
		if playeroneturn:
			print("player 1 choose:",p)
			a[p-1] ='X'
			playeroneturn=not playeroneturn
		else:
		#p= input ("choose your place,player 2 >>")
			a[p-1]='0'
			playeroneturn=not playeroneturn
		#check for winning condition:
		for i in (0,3,6):
			if(a[i]==a[i+1]and a[i]==a[i+2]):
				if a[i]=='x':
					print("player 1 wins !!!")
					exit()
				else:
					print("player 2 wins !!!")
					exit()
		for i in range(3):
			if(a[i]==a[i+3]and a[i]==a[i+6]):
				if a[i]=='x':
					print("player 1 wins !!!")
					exit()
				else:
					print("player 2 wins !!!")
					exit()

			
		if(a[i]==a[i+4]and a[i]==a[i+8]):
			if a[i]=='x':
				print("player 1 wins !!!")
				exit()
			else:
				print("player 2 wins !!!")
				exit()

		if(a[i]==a[i+4]and a[i]==a[i+6]):
			if a[i]=='x':
				print("player 1 wins !!!")
				exit()
			else:
				print("player 2 wins !!!")
				exit()
		#for i in range(1,10):
			#if()						

	else:
		continue	
