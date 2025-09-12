
def madlib1():
    print("Let's play a game of Madlibs!")

    adjective = input("Adjective: ")
    verb = input("Verb: ")
    noun = input("Noun:")
    famous_person = input("Famous Person: ")
    place = input("Place: ")

    madlib = f"I love making {adjective} content! It makes me {verb} when ever I create them. I love being financially stable and a {adjective} content creator. I want to be as famous as {famous_person} and buy my favourite items and to decorate my {place}."
    print(madlib)

def madlib2():
    adjective = input("Adjective: ")
    verb = input("Verb: ")
    noun1 = input("Noun:")
    noun = input("Noun:")
    person = input("Person: ")
    place = input("Place: ")

    madlib = f"The best memory in my school is the {noun1} day of my school. It was the best ever memory I have in my {place} time. \
         I was with my friends and we were all {verb} for jokes we did. My {person} was also with me and we both were in photography {noun} of our school. It was a very {adjective} day."
    
    
    print(madlib)

print("Welcome to Madlibs! Choose a madlib to play:")
choice = input("Type 1 for Madlib 1 or 2 for Madlib 2: ")
if choice == "1":
    madlib1()
elif choice == "2":
    madlib2()
else:
    print("Invalid choice. Please choose 1 or 2.")
