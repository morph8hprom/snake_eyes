"""

Dice rolling utility that allows the user to input number of dice as well as
sides of dice.  Also saves a log of previous dice rolls in text file dice_log

"""
import random


def roll_em():

    #Gets a number of dice and makes sure that it is a number
    while True:
        try:
            die = int(raw_input('Number of dice\n'))
            break
        except (TypeError, ValueError):
            print 'Please enter a number'
    #Gets a number of sides and makes sure that it is a number
    while True:
        try:
            sides = int(raw_input('Number of sides\n'))
            break
        except (TypeError, ValueError):
            print 'Please enter a number'


    #Generates the dice roll into a list of integers
    roll = [random.randint(1, int(sides)) for _ in xrange(int(die))]
    dice_log(die, sides, roll)
    return roll


#Create/open a log file to save dice rolls

def dice_log(die, sides, roll):
    f = open("dice_log.txt","a")
    f.write('\n{}d{}\n'.format(die, sides))
    f.write('-'* 4)
    f.write('\n{}'.format(str(roll)))
    f.write('\nTotal:')
    f.write('\n{}'.format(sum(roll)))
    f.close



#Banner that will be displayed at the start of the program
def banner(name, char):
    frame_line = char * (len(name) + 2)
    print frame_line
    print char + name + char
    print frame_line



def main():
    banner('Rollin Bones', '-')
    raw_input('\nPress enter to begin\n')
    while True:

        #Generates integer list and stores it in variable roll
        roll = roll_em()
        #Converts list into string
        rollstr = ','.join(map(str, roll))
        #Stores sum of roll in variable total
        total = sum(roll)
        #Prints list of individual dice as well as total
        print 'You rolled: {}\nTotal: {}'.format(rollstr, total)
        #Prompts the user to roll again
        roll_again = raw_input('Press enter to roll again or type quit\n')
        #Provides the user with an option to exit
        if roll_again.lower() == 'quit':
            break


if __name__ == "__main__":
    main()
