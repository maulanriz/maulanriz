import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_pic = [rock, paper, scissors]
you = int(input("Choose 0 for rock, 1 for paper, 2 for scissors\n"))
if you >= 3:
    print("You pick wrong number, You Lose!")
else:
    print(game_pic[you])
    bot = random.randint(0, 2)
    print("Bot choice:", game_pic[bot])
    if you == bot:
        print("draw")
    elif you == 0 and bot == 1:
        print("bot win")
    elif you == 0 and bot == 2:
        print("you win")
    elif you == 1 and bot == 0:
        print("you win")
    elif you == 1 and bot == 2:
        print("bot win")
    elif you == 2 and bot == 0:
        print("bot win")
    elif you == 2 and bot == 1:
        print("you win")
