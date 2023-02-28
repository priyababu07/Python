"""
# AUTHOR: Priya Babu

# DATE: 28/02/2023

# PROGRAM:Guessing game
"""
import random
print("Let play the guessing game")
print("ARE U READY FOR THE FUN CHALLENGE \n If yes Press S \n Not ready to Accept the challenge then N ")
S = input()
if S=="S":
    print("Enter your value between 0 to 1000 lets check")
    num1 = int(input())
    ran = random.randint(0,1000)
    if ran==num1:
        print("You won the challenge")
    else:
        print("The number was",ran)
        print("May be next time")
        
else:
    print("May be you are not ready hope next time")

