import random
from art import logo, vs
from data import ig_dict

# takes list input and returns a data associated with a random selection from the input list.
def rand_account(data_set):
    rand_selection = random.choice(data_set)
    # print(rand_selection["name"]) - test line
    name = rand_selection["name"]
    description = rand_selection["description"]
    country = rand_selection["country"]
    return name, description, country

print(", ".join((rand_account(ig_dict))))

# def start():
#     print(logo)
#     correct = True
#     while correct: 
#         print(f"Compare A: {rand_account(ig_dict)}.")

