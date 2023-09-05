#John Maloy
#9/5/2023
#Tip calculator


billTotal = input("Welcome to the tip calculator\nEnter the total amount of your bill\n")
billTotalConfirmation = print(f"you typed {billTotal}")

billTotalFloat = float(billTotal)

tipPercent = input("What percent would you like to tip? enter below\n")
tipPercentFloat = float(tipPercent)

tipTotal = billTotalFloat * (tipPercentFloat / 100)
billAndTip = billTotalFloat + tipTotal
whatToTip = print(f"Your tip amount for a ${billTotalFloat} purchase would be ${tipTotal} and your total bill would come out to ${billAndTip}")




