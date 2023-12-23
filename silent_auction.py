import os

print("Welcome to the Silent Auction!!")
auction = {}
names = []
bids = []

more_bidders = True
while more_bidders:
  name = input("What is your name? ")
  bid = input("What is your bid? $")
  names.append(name)
  bids.append(bid)
  auction["name"] = names
  auction["bid"] = bids
  option = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if option == "yes":
    os.system('cls')
    more_bidders = True
  else:
    more_bidders = False
    highest_bid = max(auction["bid"])
    print(f"The winner is {auction['name'][auction['bid'].index(highest_bid)]} with a bid of ${highest_bid}!!")