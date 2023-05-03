name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end, you can go left or right, which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river you can swim across "
                   "it or walk around it. Type walk or swim :")
    if answer == "swim":
        print("You swam accross and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game")
    else:
        print('Not a valid option, You lose')

elif answer == "right":
    answer = input("You come to a bridge,"
                   " do you want to cross it or head back?( back\cross):")

    if answer == "back":
        print("You go back and lose. ")
    elif answer == "cross":
      answer = input("You cross the bridge and meet a changer, do you talk? (yes/no)")

      if answer == "yes":
          print("they give you gold and you WINNNNNNNNN")
      elif answer == "no":
          print('Not a valid option, You lose')

