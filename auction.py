import os
auction_list={}
print("Welcome to action")
continue_bid ='y'
while continue_bid=='y':
    name=input("Name: ")
    bid=int(input("Bid: "))
    auction_list[name]=bid
    continue_bid= str(input("Continue?").lower())
    os.system('cls')

bid_winner=""
winning_bid=0
for bid in auction_list:
        if auction_list[bid]>winning_bid:
            winning_bid=auction_list[bid]
            bid_winner=bid
print(str(bid_winner)+" has won with "+str(winning_bid))