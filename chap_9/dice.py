from random import randint


class Die():

    def __init__(self):
        self.numSides = 6

    def roll_dice(self, *kwrds):
        if(len(kwrds)):
            self.numSides = kwrds[0]

        diceVal = randint(1, self.numSides)
        print("diceVal:", diceVal)
        print("numSides:", self.numSides)
        print()
        print()


def main():
    myDice = Die()
    n = int(input("Enter the number of times you want to roll the die:\n"))

    try:
        numSides = int(input("enter the number of sides:\n"))
    except:
        for i in range(0, n):
            myDice.roll_dice()
    else:
        for i in range(0, n):
            myDice.roll_dice(numSides)

if __name__ == '__main__':
    main()
