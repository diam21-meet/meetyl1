class User():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self,email):
		self.email=email
		self.friends_list.append(email)
		print(self.name + " has added " + self.email + " as a friend")
	def remove_friend(self,email):
		self.email=email
		self.friends_list.remove(email)
		print(self.name + " has removed " + self.email + " as a friend")
	def post(self,text):
		self.posts.append(text)
		print(self.name + "has posted " + text)
	def getuser_info(self):
		print("---------")
		print(self.name)
		print(self.email)
		print(self.password)
		print(self.friends_list)
		print(self.posts)
Jack=User("Jack", "jack.blah@email.com","Myhiddenpassword123")
Sam=User("Sam","sam.bbbbb@email.com","games")
Jack.add_friend("sam.bbbbb@email.com")
Sam.post('hello')
Jack.getuser_info()
Sam.getuser_info()
class Post():
	def __init__(self,name,email,text):
		self.name=name
		self.email=email
		self.text=text
		self.post_list=[]
	def post(self):
		self.posts_list.append(text)
		print(self.name + " has posted " + text)
