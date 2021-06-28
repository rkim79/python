# I'm gonna make a war game from scratch

from random import shuffle

# global variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 10, 'Ace': 11}

# alternative way to generate the dictionary using enumerate()
'''
value = {}
for v, k in enumerate(ranks):
    value[k] = v
'''

# Card class for each card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self, suit, rank):
        return f'{self.rank} of {self.suit}'

# Deck class for each game
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle_cards(self):
        shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# Hand class for each player
class Hand:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def add_cards(self, card):
        self.cards.extend(card)

    def draw_a_card(self):
        return self.cards.pop()

# game logic

war_rule = 5
game_on = True
at_war = False
exit = False

while not exit:
    print('Welcome to the War Game!')

    # initialize
    game_deck = Deck()
    game_deck.shuffle_cards()
    game_round = 1

    player1_hand = Hand()
    player2_hand = Hand()

    for i in range(26):
        player1_hand.cards.append(game_deck.deal())
        player2_hand.cards.append(game_deck.deal())

    while game_on:
#        print(f'Round {game_round}: ', end='')

        player1 = []
        player2 = []

        if player1_hand.__len__() > war_rule:
            player1.append(player1_hand.draw_a_card())
        else:
            print('Player 2 has won the game! Player 1 have not enough cards.')
            exit = True
            break
        if player2_hand.__len__() > war_rule:
            player2.append(player2_hand.draw_a_card())
        else:
            print('Player 1 has won the game! Player 2 have not enough cards.')
            exit = True
            break

        if values[player1[-1].rank] > values[player2[-1].rank]:
            player1_hand.add_cards(player1 + player2)
            print(f'Round {game_round}: Player 1 has won.', end='') 
            print(f'\t Cards Letf: {len(player1_hand)} vs {len(player2_hand)}')
            game_round += 1
            continue
        elif values[player1[-1].rank] < values[player2[-1].rank]:
            player2_hand.add_cards(player1 + player2)
            print(f'Round {game_round}: Player 2 has won.', end='')
            print(f'\t Cards Left: {len(player1_hand)} vs {len(player2_hand)}')
            game_round += 1
            continue
        else:
            while True:
                print(f'Round {game_round}: War!\t\t  ', end='')
                game_round += 1
                if len(player1_hand) < war_rule:
                    print('Player 2 has won the game! Player 1 have not enough cards.')
                    exit = True
                    game_on = False
                    break
                elif len(player2_hand) < war_rule:
                    print('Player 2 has won the game! Player 1 have not enough cards.')
                    exit = True
                    game_on = False
                    break

                for i in range(war_rule):
                    player1.append(player1_hand.draw_a_card())
                    player2.append(player2_hand.draw_a_card())

                if values[player1[-1].rank] > values[player2[-1].rank]:
                    player1_hand.add_cards(player1 + player2)
                    print(f'\tCards Left: {len(player1_hand)} vs {len(player2_hand)}')
                    break
                elif values[player1[-1].rank] < values[player2[-1].rank]:
                    player2_hand.add_cards(player1 + player2)
                    print(f'\tCards Left: {len(player1_hand)} vs {len(player2_hand)}')
                    break
                else:
                    print(f'\tCards Left: {len(player1_hand)} vs {len(player2_hand)}')
                    continue

# This took a long time to finish. The codes look inefficient.