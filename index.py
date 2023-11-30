class Balloon:
    def __init__(self, defence_item, colour):
        # Private attributes
        self.health = 100  # Health of the balloon
        self.__colour = colour  # Colour of the balloon
        self.__defence_item = defence_item  # Item the balloon uses to defend itself

        # Constructor initializes attributes with given parameters

    def GetDefenceItem(self):
        return self.__defence_item

    def ChangeHealth(self, change):
        self.health += change

    def CheckHealth(self):
        return self.health <= 0

def Defend(balloon_obj):
    opponent_strength = int(input("Enter the strength of the opponent: "))

    # Using the ChangeHealth method to subtract opponent's strength from the balloon's health
    balloon_obj.ChangeHealth(-opponent_strength)

    # Output the defence item of the balloon
    print(f"The defence item of the balloon is: {balloon_obj.GetDefenceItem()}")

    # Check the health of the balloon and output appropriate message
    if balloon_obj.CheckHealth():
        print("The balloon has no health remaining.")
    else:
        print("The balloon has health remaining.")

    return balloon_obj

def main():
    # Create a Balloon object
    my_balloon = Balloon("Shield", "Red")

    # Hardcoded opponent strength for testing purposes (50 as per input)
    opponent_strength = 50

    # Set the opponent strength directly without input
    my_balloon.ChangeHealth(-opponent_strength)

    # Output the defence item of the balloon
    print(f"The defence item of the balloon is: {my_balloon.GetDefenceItem()}")

    # Check the health of the balloon and output appropriate message
    if my_balloon.CheckHealth():
        print("The balloon has no health remaining.")
    else:
        print("The balloon has health remaining.")

if __name__ == "__main__":
    main()
