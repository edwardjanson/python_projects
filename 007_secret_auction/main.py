from replit import clear

print("Welcome to the secret auction program.")

add_bidders = "yes"
bidders = []

def new_bidder(bidder_name, bid_amount):
  individual_bidders = {}
  individual_bidders["name"] = name
  individual_bidders["bid"] = bid
  bidders.append(individual_bidders)

while add_bidders == "yes":
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  new_bidder(name, bid)
  add_bidders = input("Are the any other bidders? Type 'yes' or 'no'. ")
  clear()

highest_bid = 0
total_bidders = len(bidders)

for all_bids in range(total_bidders):
  bid_amount = bidders[all_bids]["bid"]
  if bid_amount > highest_bid:
    highest_bid = bid_amount
    highest_bidder = bidders[all_bids]["name"]

print(f"The winner is {highest_bidder} with ${highest_bid}.")
