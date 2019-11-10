class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.post=[]
	def add_friend(self,email):
		self.email=email
		self.friends_list.append(email)
		print(self.name+" has added "+self.email+" as a friend")
	def remove_friend(self,email):
		self.email=email
		self.friends_list.remove(email)
		print(self.name+" has removed "+self.email+" as a friend")
	def post(self,text):
		self.text = text
		self.text.append(text)
		print(self.name+" has posted: "+self.text)
	def get_userInfo():
		print("___________")
		print("name: "+self.name)
		print("password: "+self.password)
		print("freinds: "+self.friends_list)
		print("post: "+self.gethu.compost)
		print("___________")
Jack=User("Jack", "jack.blah@email.com","Myhiddenpassword123")
Sam=User("Sam","sam.bbbbb@email.com","games")
Jack.add_friend("sam.bbbbb@email.com")
Sam.post()
