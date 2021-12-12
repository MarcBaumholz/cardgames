import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()   

class Player:

    def __init__(self,name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        #if a list => add multiple cards else add single card
       if type(new_cards) == type([]):
           #list of cards
           self.all_cards.extend(new_cards)
       else:
           #single card
           self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'   


# Test functionality
'''
two_hearts = Card("Clubs", 'Three')
new_deck = Deck()
new_player = Player('Jose')
print(new_player)

print(two_hearts)
print(new_deck.all_cards[0])
print(new_deck.all_cards[-1])
for card_obejct in new_deck.all_cards:
    print(card_obejct)

new_deck.shuffle()
mycard = new_deck.deal_one()
new_player.add_cards(mycard)
new_player.add_cards([mycard,mycard,mycard])

print(new_player.all_cards[2])

new_player.remove_one()
print(new_player)
'''
#Game setup

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

deck_length = len(new_deck.all_cards)
for x in range(deck_length//2):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

#Game logic

round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break

    #start new round grabbing one card each 
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    at_war = True
    
    while at_war:
        #player 1 higher card
        # with -1 compare with the newest card => gets appended in the end
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        #player 2 higher card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False
        
        else:
            print('War started')

            if len(player_one.all_cards) < 3:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
        
