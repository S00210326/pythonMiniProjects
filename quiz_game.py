print("Welcome to my computer quiz")

score = 0
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :) ")

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    score += 1
    print("Correct Answer")

else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    score += 1
    print("Correct Answer")
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    score += 1
    print("Correct Answer")
else:
     print("Incorrect")

print("score == " + str(score) + " of 3")