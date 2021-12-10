from art import logo
import os


print(logo)

bid_again = True
bid_list = {}

def search_winner():
    higher_price = 0
    name_winner = ""
    for name in bid_list:
        price = bid_list[name]
        if price > higher_price:
            higher_price = price
            name_winner = name

    print(f"The winner is {name_winner}, with bid ${higher_price}")

while bid_again == True:
    bidder_name = input("Whats your name?\n")
    bidder_price = int(input("Your bid?\n$"))
    bid_list[bidder_name] = bidder_price
    ask = input("Any bid higher? Yes/No\n").lower()
    if ask == "yes":
        bid_again = True
        os.system("cls")
    else:
        bid_again = False
        search_winner()


