import pickle

def store_info(path_name="data.bin"):
    data = {}
    num_true = 2
    num_false = 1
    def get_boolean():
        x = input(f"Is this True or False?\n> ")
        while x not in ["True", "true", "False", "false"]:
            x = input(f"Is this True or False?\n> ")            
        if x.lower().strip() == "true":
            return True
        elif x.lower().strip() == "false":
            return False
    for i in range(0, 3):
        a = input(f"What is the #{i+1} statement?\n> ")
        x = get_boolean()
        if x:
            num_true -= 1
        else:
            num_false -= 1
        if num_true < 0:
            return print("There are too many true statements!")
        elif num_false < 0:
            return print("There are too many false statements!")
        data[a] = x
    if len(data) < 3:
        return print("You have too few arguments!\nMaybe you typed the same thing twice?")
    with open(path_name, 'wb') as f:
        pickle.dump(data, f)
    return print("Stored your information successfully!")


def play(path="data.bin"):
    with open(path, 'rb') as f:
        param = pickle.load(f)
    for i in range(0,len(param)):
        print(f"({i+1}) {list(param.keys())[i]}")
    answer = int(input("Which one is a lie?\n> "))
    if not list(param.items())[answer-1][1]:
        print("You won!")
    else:
        print("You lost!")

store_info()
play() 
