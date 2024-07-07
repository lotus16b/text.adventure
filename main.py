### Text Adventure 
print("You have been recruited by the Star League to defend the Frontier against Xur and the Ko-Dan Armada!")
print("Are you ready player one?")
print("If ready, take the blue pill. If you are not ready, take the red pill.")

### Prompt player for a choice
pillChoice = input("> ")

if(pillChoice == "blue pill"):
    print("You take the blue pill...you quickly become disoriented and as you stare blindly at the arcade cabinet...you blackout")
    print("...and awake...feeling as if you are in motion, no longer in the Starlite Starbrite trailer court. You find yourself in a car? Or at least it looks like a car.")
    print("except the scenery out the window is not California, it's a up close tour of the rings of Saturn.")
elif(pillChoice == "red pill"):
    print("You take the red pill and...feel no change...the arcade cabinet sits before you. You remain stuck in the Starlite Starbrite trailer court wishing you could do something with your life besides fixing Elvira's electric so she can watch her soaps.")
else:
    print("Invalid choice. Please enter blue pill or red pill...hint pick the blue pill.")
    