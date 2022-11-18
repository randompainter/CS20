# Python Coin Flip

import random

# Total
num_heads = 0
num_tails = 0

n = 0
while n <= 10:
  #Flip coin
 randNum = random.randrange(1, 3) # 1 and 2 
 if randNum == 1:
   num_heads += 1
   print("Heads (Head: " + str(num_heads) + " Tail: " + str(num_tails) + ")")
 else:
   num_tails += 1
   print("Tails (Tails: " + str(num_tails) + " Tail: " + str(num_tails) + ")")
   
  # Increment n
 n += 1



# Use a for loop to run a set # of times
#for n in range (8):
# print("Joe")