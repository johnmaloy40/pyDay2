#functions not working with the data type requested will leave you with an error

lettersCount = len(input("What is your name?\n"))
newLettersCount = str(lettersCount)#store the lettersCount as a str instead of an int so you can add the parts together in the print statement


print("your name has " + newLettersCount + "letters")

#a = float("123") #check the data type of a, it will show as float

#print(str(70) + str(100)) #we can change data types to work with them more easily.