import random

print("Spades!")
input("press enter to play")
print("pick your card")

cards = ["AH","2H","3H", "4H", "5H", "6H", "7H", "8H", "9H", "JH", "QH", "KH","AS","2S","3S", "4S", "5S", "6S", "7S", "8S", "9S", "JS", "QS", "KS", "AD","2D","3D", "4D", "5D", "6D", "7D", "8D", "9D", "JD", "QD", "KD", "AC","2C","3C", "4C", "5C", "6C", "7C", "8C", "9C", "JC", "QC", "KC"]

shuffle_cards = random.sample(cards, len(cards))

quarter = len(shuffle_cards) // 4

your_cards = shuffle_cards[0:quarter]
opps_cards1 = shuffle_cards[quarter : quarter * 2]
opps_cards2 = shuffle_cards[quarter * 2 : quarter * 3]
opps_cards3 = shuffle_cards[quarter * 3 :]

print(your_cards)
print(opps_cards1)
print(opps_cards2)
print(opps_cards3)

print("Player to the left of the dealer goes first...")
print("player 2 goes first")

for i in opps_cards2:   
    if "A" in i and "S" not in i:
        player2_downcard = i
        break
    else:
        if "S" not in i:
            player2_downcard = i



print("player 2 places down card: " + player2_downcard)


    

