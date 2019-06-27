import pickle  # Pickle essentially obscures data we give it until later need

def store_info(path_name="ttol.bin",statements=3):  # Handler to pickle some data to use later
    if statements < 2: # Lets not play a game with only 1 correct answer :D
        return print("You need to have a minimum of 2 statements!")
    data = {} # Empty dictionary to hold our string then our bool
    num_true = statements-1 # Number of truths we want
    num_false = 1 # Number of lies we want
    def get_boolean(): # Handler to get a boolean value from an input we will use later on
        true_keywords = ["True", "true", "1", "T", "t"] # List of all the acceptable values for true
        false_keywords = ["False", "false", "0", "F", "f"] # List of all the acceptable values for false
        x = input("Is this True or False?\n> ") # Ask for true or false
        while x not in true_keywords + false_keywords: # If the input doesn't match what I want in the list, keep asking
            print("Please type a boolean value!")
            x = input(f"Is this True or False?\n> ")            
        if x.lower().strip() in true_keywords: # Basic assignment to get a proper boolean value
            return True
        elif x.lower().strip() in false_keywords:
            return False
    for i in range(0, statements): # Loop to start asking for the statements
        a = input(f"What is the #{i+1} statement?\n> ") # Basic input
        x = get_boolean() # This is where we used the above function to get a boolean value
        if x:             # This statement here makes sure that we don't go under the amount of trues and falses we want
            num_true -= 1 # Simply: If I said a true statement, then subtract one from the total of trues available, and same for false
        else:
            num_false -= 1
        if num_true < 0: # If we do go under the limits, then exit the function
            return print("There are too many true statements!")
        elif num_false < 0:
            return print("There are too many false statements!")
        data[a] = x # Finally store this data in a seperate slot in the dictionary
    if len(data) < statements: # Make sure we didn't type anything twice
        return print("You have too few arguments!\nMaybe you typed the same thing twice?")
    with open(path_name, 'wb') as f: # This is how we pickle the data to another file
        pickle.dump(data, f) # .dump() dumps the dictionary we have into a file that we want
    return print("Stored your information successfully!\n") # Confirmation message that we stored our data


def play(path="ttol.bin"): # Handler to actually play
    # Function to get an integer value from the input() function. This one looks different because it servers more uses
    def get_integer(message, default=None):
        x = input(message) # Get an input
        if not x and default: # If there is no input and we are given a default value, return the default value
            return default
        else:
            try: # See if the person gave us an integer value. If so? Great!
                x = int(x)
            except ValueError: # If they gave something that can't be converted to an integer, run this function again and again
                print("Enter an integer!")
                return get_integer(message)
        return x # Return the integer value
    try: # Let's make this easier for the player so they only have to run 1 function, the play() function
        with open(path, 'rb') as f: # Un-pickle the file we created before
            param = pickle.load(f) # Assign the data (a dictionary) to a variable called param
    except FileNotFoundError: # If there isn't a file with what we want, we will make 1
        print("There doesn't seem to be a file to play with. Let's make one")
        # Run our previous function that pickles some data it'll ask us for, and we use our get_integer() function
        store_info(path_name=path, statements=get_integer("How many statements do you want to play with?\n(Default is 3) > ", default=3))
        with open(path, 'rb') as f:  # Un-pickle the file we created before again
            param = pickle.load(f) # Store it to param
    for i in range(0,len(param)): # This is a for loop to list all the options from our param
        print(f"({i+1}) {list(param.keys())[i]}") # This is just a print statement beautifying the options to make it readable
    def get_answer(): # Function to get the answer from the human after viewing the possible options
        answer = get_integer(f"Which one is a lie?\n(1-{len(param)}) > ") # Ask for the answer based on the options above
        if answer <= 0 or answer > len(param): # If the answer is 0 or less, it will become negative and break our game, we dont want that
            print("Enter a valid answer choice!") # If its more than what we have for options, it'll error out so we don't want it either
            return get_answer() # Re-run the function to get the answer
        return answer-1 # Return an index-able format for our list
    choice = list(param.values())[get_answer()] # Convert the values from the dictionary into a list of boolean values, then select the answer
    if not choice: # If the answer is False, then you win!
            print("You guessed correctly!")
    else:
            print("You didn't guess the right one!")

play() # Play the game
