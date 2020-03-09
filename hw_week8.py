import random

def hw_week8():
  print('ROCK, PAPER, SCISSORS')
  win = 0
  losses = 0
  ties = 0

  while True:
    print(
     str(win) + ' Wins, '+ str(losses) +' Losses, ' +str(ties)+' Ties'
    )

    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

    user_input = input()
    if user_input =='r':
      print ('ROCK versus...')
    elif user_input =='p':
     print ('PAPER versus...')
    elif user_input =='s':
     print ('SCISSORS versus...')
    elif user_input =='q':
     break
    else:
     pass

    computer_chose = random.choice('rps')
    if computer_chose == 'r':
      print ('ROCK')
    elif computer_chose == 'p':
      print ('PAPER')
    elif computer_chose == 's':
      print ('SCISSORS')

    if computer_chose == user_input:
      print ('It is a tie!')
      ties=ties+1
    elif user_input == 'r' and computer_chose =='p':
      print ('You lose!')
      losses=losses+1
    elif user_input == 'r' and computer_chose =='s':
      print ('You win!')
      win=win+1
    elif user_input == 'p' and computer_chose =='s':
      print ('You lose!')
      losses=losses+1
    elif user_input == 'p' and computer_chose =='r':
      print ('You win!')
      win=win+1
    elif user_input == 's' and computer_chose =='r':
      print ('You lose!')
      losses=losses+1
    elif user_input == 's' and computer_chose =='p':
      print ('You win!')
      win=win+1

if __name__ == '__main__':
    hw_week8()
