first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}, how are you today?"
print(message)
response = input(">")

if(response == "good"):
    print("Great!")
elif(response == "not good"):
    print("Sorry to hear that")
else:
    print("hmmm....interesting")