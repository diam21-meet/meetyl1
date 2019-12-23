list1=[1, 2, 3, 4, 5, 6, 7,8 ,9]
list2=[2, 3, 5, 6, 7, 8, 9, 10]
def common_numbers(list1, list2):
	list3=[]
	for num in list1:
		if num in list2:
			list3.append(num)
	return (list3)
list4 = common_numbers(list1,list2)
print(list4)

encoder_caesar={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}
def bhj(stringin):
	stringin=input("Can you type anything?")
	print(encoder_caesar[stringin])