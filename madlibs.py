import random 

default_adjectives = ["funny", "exciting", "boring", "adventurous"]
default_verbs = ["run", "jump", "swim", "dance"]
default_nouns = ["cat", "dog", "car", "house"]
default_famous_people = ["Albert Einstein", "Marie Curie", "Isaac Newton", "Ada Lovelace"]
default_places = ["park", "beach", "mountains", "city"]

#Helper Function to get user input or default value
def get_input(prompt, default_list):
        user_input = input(prompt + " (or press Enter to use a default): ")
        if user_input.strip() == "":
            return random.choice(default_list)
        return user_input

#Saving story function
def save_story(story):
    """Save the generated story in to files."""
    with open("Saved_stories.txt", "a", encoding="utf-8") as file:
        file.write(story + "\n\n")

#madlib functions

def madlib1():
    print("\n🎉 Let's play Madlib 1! 🎉")

    adjective = get_input("Adjective: ", default_adjectives)
    verb = get_input("Verb: ", default_verbs)
    noun = get_input("Noun: ", default_nouns)
    famous_person = get_input("Famous Person: ", default_famous_people)
    place = get_input("Place: ", default_places)


    madlib = (
        f"\nI love making {adjective} content! 😎\n"
        f"It makes me {verb} whenever I create them. 💡\n"
        f"I love being financially stable and a {noun} content creator. 🏆\n"
        f"I want to be as famous as {famous_person} 🌟\n"
        f"and decorate my {place} with cool stuff! 🏠\n"
    )
    save_story(madlib)
    print(madlib)

def madlib2():

    print("\n🎉 Let's play Madlib 1! 🎉")

    noun1 = get_input("Noun: ", default_nouns)
    place = get_input("Place: ", default_places)
    verb = get_input("Verb: ", default_verbs)
    person = get_input("Person: ", default_famous_people)
    adjective = get_input("Adjective: ", default_adjectives)
    noun = get_input("Noun: ", default_nouns)


    madlib = (
        f"\nThe best memory in my school is the {noun1} day. 📚\n"
        f"It was the best ever memory I had in my {place} days. 🏫\n"
        f"I was with my friends and we were all {verb} at the jokes we made. 😂\n"
        f"My {person} was also with me and we both joined the photography {noun2}. 📸\n"
        f"It was such a {adjective} day! 🌞\n"
    )

    print(madlib)
    save_story(madlib)

print("🎮 Welcome to Madlibs! 🎮 Choose a madlib to play:")
choice = input("Type 1 for Madlib 1 or 2 for Madlib 2: ")
if choice == "1":
    madlib1()
elif choice == "2":
    madlib2()
else:
    print("❌ Invalid choice. Please choose 1 or 2.")


print("Do you want to play again? (yes/no)")

while True:
    play_again = input().lower()
    if play_again == "yes":
        choice = input("Type 1 for Madlib 1 or 2 for Madlib 2: ")
        if choice == "1":
            madlib1()
        elif choice == "2":
            madlib2()
        else:
            print("Invalid choice. Please choose 1 or 2.")
    elif play_again == "no":
        print("👋 Thanks for playing! Goodbye!")
        break
    
#Run the program 
if __name__ == "__main__":
    pass

