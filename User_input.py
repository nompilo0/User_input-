name = input("Enter your name: ")
age = int(input("Enter your age"))
location = input("Enter your location: ")

# first approach
print(" Hello ", name , "you are " , age, "years old and you live in " , location)

#second approach %
print ("second approach")
print("Hello %s you are %d years old and you live in %s"% name , age , location )

#third approach format
print("third approach")
print("Hello {} you are {}years old and you live in {}".format(name ,age , location ))