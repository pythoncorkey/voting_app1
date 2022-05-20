import random
import time

print("Welcome to Ella's voting program!")
results = {}
votes = 0
selections = input("what are you voting on?, separate selections with a comma ").split(",")
count_list = []
assist = input("would you like to randomly select a winner? y/n: ")

if assist == "y":
    print(f"the random winner is {random.choice(selections)}")
else:
    voters = int(input("how many people are voting?: "))
    while votes < voters:
        name = input("What is your name?")
        selection = input(f"select one of the following {selections}")
        if selection in selections:
            results[name] = selection
            votes += 1
            count_list.append(selection)
        else:
            print("please reenter a proper selections ")


    winner_dict = {}
    for i in range(len(selections)):
        winner_dict[count_list[i]] = count_list.count(count_list[i])

    max_key = max(winner_dict, key=winner_dict.get)
    print("calculating results...")
    time.sleep(3)
    print(f"{max_key} is the winner with {winner_dict[max_key]} votes!")

    complete_results = input("would you like to see the complete results?y/n: ")
    if complete_results == "y":
        for key, value in results.items():
            print(f"{key.title()} voted for {value.upper()}", end=" | ")
            print("thanks for voting, Goodbye!")
    else:
        print("thanks for voting, Goodbye!")


