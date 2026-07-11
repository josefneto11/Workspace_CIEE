


#check python version 
#python --version
# if not installed (https://www.python.org/)


#check python editor version 
import sys
print(sys.version)
print(sys.version_info)
print("Trial version: ", sys.version_info.major, sys.version_info.minor, sys.version_info.micro)


# Hello world
print("Hello, World!")
print("I love Tokyo")
print("I Love America")


# new line and space
#print("Python is fun!") print("Really!") 
print("Hello \n World")
print("Python\tProgramming")

# print a number 
print(0.07)
print(123)
print(5000)

#doing maths inside print
print(3+4)
print(3*4)
print(3/4)
print(10 + 5)
print(8 * 7)
print((5 + 3) * 2)
print(2 ** 5)      # Power
print(17 % 5)      # Remainder
print(17 // 5)     # Integer division

print(format(3.14159265, ".2f"))
print(format(1234567, ","))

#Mix text and numbers 
print ("Hello my name is google and I am", 27)
print ("Hello my name is google and I am", 27, "and I was born in California")

#using some pythin parameters
print("Apple", "Banana", "Orange")
print("Apple", "Banana", "Orange",sep=",")
print("Apple", "Banana", "Orange",sep="|")
print("Apple", "Banana", "Orange",sep="-")

# using end 
print("Loading", end="....")
print("done!")

# position 
print("Python".center(20))
print("Python".ljust(20))
print("Python".rjust(20))

# python unicode
print("😀")
print("🤖 Robotics")
print("日本")
print("Olá")

#printing repeated text
print("Hello " * 5)
print("*" * 30)
print("=" *30)

#printing true or false
print(True)
print(False)