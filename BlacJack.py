import random

cards = {'A':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
playerCard = []
dealerCard = []
playerScore = 0
dealer_score = 0

def random_card(draw):
    for i in range(draw):
        playerCard.append(random.choice(list(cards.keys())))

def pre_score(card_lst):
    pre_sc = 0
    for i in card_lst: pre_sc += cards[i]
    return pre_sc

def actual_score(pre_sc,items):
    act_score = 0
    for i in items: act_score += cards[i]
    if 'A' in items and pre_sc > 21: act_score -= (10 * items.count('A'))
    print(f'Item count {items.count("A")}')  #--
    print(f'Actual score : {act_score}')  #--
    return act_score

def dealer_card(dealer_sc):
    while dealer_sc < 17:
        dealerCard.append(random.choice(list(cards.keys())))
        dealer_sc = pre_score(dealerCard)
    print(f'Dealer score: {dealer_sc}')  #--
    return dealer_sc


random_card(2)
dealer_score = dealer_card(dealer_score)
actual_score(dealer_score,dealerCard)
print(playerCard)
print(dealerCard)



print('gfsfhsfsfsdsgs')