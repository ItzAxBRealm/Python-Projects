
print("Welcome to the secret auction program.")
another_try = False
dictionary = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while another_try == False:
  name = input("What is your name?: \n")
  bid = int(input("What's your bid?: \n$"))
  go_again = input("Are there any more bidders? Type 'Yes' or 'No'.\n").lower()
  dictionary[name] = bid
  if go_again == "yes":
    pass
  elif go_again == "no":
    another_try = True
    find_highest_bidder(dictionary)
  else:
    print("Invalid Input")
    another_try = True