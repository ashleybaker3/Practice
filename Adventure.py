print("Dragon Age Mini Storytime!")

print("Hello and welcome to a little Dragon Age story. Before we begin, what is your name?")

name = input("Your Name: ")

print(f"Welcome to Thedas, {name}. Let's begin this little adventure! Can you tell me which country you are coming in from?")


country = input("Country: ")

print(f"A pleasure to meet you {name}.")

if country == "Ferelden":
    print(f"Ah, {country}. Heard that place has the best war dogs. A little smelly, though.")

elif country == "Nevarra" or country == "Free Marches":
    print(f"Ah, {country}. Well, that's just a short passage down to here. Must have taken you no time at all!")

elif country == "Tevinter":
    print(
        f"Hm, {country}. Well, so long as the money you bring has value, you're welcome here to me at least. Don't expect the same kindness from others.")

else:
    print(f"Ah, {country}. Never been there myself. You must have travelled pretty far to reach this port here.")

print(f"Say, {name}, you're probably new here.")
join = input("Would you like to come with me into town?" ).lower()

if join.startswith("y"):
    print("Wonderful! Follow me. I'll show you to an inn here on the nicer side of Val Royeaux.")

else:
    print(f"Bit more of an independent spirit in you, {name}? Enjoy your stay, but I suggest staying out of the south side of town if you want to steer clear of trouble.")

if country == "Tevinter":
    print("Ah, but who am I to judge? Perhaps you do seek out some danger.")
