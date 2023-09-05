#John Maloy
#9/5/2023
#Days remaining until 90 years old (lifetime)

ageInput = input("What is your current age?\n")#taking age input from user
print(f"You said your age is: {ageInput} years old")#checking that input is working thus far

newAgeInput = float(ageInput)
#ageInWeeks = newAgeInput * 52.143
#ageInMonths = newAgeInput / 30.4167
#ageinDays = newAgeInput / 7

#print(f"your age in weeks is", ageInWeeks)

remainingYears = 90 - newAgeInput
remainingMonths = remainingYears * 12
remainingWeeks = remainingMonths * 4
remainingDays = remainingWeeks * 7


print(f"you have {int(remainingMonths)} months remaining, {int(remainingWeeks)} weeks remaining, and {int(remainingDays)} days remaining until 90 years")
