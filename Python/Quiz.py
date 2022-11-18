# Python Simple Quiz Start

score = 0 
percent = 0

# Question 1
answer1 = input("\n Who is your teacher? ")
if answer1.lower() == "mr. v" or answer1.lower() == "mr. veldkamp" or  answer1.lower() == "mr v":
  print("Correct")
  score = score + 1 
else:
  print("Incorrect")

# Question 2 
answer2 = input("\n what is the square root of 169? ")
if answer2 == "13" or answer2.lower() == "thirteen":
 print("Correct")
 score = score + 1 
else: 
 print("Incorrect")    

# Question 3 
answer3 = input("\n What does UNO mean in English ")
if answer3.lower() == "one" or answer3 == "1":
 print("Correct")
 score = score + 1 
else: 
 print("Incorrect")  

# Question 4
answer4 = input("\n Who Created UNO ")
if answer4.lower() == "merle robbins" or answer4.lower() == "merle" or answer4.lower() == "robbins":
 print("Correct")
 score = score + 1 
else: 
 print("Incorrect")  
  
 # Output Result 
percentage = (score / 4) * 100
print("\nYour score is " + str(score) + " / 4 " + "(" + str(percentage) + "%" + ") ")
  
if score == 4:
  print("Perfect as all things should be")
elif score == 3: 
  print("Almost Perfect")
elif score == 2:
  print("Good Try, Study more")
elif score == 1:
  print("There was an effort")
else: 
  print("Not even close")