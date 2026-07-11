
# Text Type:	str
# Numeric Types:	int, float, complex
# Boolean Type:	bool
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


""" Text Type """

# string 
teacher_name = "David"


""" Numeric Types"""

#integer 
step =5

#float 
distance =  10.5 #cm

#complex 
relative_target_vector = 2j

""" Boolean"""
trigger =  False
check =  True

""" Sequence Types """
car = ["Nissan", "Suzuki", "Mazda", "Nissan"]
print(f"car 1: {car[0]}", f"car 2: {car[1]} ",f"car 3:{car[2]} ", sep = "|")

car[1] = "Toyota"  # Changing "Suzuki" to "Toyota"
car.append("Honda")  # Adding a new car to the end
print(f"car 1: {car[0]}", f"car 2: {car[1]}", f"car 3: {car[2]}", f"car 4: {car[3]}", f"car 5: {car[4]}", sep=" | ")

fruits = ("apple", "banana", "Melon")  #tuple
person = {"name" : "John", "age" : 36}  #dictionary
t_shirt = {"white", "green", "yellow"}   #set



""" range"""
length =  range(0,10)
print(type(length))

