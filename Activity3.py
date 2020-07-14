username1=input("What is the player 1's name: ")
username2=input("What is the player 2's name: ")

user1_ans=input(" 1's user pick the options from rock, scissors and paper?: ")
user2_ans=input(" 2's user pick the options from rock,paper and scissors?: ")

#alogorithms
if user1_ans==user2_ans:
    print("Its a tie")
if user1_ans=="rock":
    if user2_ans=="scissors":
        print("Rock wins!")
    else:
        print("Paper wins!")
elif user1_ans=="scissors":
    if user2_ans=="paper":
        print("Scissor win!")
    else:
        print("rock wins!")
else:
    if user2_ans=="rock":
        print("paper wins!")
    else:
        print("Scissors wins!")



