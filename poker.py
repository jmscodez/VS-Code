import random
import sys
from typing import LiteralString


def poker():
    # Define the card values and suits
    values = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    suits = ["hearts", "diamonds", "clubs", "spades"]

    Game_Played = 0

    # Create a dictionary
    cards = {}

    # Generate the card variables
    for value in values:
        for suit in suits:
            number_suit = f"{value}_{suit}"
            cards[number_suit] = f"{value.capitalize()} of {suit.capitalize()}"

    #Dealt Cards
    Dealt_One = ""
    Dealt_Two = ""

    #Table Cards
    Card_One = ""
    Card_Two = ""
    Card_Three = ""
    Card_Four = ""
    Card_Five = ""

    #Deal Hand 
    def card_deal():
        global Dealt_One
        global Dealt_Two
        user_input: str = input('\nPress D to Deal Cards or Q to quit\n')

        if user_input.upper() == 'D':
            selected_cards = random.sample(list(cards.keys()), 2)
            print('\nYour Cards:\n')
            Dealt_One = cards.pop(selected_cards[0])
            Dealt_Two = cards.pop(selected_cards[1])
            print(Dealt_One)
            print(Dealt_Two)
            print('\n')
        elif user_input.upper() == "Q":
            sys.exit('Thanks for playing!\n')
        else:
            print('\nPlease select either D or Q.\n')
            return card_deal()

    card_deal()

    #add a game played counter
    Game_Played += 1

    #flop
    def Flop():
        user_input: str = input('\nSelect D to see the flop \n')
        global Dealt_One
        global Dealt_Two
        print('Your Cards:\n')
        print(Dealt_One)
        print(Dealt_Two)
        print('\n')
        global Card_One
        global Card_Two
        global Card_Three
        if user_input.upper() == 'D':
                selected_cards = random.sample(list(cards.keys()), 3)
                print('\nCards on Table::\n')
                Card_One = cards.pop(selected_cards[0])
                Card_Two = cards.pop(selected_cards[1])
                Card_Three = cards.pop(selected_cards[2])

                print(Card_One)
                print(Card_Two)
                print(Card_Three)
                print('\n')
        else:
                print('\nSelect D to see the flop')
                return Flop()

    Flop()



    #Turn
    def Turn():
        user_input: str = input('\nSelect D to see the Turn \n')
        global Dealt_One
        global Dealt_Two
        global Card_One
        global Card_Two
        global Card_Three
        global Card_Four
        print('Your Cards:\n')
        print(Dealt_One)
        print(Dealt_Two)
        print('\n')

        if user_input.upper() == 'D':
                
                selected_cards = random.sample(list(cards.keys()), 1)
                Card_Four = cards.pop(selected_cards[0])
                print('\nCards on Table:\n')
                print(Card_One)
                print(Card_Two)
                print(Card_Three)
                print(Card_Four)
                
                print('\n')
        else:
                print('\nSelect D to see the Turn')
                return Turn()
        
    Turn()

    #River

    def River():
        user_input: str = input('\nSelect D to see the River \n')
        global Dealt_One
        global Dealt_Two
        global Card_One
        global Card_Two
        global Card_Three
        global Card_Four
        global Card_Five
        print('Your Cards:\n')
        print(Dealt_One)
        print(Dealt_Two)
        print('\n')

        if user_input.upper() == 'D':
                
                selected_cards = random.sample(list(cards.keys()), 1)
                Card_Five = cards.pop(selected_cards[0])
                print('\nCards on Table:\n')
                print(Card_One)
                print(Card_Two)
                print(Card_Three)
                print(Card_Four)
                print(Card_Five)
                
                print('\n')
        else:
                print('\nSelect D to see the Turn')
                return Turn()
        
    River()

    
    #------------------------------------------------------------------

    # Extract the number from the card variable and convert it to an integer
    number1 = Dealt_One.split(" ")[0]
    number2: LiteralString = Dealt_Two.split(" ")[0]
    number3 = Card_One.split(" ")[0]
    number4 = Card_Two.split(" ")[0]
    number5 = Card_Three.split(" ")[0]
    number6: LiteralString = Card_Four.split(" ")[0]
    number7 = Card_Five.split(" ")[0]

    #Convert to integers
    number_words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "jack": 11,
        "queen": 12,
        "king": 13,
        "ace": 14
    }

    
    #convert each number from text to the interger by referncing number_words dictionary. So if number1 is "two", number1 will be 2. do this for number1 to number7. Then print just number1
    number1 = number_words[number1.lower()]
    number2 = number_words[number2.lower()]
    number3 = number_words[number3.lower()]
    number4 = number_words[number4.lower()]
    number5 = number_words[number5.lower()]
    number6 = number_words[number6.lower()]
    number7 = number_words[number7.lower()]


    #find the suit of each card. We will call these values suit1, suit2, suit3, suit4, suit5, suit6, suit7. For example, if Card_One is "Nine of Hearts", suit1 will be "hearts".
    suit1 = Card_One.split(" ")[2].lower()
    suit2 = Card_Two.split(" ")[2].lower()
    suit3 = Card_Three.split(" ")[2].lower()
    suit4 = Card_Four.split(" ")[2].lower()
    suit5 = Card_Five.split(" ")[2].lower()
    suit6 = Dealt_One.split(" ")[2].lower()
    suit7 = Dealt_Two.split(" ")[2].lower()



    hand_values = [number1, number2, number3, number4, number5, number6, number7]

    #make a counter that can count how many of each interger there are. Example,if there are two 7s, the output for the variable Seven should be 2. if there 0, the output would be 0. do this for all numbers 1 to 14. Only use variables that were used before. for the new variables, they should be named as the text of the interger (ex: 2 = two)
    # Count the occurrences of each number in the hand
    number_counts = {
        "zero": hand_values.count(0),
        "one": hand_values.count(1),
        "two": hand_values.count(2),
        "three": hand_values.count(3),
        "four": hand_values.count(4),
        "five": hand_values.count(5),
        "six": hand_values.count(6),
        "seven": hand_values.count(7),
        "eight": hand_values.count(8),
        "nine": hand_values.count(9),
        "ten": hand_values.count(10),
        "jack": hand_values.count(11),
        "queen": hand_values.count(12),
        "king": hand_values.count(13),
        "ace": hand_values.count(14)
    }



    #now do the same thing but instead of the numbers, do it with suits. it shoudl look the same as above
    suit_values = [suit1, suit2, suit3, suit4, suit5, suit6, suit7]
    suit_counts = {
        "hearts": suit_values.count("hearts"),
        "diamonds": suit_values.count("diamonds"),
        "clubs": suit_values.count("clubs"),
        "spades": suit_values.count("spades")
    }


    print("\nYour Outcome is:")
    #create a def fuction to evaluate the outcome. Start by evaluating for four of kind. this would mean that there are 4 of any give value in number_counts
    # Evaluate the outcome for Four of a Kind
    def evaluate_outcome():
        if 4 in number_counts.values():
            print("Four of a Kind")    
            return    
        elif 3 in number_counts.values() and 2 in number_counts.values():
            print("Full House")
            return
        elif 5 in suit_counts.values():
            print("Flush")
            return
        
        #create code for a straight
        #####straight missing
        elif 3 in number_counts.values():
            print("Three of a Kind")
            return

        elif 3 in number_counts.values():
            print("You have a pair")
            return
        else:
            print("You have a high card")
            return

    evaluate_outcome()
    print('----------------------------')
    print('Games Played: ' + str(Game_Played))
    print('----------------------------')

poker()







    #sort code only values
    #check 