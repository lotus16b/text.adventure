# variables
first_name = "alex"
last_name = "rogan"
full_name = f"{first_name} {last_name}"
famous_person = "Centauri"
centauri_message = "Always trust Centauri, my boy."
x, y, z = 32, 47, 171
# create a list of equipment Alex needs
equipment = ['starfighter uniform', 'helmet', 'gunstar', 'positive attitude']
# create a list of high scores
high_scores = [value**3 for value in range(99, 104)]
# start the interaction with a question
message = f"Hello, {full_name.title()}, how are you today?"
print(message)
# create an input to respond to the question
response = input(">")
# if elif else statement
if(response == "good"):
    print("Great!")
    print("We need to get to the frontier")
    print(f"Grab your {equipment[0]} and {equipment[1]} and get in the {equipment[-2].title()}")
    print("Program your nav system with the coordinates:")
    print(x, y, z)
elif(response == "not good"):
    print("What?! Don't you want to be a Starfighter?")
    print(f"What you need is a {equipment[-1]}")
    print("Alright, take this communicator if you change your mind")
    equipment.append('communicator')
    print(f"Just tap the crystals on the {equipment[-1]} and I'll be back.")
else:
    print(f"hmmm....nevermind that...{centauri_message}")
    print("You're the best I've ever seen, here are your high scores:")
    print(high_scores)
    print(f"That {max(high_scores)} set a record across the Star League!")
    print("It is time to get going...") 
    print(f"You have {len(equipment)} items in your equipment list.")
    print("Here is a list of your equipment for fighting Xur:")
    print(', '.join(sorted(equipment)))
    print("The most important item on your list is:")
    print(equipment[3:])