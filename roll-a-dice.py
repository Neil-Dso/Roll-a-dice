import random
from playsound import playsound 

response = input('Do you want to roll the dice?(Enter "y" for yes and "n" for no):')

while response == 'y':
    no = random.randint(1, 6)
    if no == 1:
        print('[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]')
        print("Aww.. Let's try again!")
        response = input('To roll the dice enter "y" or "n" to exit):')
    elif no == 2:
        print('[-----]\n[ 0   ]\n[     ]\n[   0 ]\n[-----]')
        response = input('To roll the dice enter "y" or "n" to exit):')
    elif no == 3:
        print('[-----]\n[ 0   ]\n[  0  ]\n[   0 ]\n[-----]')
        response = input('To roll the dice enter "y" or "n" to exit):')
    elif no == 4:
        print('[-----]\n[ 0 0 ]\n[     ]\n[ 0 0 ]\n[-----]')
        response = input('To roll the dice enter "y" or "n" to exit):')
    elif no == 5:
        print('[-----]\n[ 0 0 ]\n[  0  ]\n[ 0 0 ]\n[-----]')
        print('Nice!')
        response = input('To roll the dice enter "y" or "n" to exit):')
    elif no == 6:
        print('[-----]\n[ 0 0 ]\n[ 0 0 ]\n[ 0 0 ]\n[-----]')
        print('Amazing!')
        playsound('party.mp3')
        response = input('To roll the dice enter "y" or "n" to exit):')

if response == 'n':
    print('Thank you!')