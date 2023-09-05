#John Maloy
#9/5/2023
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

getNumber = input("Enter a two digit number, please.\n")#changed getNumber from str to int
#repeatNumber = print("The number you typed was", getNumber) (just checkthing that the getNumber function works)

digit1 = int(getNumber[0]) #update the getNumber variable to the correct data type
digit2 = int(getNumber[1]) #update the getNumber variable to the correct data type

print("The two numbers added together are", digit1 + digit2) #performed the action on the two numbers