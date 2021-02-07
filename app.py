name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!")
print("Wow, you are " + age + " years old!")
print("I have never met a " + name + " that is " + age + " years old")
print("Today we will be taking a math quiz")
print("Question 1, What is 10+10")
input("Enter your answer: ")
problem_one = "20"
print("The correct answer is " + problem_one + " Did you get it correct?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("That is great!")
    print("You are at a 100 percent")
elif answer == "no":
    print("That is horrible, you need to do better you are at a 0 percent")
print("Question 2, What is 2 to the 4th power")
input("Enter your answer: ")
problem_two = "16"
print("The correct answer is " + problem_two + " Did you get it correct?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("That is great!")
elif answer == "no":
    print("That is horrible, you need to do better")
print("Question 3, What is 4*5")
input("Enter your answer: ")
print("The correct answer is " + problem_one + " Did you get it correct?")
answer = input("Enter yes or no: ")
if answer == "yes":
    print("That is great!")
elif answer == "no":
    print("That is horrible, you need to do better")
print("This is the end of the quiz. What was your score?")
print("please choose one of the following, 1/3, 2/3, 3/3")
answer_two = input("Enter 1/3 or 2/3 or 3/3: ")
if answer_two == "3/3" or "2/3":
    print("Great job, you recieved above a 50 percent")
elif answer_two == "1/3":
    print("You failed, try again next time!")
print("The End!")
