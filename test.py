first_name = "alex"
last_name = "rogan"
full_name = f"{first_name} {last_name}"
famous_person = "Centauri"
centauri_message = "Always trust Centauri, my boy."
print(centauri_message)
message = f"Hello, {full_name.title()}, how are you today?"
print(message)
response = input(">")

if(response == "good"):
    print("Great!")
elif(response == "not good"):
    print("What?! Don't you want to be a Starfighter?")
else:
    print("hmmm....nevermind that...all you need to know is trust Centauri.")