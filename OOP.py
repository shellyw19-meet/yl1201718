import turtle 

class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def Eat(self,food):
		print("Yummy! " + self.name + " is eating " + food)
	def Description(self):
		print(self.name + " is " +	str(self.age) + " years old and he likes the color " + self.favorite_color)
	def make_sound(self,x):
		print(self.name + " is doind " +self.sound*x)



dog = Animal("woof ","doggie",7,"Green")
dog.Eat("milk")
dog.Description()
dog.make_sound(4)


class Person(object):
	def __init__(self,name, age, city, gender, pet):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
		self.pet = pet
	def Breakfast(self, food):
		print("I am eating" + self.food +"! " + "I like it very much")

person = Person("Omer", 16, "Jerusalem", "male", "fish")
person.breakfast("Mekushkeshet")



		
