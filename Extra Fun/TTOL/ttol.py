import pickle  # Pickle essentially obscures data we give it until later need

def store_info(path_name="data.bin"):  # Handler to pickle some data
    data = {} # Empty dictionary to hold our string then our bool
    num_true = 2 # Number of truths we want
    num_false = 1 # Number of lies we want
    def get_boolean(): # Handler to get a boolean value from an input we will use later on
        x = input(f"Is this True or False?\n> ") # Basic input
        while x not in ["True", "true", "False", "false"]: # If the input doesn't match what I want in the list, keep asking
            x = input(f"Is this True or False?\n> ")            
        if x.lower().strip() == "true": # Basic assignment to get a proper boolean value
            return True
        elif x.lower().strip() == "false":
            return False
    for i in range(0, 3): # Loop to start asking for the statements
        a = input(f"What is the #{i+1} statement?\n> ") # Basic input
        x = get_boolean() # This is where we used the above function to get a boolean value
        if x:             # This statement here makes sure that we don't go under the amount of trues and falses we want
            num_true -= 1 # Simply: If I got a true, then subtract one from the total of trues available, and same for false
        else:
            num_false -= 1
        if num_true < 0: # If we do go under the limits, then exit the function
            return print("There are too many true statements!")
        elif num_false < 0:
            return print("There are too many false statements!")
        data[a] = x
    if len(data) < 3: # Make sure we didn't type anything twice
        return print("You have too few arguments!\nMaybe you typed the same thing twice?")
    with open(path_name, 'wb') as f: # This is how we pickle the data to another file
        pickle.dump(data, f) # .dump() dumps the data into a file that we want
    return print("Stored your information successfully!") # Confirmation message


def play(path="data.bin"): # Handler to actually play
    with open(path, 'rb') as f: # Un-pickle the file we created before
        param = pickle.load(f) # Assign the data (a dictionary) to a variable called param
    for i in range(0,len(param)): # This is a for loop to list all the options -- very bulky to do
        print(f"({i+1}) {list(param.keys())[i]}") # This is just a print statement beautifying the options to make it readable
    answer = int(input("Which one is a lie?\n(number)> ")) # Ask for the answer based on the options above
    if not list(param.items())[answer-1][1]: # Check if the answer is false, and if so, print that you won
        print("You won!")
    else:
        print("You lost!")

store_info() # Run the pickling handler
play() # Play the game
