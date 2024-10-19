import random
from art import logo, vs
from data import ig_dict

# takes list input and returns a list associated with a random selection from the input list.
# the output will include the following the name of the instagram account, a description of what is displayed on the account
# and where is the person, place, or thing from that owns the account.
def rand_account(data_set):
    rand_selection = random.choice(data_set)
    #  - test line
    # print(rand_selection["name"])
    name = rand_selection["name"]
    description = rand_selection["description"]
    country = rand_selection["country"]
    follower_count = rand_selection["follower count"]
    return [name, description, country, follower_count]

# - test line
# print(rand_account(ig_dict)[0])

def highest_followers(a_count, b_count):
    if a_count > b_count:
        return "a"
    else: 
        return "b"

def start():
    print(logo)
    correct = True
    rand_account_a = rand_account(ig_dict)
    count = 0
    while correct:
        rand_account_b = rand_account(ig_dict)
        comp_a = f"Compare A: {rand_account_a[0]}, {rand_account_a[1]}, from {rand_account_a[2]}."
        comp_b = f"Against B: {rand_account_b[0]}, {rand_account_b[1]}, from {rand_account_b[2]}."
        print(comp_a)
        print(vs)
        print(comp_b)
        correct = highest_followers(rand_account_a[3],rand_account_b[3])
        user_selection = input("Which of the above meantioned has more followers? Type 'A' or 'B': ").lower()
        if user_selection != correct:
            print(f"\n Sorry that wrong. Final score: {count}")
            correct = False
        else:
            print("\n" * 30)
            print(logo) 
            count += 1
            rand_account_a = rand_account_b
start()
