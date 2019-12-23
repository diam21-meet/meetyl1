import math
x=input ("Can you type a number?")
y=input("Can you type another number?")
if x>10 or x<1:
	x=input("Your number was too big or too small, can you retype a number that is smaller than 11 and bigger than 0?")
elif y>10 or y<1:	
	y=input(" You typed a number that is bigger than 0 or smaller than 11, can you give another input?")
z=math.pow(x,y)	
print(z)
t=math.sqrt(z)
print(t)
q=math.pow(t,2)
print(q)
while q<100000:
	q = q + 1
print(q)