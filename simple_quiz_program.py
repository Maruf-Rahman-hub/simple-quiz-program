stranger = input("What is your name? \n")
def ans_cheacker_a(ans):
    if ans == "a" or ans == "A" :    
        print(f"you are correct  {stranger}\n ")
    else:
        print(f"you are wrong  {stranger}")
def ans_cheacker_b(ans):
    if ans == "b" or ans == "B" :    
        print(f"you are correct  {stranger}\n ")
    else:
        print(f"you are wrong  {stranger}")
    
#welcome to quiz       
print(f"Welcome to the simple quiz {stranger} \n "  )
#q1
print("What is the capital of Chile? Santiago(a) , Mario(b)\n")
ans1 = input("Enter the answer \n") 
ans_cheacker_a(ans1)
#q2
print("What is the highest mountain in Britain? Everest(a) , Ben Nevis(b)\n")
ans2 = input("Enter the answer \n")
ans_cheacker_b(ans2)
#q3
print("What is the smallest country in the world? \n Vatican City(a) , Canada(b)\n")
ans3 = input("Enter the answer \n") 
ans_cheacker_a(ans3)
#q4
print(" What did the Romans call Scotland? Caledonia(a) , Norwegian(b) \n")
ans4 = input("Enter the answer \n") 
ans_cheacker_a(ans4)
#q5
print("Who was Henry VIIIs last wife? William Pitt(a) , Catherine Parr(b) \n")
ans5 = input("Enter the answer \n") 
ans_cheacker_b(ans5)
#q6
print("Who was the first female Prime Minister of Australia? Julia Gillard(a) , Sir Walter Raleigh(b) \n")
ans6 = input("Enter the answer \n") 
ans_cheacker_a(ans6)
#q7
print("What is the most famous Mexican beer Anchovy(a) , Corona(b) \n")
ans7 = input("Enter the answer \n") 
ans_cheacker_b(ans7)

