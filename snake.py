import random
n=0
while(n<=100):
	a=input("enter r to roll dice")
	if(a=='r'):
		r=random.randint(1,6)
		print('u got',r)
		n=n+r
		print('your score is',n)
		if(n==8):
			n=37
			print('you got ladder and now u r at',n)
		elif(n==11):
			n=2
			print('you were eaten by snake',n)
		elif(n==13):
			n=34
			print('you got ladder',n)
		elif(n==38):
			n=9
			print('snake bite',n)
		elif(n==40):
			n=68
			print('ladder',n)
		elif(n==52):
			n=81
			print('ladder',n)
		elif(n==65):
			n=46
			print('snake bite',n)
		elif(n==76):
			n=97
			print('ladder you pretty much will win now',n)
		elif(n==99):
			n=70
			print('snake aww so close',n)
		elif(n==93):
			n=64
			print('snake bite. so close',n)
		elif(n==100):
			print("winner winner chicken dinner you won")
		elif(n>100):
			n=n-r
			print('you went after 100 retry again')	
	else:
		break
