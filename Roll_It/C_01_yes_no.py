
while True:

    want_instructions = input("do you want to see the instruction?").lower()

    # check the user says yes / no/ /y / no
    if want_instructions == "yes" or want_instructions == "y":
        print("you said yes")
        break
    elif want_instructions == "no" or want_instructions == "n":
        print("you said no")
        break
    else:
        print("please enter yes / no")
        continue

print("we are done")
