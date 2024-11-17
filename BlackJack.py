import random

cards = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
playerCard = []
dealerCard = []
playerScore = 0
dealerScore = 0
revealDealer = True
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

def final_display(reveal_dealer):
    print("Your final cards: ")
    for card in playerCard:
        print(card)
    print(f'You final score : {playerScore}')
    if reveal_dealer:
        print("Dealer's final cards: ")
        for card in dealerCard:
            print(card)
        print(f'Dealer final score : {dealerScore}')

def compare(player_score,dealer_score):
    if dealer_score == 21 and isFreshStart:
        print('dealer got black jack, You lost.')
    if player_score > 21:
        print('Bust! You lost.')
    if player_score == 21:
        print("BlackJack! You Win.")
    if player_score < 21 < dealer_score:
        print("You Win! Dealer goes over 21")
    if player_score < dealer_score < 21:
        print("You lost.")
    if dealer_score < player_score < 21:
        print("You Win.")
    if player_score != 21 and dealerScore == 21:
        print("You lost! dealer got black jack.")
    if player_score == dealerScore:
        print("It's a Draw")

#game start 
while True:
    playerCard.clear()
    dealerCard.clear()

    if isFreshStart:
        Start = input('Are you ready to play? (y/n) : ')
    else:
        Start = input('Do you want to play again? (y/n) : ')
    if Start not in ('y', 'n'): continue
    if Start == 'y':
        isFreshStart = False
        for _ in range(2):
            draw_card(playerCard)
            draw_card(dealerCard)
        dealerScore = calculate_score(dealerCard)
        playerScore = calculate_score(playerCard)
        if playerScore == 21 or dealerScore == 21:
            final_display(revealDealer)
            compare(playerScore,dealerScore)
            continue
        while dealerScore < 17:
            draw_card(dealerCard)
            dealerScore = calculate_score(dealerCard)
        while playerScore < 21:
            init_display(playerCard, dealerCard)
            drawMore = input("Type 'y' to get another card 'n' to stop : ").lower()
            if drawMore not in ('y', 'n'): continue
            if drawMore == 'y':
                draw_card(playerCard)
                print("===================", end='\n' * 2)
            if drawMore == 'n': break
            playerScore = calculate_score(playerCard)
        revealDealer = True
        if dealerScore > 21 and playerScore > 21: revealDealer = False
    final_display(revealDealer)
    compare(playerScore, dealerScore)
    if Start == 'n':
        print('Exit...')
        break


