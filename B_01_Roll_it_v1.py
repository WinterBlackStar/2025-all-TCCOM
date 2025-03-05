# functions go here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        # check the user says yes / no/ /y / n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Roll the dice and try to win!
    """)


def int_checker():
    """Check user enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13."

    while True:
        try:
            response = int(input("What is the game goal?"))

            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine

# ask the user if they want to see instructions (check is they say yes / no)
want_instructions = yes_no("Do you want to see the instructions?")

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_checker()
print(game_goal)
