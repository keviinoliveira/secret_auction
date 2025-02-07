import art_init

def rec_bid (name_bid, price_bid, bids):
    if (name_bid in bids) and (bids[name_bid] < price_bid):
        bids[name_bid] = price_bid
    else:
        bids[name_bid] = price_bid
    return bids

def max_bid (bids):
    max_price = 0
    for bid in bids:
        if (bids[bid] > max_price):
            max_price = bids[bid]
            name_winner = bid
    return max_price, name_winner

print(art_init.art)
print("Welcome to the secret auction program.")

bids = {}
auction = True
while (auction == True):
    name_bid = input("What is your name?: ")
    price_bid = int(input("What is your bid?: $"))
    rec_bid(name_bid=name_bid, price_bid=price_bid, bids=bids)
    new_bids = input ("Are there any other bidders? Type 'yes' or 'no' ")
    if new_bids == 'no':
        auction = False
    elif new_bids == 'yes':
        continue
    else:
        print("Comand not found")

max_price, name_winner = max_bid(bids)
print(f"The winner is {name_winner} with a bid of ${max_price}")