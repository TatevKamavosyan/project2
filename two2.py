import random

win_num=[7,11]
lose_num=[2,3,11]
goal_num=[4,5,6,8,9,10]
goal_number=0
game_play=True
game_play=False

value1=random.randint(1,6)
value2=random.randint(1,6)
dice_sum=value1+value2
print(f'The sum of dice is {value1}+{value2}={dice_sum}')
if dice_sum in win_num:
  print('You win!')
elif dice_sum in lose_num:
  print('You lose!')
else:
  goal_number=dice_sum
  print(f'Your goal number is {goal_number}')
  
  game_play=True
  while game_play:
    value1=random.randint(1,6)
    value2=random.randint(1,6)
    dice_sum=value1+value2
    print(f'The sum of dice is {value1}+{value2}={dice_sum}')
    if dice_sum==goal_number:
      print('You win!')
      game_play=False
    elif dice_sum==7:
      print("You lose!")
      game_play=False
    