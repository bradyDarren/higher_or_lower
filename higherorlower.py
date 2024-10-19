import random
from art import logo, vs
from data import ig_dict

# takes list input and returns a data associated with a random selection from the input list.
# the output will include the following the name of the instagram account, a description of what is displayed on the account
# and where is the person, place, or thing from that owns the account.
def rand_account(data_set):
    rand_selection = random.choice(data_set)
    # print(rand_selection["name"]) - test line
    name = rand_selection["name"]
    description = rand_selection["description"]
    country = rand_selection["country"]
    follower_count = rand_selection["follower count"]
    return [name, description, country, follower_count]

print(rand_account(ig_dict)[0])

def start():
    print(logo)
    correct = True
    rand_account_a = rand_account(ig_dict)
    rand_account_b = rand_account(ig_dict)
    while correct:
        comp_a = f"Compare A: {rand_account(ig_dict)[0]}, "
        comp_b = rand_account(ig_dict)
        print(f"Compare A: {comp_a}.")
        print(vs)
        print(f"Against B: {comp_b}.")
        break

start()
