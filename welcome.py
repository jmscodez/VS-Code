import random

# Define the card values and suits
values = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
suits = ["hearts", "diamonds", "clubs", "spades"]

# ANSI escape codes for colors
RED = '\033[91m'
RESET = '\033[0m'

# Function to wrap text in color
def colorize_suit(suit):
    if suit in ["hearts", "diamonds"]:
        return f"{RED}{suit}{RESET}"
    return suit

# Card class to represent a single card
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value.capitalize()} of {colorize_suit(self.suit).capitalize()}"

# Deck class to represent a deck of cards
class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in values for suit in suits]
        random.shuffle(self.cards)

    def deal(self, num):
        dealt_cards = []
        for _ in range(num):
            dealt_cards.append(self.cards.pop())
        return dealt_cards

# Function to evaluate the hand
def evaluate_hand(hand):
    # Implement hand evaluation logic
    # For simplicity, we will only detect pairs, two pairs, and three of a kind
    value_counts = {}
    for card in hand:
        if card.value in value_counts:
            value_counts[card.value] += 1
        else:
            value_counts[card.value] = 1
    
    pairs = []
    three_of_a_kind = None
    for value, count in value_counts.items():
        if count == 2:
            pairs.append(value)
        elif count == 3:
            three_of_a_kind = value
    
    if three_of_a_kind:
        return f"Three of a Kind: {three_of_a_kind.capitalize()}s"
    elif len(pairs) == 2:
        return f"Two Pairs: {pairs[0].capitalize()}s and {pairs[1].capitalize()}s"
    elif len(pairs) == 1:
        return f"One Pair: {pairs[0].capitalize()}s"
    else:
        return "High Card"

# Main function to simulate the poker game
def play_poker():
    deck = Deck()
    player_hand = deck.deal(2)
    community_cards = deck.deal(5)
    
    print("Player's Hand:")
    for card in player_hand:
        print(card)
    
    print("\nCommunity Cards:")
    for card in community_cards:
        print(card)
    
    # Combine player hand with community cards
    full_hand = player_hand + community_cards
    outcome = evaluate_hand(full_hand)
    
    print(f"\nOutcome of the Hand: {outcome}")

# Run the poker game
play_poker()