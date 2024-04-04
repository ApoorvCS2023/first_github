#Apoorv Awasthi
#U03660678
#This python program is used to get cards, we first take two lists containing both the suits and ranks, we then have
#a function which makes a deck of the cards, then we have a value returning function which takes three arguments and
# and returns the deck of dealt cards and finally we have the main fucntion which calls all the other functions and 
#displays the output accordingly.
import random
l1 = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
l2 = ["Clubs", "diamonds", "hearts", "spade"]
local_list = []

def function1():
    for ele in l1:
        for elem in l2:
            local_list.append(f"{ele} of {elem}")
    return local_list

def function2(n_cards, local_list):
    drawn_cards = []
    for i in range(n_cards):
        selected = random.choice(local_list)
        local_list.remove(selected)
        drawn_cards.append(selected)
    return drawn_cards

def main():
    cards = int(input("How many cards to draw from deck?: "))
    while cards > 52 or cards <= 0:
        print("Invalid entry, you can only draw between 1 & 52 cards!")
        cards = int(input("How many cards to draw from deck?: "))
        
    function1()
    selected_cards = function2(cards, local_list)
    
    for index, card in enumerate(selected_cards, 1):
        if index == 1:
            print(f"your {index}st card is the {card}")
        elif index == 2:
            print(f"your {index}nd card is the {card}")
        elif index == 3:
            print(f"your {index}rd card is the {card}")
        elif index == 52 or index==cards:
            print(f"and your last card is the {card}")    
        else:
            print(f"your {index}th card is the {card}")

main()
