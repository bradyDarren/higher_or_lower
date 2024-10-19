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

account1 = rand_account(ig_dict)[3]
print(account1)
account2 = rand_account(ig_dict)[3]
print(account2)
print(max(account1,account2))

def start():
    print(logo)
    correct = True
    rand_account_a = rand_account(ig_dict)
    rand_account_b = rand_account(ig_dict)
    while correct:
        comp_a = f"Compare A: {rand_account_a[0]}, {rand_account_a[1]}, from {rand_account_a[2]}."
        comp_b = f"Against B: {rand_account_b[0]}, {rand_account_b[1]}, from {rand_account_b[2]}."
        print(comp_a)
        print(vs)
        print(comp_b)
        user_selection = input("Which of the above meantioned has more followers? Type 'A' or 'B': ").lower()

        
# start()
