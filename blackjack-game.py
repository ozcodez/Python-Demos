import random


def give_card():
  cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,11]
  card = random.choice(cards)
  return card

def calculate_cards(cards):

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose "


  if user_score == computer_score:
    return "It is draw "
  elif computer_score == 0:
    return "You lose, opponent has Blackjack "
  elif user_score == 0:
    return "You win with a Blackjack "
  elif user_score > 21:
    return "You lose "
  elif computer_score > 21:
    return "You win "
  elif user_score > computer_score:
    return "You win "
  else:
    return "You lose "

def start_the_game():


  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  dealer_cards = []
  is_game_over = False

  for i in range(2):
    user_cards.append(give_card())
    dealer_cards.append(give_card())

  while not is_game_over:
    user_score = calculate_cards(user_cards)
    dealer_score = calculate_cards(dealer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(give_card())
      else:
        is_game_over = True

  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(give_card())
    dealer_score = calculate_cards(dealer_cards)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(user_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  start_the_game()
