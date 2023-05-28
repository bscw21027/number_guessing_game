import random

print ( "\n Welcome to the Number Guessing game.")

def guess(n):
 com_choice = random.randint(1, 100)  
 print(com_choice) 
 for i in range(10):     
     gues = int (input( " Guess a number : "))
     a = com_choice + 10
     b = com_choice - 10
     c = com_choice + 5
     d = com_choice - 5
     e = com_choice + 2
     f = com_choice - 2
     if gues>=a or gues<=b:
         print(" High.", end = "")
         if gues>=c or gues<=d:
             print(" Close.", end = "")
             if gues>=e or gues<=f:
                 print(" Very Close.", end = "")
     else:
         print ( " Very Very High. ", end = "")
     if gues == com_choice:
         print( " Congratz! You Won.")
         break
     else:
         print( " Guess Again.")
 if gues != com_choice:    
   print( " Sorry! You ran out of lives. ")
     
choice = input (" Choose a difficulty level : ")


if choice == "easy":
   guess(10)
else:
   guess(5)





















