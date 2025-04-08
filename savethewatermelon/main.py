import domains
import display
import random

def domain_selection():
    """
    User selects the domain based on the given selection and the return will be a random single word
    dom_selection: takes user selection of domain in integer format; For example,
    1--> Animals; 2--> Cities
    :return: list of a random selected element from the domain
    """
    while True:
        print("Select the domain")
        print("1. Animals")
        print("Select an option from the menu. You can press + for a hint")
        print("x to exit the game")
        dom_selection = input("What is your selection? ")
        if dom_selection == 'x' or dom_selection == 'X':
            print("Goodbye")
            exit(0)
        elif ord(dom_selection) > 57 or ord(dom_selection) < 47:
            print("Invalid selection - not a number")
            print("Try again")
            continue
        elif int(dom_selection) != 1:
            print("Enter a valid number\n")
        elif int(dom_selection) == 1:
            return random.sample(domains.animals,1)  # select the random animal from the animal list defined in domains.py

def hint(user_domain):
    file = open("animals.txt", "r")
    hint_list = [] # saving the hint in the list
    while True:     # loop to read the file
        x = file.readline() # read the first line from the file
        # the following lines gets the hint of the selected animal out of many animals and hints
        if x.startswith("@"):   # the word starts with @ is the word to be guessed.
                                # The @ in the file is used to differentiate animal name and the corresponding hint
                                # if the line starts with @, it is an animal name
            x = x.upper()   # make the guess word in uppercase
            if x[1:-1] == user_domain[0]:   # compare the read line with the selected animal name, and add relevant hint of the selected animal
                while True:     # this nested loop is used to fetch multiline hints and save in the hint list of the selected animal
                    x = file.readline() # read the next line when the animal name in the file is same as the selected animal name
                    if not x.startswith("@"):   # there are two dconditions when the next line is read;
                                                # First condition: when the next line does not start with @,
                                                # this means the next line contains hint of an animal
                        hint_list.append(x)     # save the hint in the list
                        if x == "": break  # end of file if the hint is the last in the file
                    if x.startswith("@"):   # Second condition: when the next line starts with @, there is no hint available, and
                                            # the next line is an animal name
                        break               # break; the section of the hint is ended, end of nested while loop
        if x == "":     # end of file
            break
    file.close()

    print(hint_list[0])
    return None

def user_guess(user_domain, l):
    """
    Takes user guess; there are three possibilities: a. new wrong guess; b. duplicated wrong guess; c. new correct guess; d. duplicated correct guess
    :param user_domain: a single random element (dtype: list)
    :param l: user correct guess saved in the list (dtype: list)
    :return: None
    """

    wrong_guess = []  # saving the user's wrong guesses
    wrong = 0
    while True:
        user_input = input("Enter your guess: ").upper()  # Takes user input as character and convert into uppercase

        # Check for a valid input
        if user_input == "+":
            hint(user_domain)
            continue
        elif not (ord(user_input) >= 65 and ord(user_input) <= 90): # Accepts only alphabets
            print("Invalid input - Only letters A-Z or a-z")
            continue

        if user_input in wrong_guess:  # Check if the guess is already in the wrong guess list
            print("Already used and was WRONG, try again")
        elif user_input in l:  # Check if the guess is already in the correct guess list
            print("This guess is already used and it is CORRECT")
        elif user_input not in user_domain[0]:  # Append the wrong guess in the wrong guess list
            wrong_guess.append(user_input)
            print("You guessed incorrectly")
            wrong += 1
            display.display(wrong)
            print(''.join(l))
            if wrong == 6: print("This is your last attempt")
            if wrong == 7:
                print(f"The animal is {user_domain[0]}")
                break
        else:
            # the last possibility is an obvious case; the user guess is correct.
            for i in range(0,len(user_domain[0])):  # checks if the user guessed char appears more than once in the word
                if user_input == user_domain[0][i]:  # check user guessed char against every index in the word
                    l[i] = user_input  # insert the correct guessed char in the correct guess list (l) at the correct index
            # print(l)
            print(''.join(l))  # join the elements of list into a single word
            if "".join(l) == user_domain[0]:
                print("Good job!!")
                break

def main():
    l = []  # user correct guess saved in the list (dtype: list)
    user_domain = domain_selection()  # user_domain contains the list of a single word
    chr_rnd_animals = random.sample(user_domain[0],1)  # the game starts with providing a random single char hint (k=1).
    # Can be changed to insert a multiple correct random chars (k=2 or greater)
    # chr_rnd_animals holds a list of a random single char of the random single word
    # print(user_domain[0]) for test only
    for i in range(0, len(user_domain[
                              0])):  # initialize the correct guess list with the number of dashes equal to the length of the word to be guessed
        l.append("_")
    for i in range(0, len(user_domain[0])):  # run the loop equal to the length of the word
        if chr_rnd_animals[0] == user_domain[0][i]:  # match the single char with each char in the word
            l[i] = chr_rnd_animals[0]  # if the match is True; insert the single char in the guess list at index i
        if " " == user_domain[0][i]:  # check for the space in a word
            l[i] = " "  # if there is a space, add space in the guess list at index i
    # print(l)
    print("".join(l))  # join the elements of list into a single word
    user_guess(user_domain, l)


if __name__ == "__main__":
    main()
