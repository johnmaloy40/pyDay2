#John Maloy
#9/5/2023
#BMI calculation printed out in a whole number
#BMI = weight(kg) / height^2

heightInput = input("What is your height in m: \n")
weightInput = input("What is your weight in kg: \n")

print("you input", heightInput, "as your height, your weight was", weightInput)

newHeightInput = float(heightInput)#changed the original input to a float to take a more maleable input and then operate on it
newWeightInput = float(weightInput)#changed this to float as well for the operation

confirmInput = input("Was this correct? Type y or n\n")

bmiCalculation = newWeightInput/ (newHeightInput ** 2)
bmiCalculationOutput = int(bmiCalculation)

print("Your bmi is ", bmiCalculationOutput)