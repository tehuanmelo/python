
from art import logo

bids = {}
print(logo)
print("Welcome to the secret auction program.")

def find_highest(bids):
  max_bid = 0
  for bidder in bids:
    if bids[bidder] > max_bid:
      max_bid = bids[bidder]
      
  for bidder in bids:
    if bids[bidder] == max_bid:
      os.system('clear')
      print(f'The winner is {bidder} with ${bids[bidder]} bid')

more_bidders = True
while more_bidders:
  bidder_name = input("What is your name: ")
  bidder_bid = int(input("What's your bid?: $"))
  bids[bidder_name] = bidder_bid
  flag = input("Are there any other bid?: Yes or No ").lower()
  if flag == "yes":
    os.system('clear')
  else:
    more_bidders = False
    find_highest(bids)
    
