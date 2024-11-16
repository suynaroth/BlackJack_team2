import random

cards = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
playerCard = []
dealerCard = []
playerScore = 0
dealerScore = 0
isBlackJack = False
isFreshStart = True
Start = ''
drawMore = ''

def draw_card(user_card):
    card = random.choice(list(cards.keys()))
    user_card.append(card)

def calculate_score(user_card):
    score = sum(cards[c] for c in user_card)
    if 'A' in user_card and score > 21:
        score -= (10 * user_card.count('A'))
    return score

def init_display(player_card,dealer_card):
    print('Your card : ')
    for card in player_card: print(card)
    print(f'Your score : {calculate_score(playerCard)}',end = '\n' * 2)
    print(f'Dealer first card : {dealer_card[0]}')

def final_display():
    print("Your final cards: ")
    for card in playerCard:
        print(card)
    print(f'You final score : {playerScore}')
    print("Dealer's final cards: ")
    for card in dealerCard:
        print(card)
    print(f'Dealer final score : {dealerScore}')

def black_jack(player_card,dealer_card):
    if calculate_score(dealer_card) == 21:
        final_display()
        print("You Lost.")
        print('Dealer got BlackJack.')
        return True
    if calculate_score(player_card) == 21 and calculate_score(dealer_card) != 21:
        final_display()
        print("You Win.")
        print('You got BlackJack.')
        return True
    return False

def compare(player_score,dealer_score):
    if player_score > 21:
        print('You lost.')
        print('Your score go over 21.')
    if player_score == 21:
        print("You Win.")
        print('You got BlackJack.')
    if player_score < 21 < dealer_score:
        print("You Win.")
        print('Dealer goes over 21')
    if player_score < dealer_score < 21:
        print("You lost.")
        print('You score less than dealer')
    if dealer_score < player_score < 21:
        print("You Win.")
        print('You score greater than dealer')
    if player_score != 21 and dealerScore == 21:
        print("You lost.")
        print('dealer got black jack')
    if player_score == dealerScore:
        print('Draw')

#game start
while True:
    playerCard.clear()
    dealerCard.clear()
    if isFreshStart:
        Start = input('Are you ready to play? (y/n) : ')
    else: Start = input('Do you want to play again? (y/n) : ')
    if Start == 'y' or 'n':
        if Start == 'y':
            isFreshStart = False
            for _ in range(2):
                draw_card(playerCard)
                draw_card(dealerCard)
            isBlackJack = black_jack(playerCard, dealerCard)
            if not isBlackJack:
                init_display(playerCard, dealerCard)
                while calculate_score(dealerCard) < 17:
                    draw_card(dealerCard)
                while True:
                    playerScore = calculate_score(playerCard)
                    dealerScore = calculate_score(dealerCard)
                    if playerScore > 21 or playerScore == 21 or dealerScore == 21 : break
                    drawMore = input('Do you want to draw more card? (y/n) : ').lower()
                    if drawMore == 'y' or 'n':
                        if drawMore == 'y':
                            draw_card(playerCard)
                            init_display(playerCard,dealerCard)
                        if drawMore == 'n':
                            break
                final_display()
                compare(playerScore,dealerScore)
        if Start == 'n':
            break


