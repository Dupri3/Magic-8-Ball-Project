import sys
import random

ans = True

while ans:
    question = input('ask magic 8 ball anything ! ')

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print( 'it is certain ')

    elif answers == 2:
        print('out-look is amazing')

    elif answers == 3:
        print('you should be alright .. for now')

    elif answers == 4:
        print('ask again later')

    elif answers == 5:
        print('concentrate on something else for now')

    elif answers == 6:
        print('nothing is coming to me at the moment try again later')

    elif answers == 7:
        print('i\'m sorry but no..')

    elif answers == 8:
        print('my sources say no')
