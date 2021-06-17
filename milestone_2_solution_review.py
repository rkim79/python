import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = (
	'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
	'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',
	'Ace'
)

values = {
	'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
	'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
	'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
	'Ace': 11
}

# QUESTION: can I use a list or a tuple of keys of the dictionary, instead of the rank variable?
# 대신 딕셔너리 키로 만든 리스트 를 사용할 수 있지 않을까?

playing = True

class Card:
	"""Attributes for Each Card:"""
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	# String value
	def __str__(self):
		return f'{self.rank} of {self.suit}'

class Deck:
	def __init__(self):
		self.cards = []

		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(suit, rank))

# missing __str__ method impelementation

	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self):
		return self.cards.pop()

class Hand:
	def __init__(self):
		self.cards = []
		self.total = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.total += values[card.rank]

		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):
		if self.total > 21 and self.aces: # MISTAKE: use while not if, because there might be more than 2 aces
			self.total -= 10
			self.aces -= 1

#TODO: implement defalut value instead of hard coding
class Chips:
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def hit(deck, hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck):
	global playing

	while True:
		choice = input('Hit or Stand? ').lower()

		if choice[0] == 'h':
			hit(deck, player_hand)

		elif choice[0] == 's':
			playing = False

		else:
			print('Choose either \'Hit\' or \'Stand\'.')
			continue

		break

# TODO : make another version that using * operand for display the cards
def show_some(player_hand, dealer_hand):
	print('\nDealer\'s Hand:')
	print('<card hidden>')
	print('\n'.join([str(card) for card in dealer_hand.cards[1:]]))

	print('\nPlayer\'s Hand:')
	print('\n'.join([str(card) for card in player_hand.cards]))

def show_all(player_hand, dealer_hand):
	print('\nDealer\'s Hand:')
	print('\n'.join([str(card) for card in dealer_hand.cards]))
	print(f'Dealer\'s Total = {dealer_hand.total}')

	print('\nPlayer\'s Hand:')
	print('\n'.join([str(card) for card in player_hand.cards]))
	print(f'Player\'s Total = {player_hand.total}')

def take_bet(chips):
	while True:

		try:
			chips.bet = int(input('How much would you bet? '))

		except ValueError:
			print('You must input a number, try again!')
			continue

		else:
			if chips.bet > chips.total:
				print(f'You cannot bet more than {chips.total}, try again!')
				continue

			else:
				break

def player_busts(chips):
	print('\nPlayer Busts!')
	chips.lose_bet()

def player_wins(chips):
	print('\nPlayer Wins!')
	chips.win_bet()

def dealer_busts(chips):
	print('\nDealer Busts!')
	chips.win_bet()

def player_lose(chips):
	print('\nDealer Wins!')
	chips.lose_bet()

def push():
	print('\nPlayer and Dealer Tie!')

while True:
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	dealer_hand = Hand()

	chips = Chips()

	take_bet(chips)

	for i in range(2):
		player_hand.add_card(deck.deal())
		dealer_hand.add_card(deck.deal())

	show_some(player_hand, dealer_hand)

	while playing:
		hit_or_stand(deck)
		show_some(player_hand, dealer_hand)

		if player_hand.total > 21:
			player_busts(chips)
			#playing = False
			break

	if player_hand.total <= 21:
		while dealer_hand.total < 17:
			dealer_hand.add_card(deck.deal())

		show_all(player_hand, dealer_hand)

		if player_hand.total > dealer_hand.total:
			player_wins(chips)

		elif dealer_hand.total > 21:
			dealer_busts(chips)

		elif player_hand.total < dealer_hand.total:
			player_lose(chips)

		elif player_hand.total == dealer_hand.total:
			push()

	print(f'\nPlayer have {chips.total} chips.')

	if input('Another Game? Yes or No: ').lower()[0] == 'y':
		playing = True
		continue
	else:
		break