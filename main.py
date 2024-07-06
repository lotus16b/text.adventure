### Text Adventure 
print("You have been recruited by the Star League to defend the Frontier against Xur and th Ko-Dan Armada!")
print("Are you ready player one?")
print("If ready, take the blue pill. If you are not ready, take the red pill.")

### Prompt player for a choice
pillChoice = input("> ")

if(pillChoice == "blue pill"):
    print("You take the blue pill...you quickly become disoriented and as you stare blindly at the arcade cabinet...you blackout")
    print("...and awake...feeling as if you are in motion, no longer in the Starlight Starbright trailer park")
elif(pillChoice == "red pill"):
    print("You take the red pill and...feel no change...the arcade cabinet sits before you. You remain stuck in the Starlight Starbrite trailer park wishing you could do something with your life besides fixing TV receptions.")
else:
    print("Invalid choice. Please enter blue pill or red pill...hint pick the blue pill.")
    