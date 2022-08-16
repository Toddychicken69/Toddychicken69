#Introductory Question
print("Welcome to the General quiz")
answer = str(input('Are you ready to play the Quiz ? (yes/no):'))
Score = 0
Total = 5

#Questions
if answer.lower()=="yes":
    answer = input("Question 1: What does the Japanese word Sayonara mean?:")
    if answer.lower()=="goodbye":
        print("Correct!")
        Score += 1
    else:
        print("Wrong!")

    answer = input("Question 2: How many grapes are needed to make one bottle of wine?:")
    if answer.lower()=="700":
        print("Correct!")
        Score += 1
    else:
        print("Wrong!")

    answer = input("Question 3: Which school did Harry Potter attend?:")
    if answer.lower()=="hogwarts":
        print("Correct!")
        Score += 1
    else:
        print("Wrong!")

    answer = input("Question 4: What is 77+33?:")
    if answer.lower()=="110":
        print("Correct!")
        Score += 1
    else:
        print("Wrong!")

    answer = input("Question 5: In humans, fertilization normally occurs in?:")
    if answer.lower()=="fallopian tube":
        print("Correct!")
        Score += 1
    else:
        print("Wrong!")

#Ending
mark = (Score/Total)*100
print('Marks obtained:',mark)

if mark > 50:
    print("You Passed!")
else:
    print("You Failed!")

answer = str(input("Was this game rigged? (yes/no):"))

if answer.lower()=="yes":
    print("Thanks for the feedback")
else: 
    print("Thanks")