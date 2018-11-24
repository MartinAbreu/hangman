import random
def eight_ball():
    ball_shake=input('Do you want to shake the magic ball? y/n ')
    fortune=['You will be wealthy!', 'You will die a slow agonizing death',
             ' I see good health in your life', 'It\'s very hazy, try again',
             ' A stranger will appear...', 'Shake harder, ']
    if ball_shake == 'y':
        print(random.choice(fortune))
        try_again=input('Try again? y/n ')
        if try_again == 'y':
            eight_ball()
        elif try_again == 'n':
            exit()
        else:
            input('Thats not an option')
            eight_ball()
    elif ball_shake == 'n':
        exit()
    else:
            input('Thats not an option')
            eight_ball()    

eight_ball()        
