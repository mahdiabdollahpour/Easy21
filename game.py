cards = []
cards += range(1, 11)
cards += range(-10, 0)
cards += range(1, 11)
import numpy as np
np.random.shuffle(cards)
# cards += range(-10, 0)
print(cards)
import random


def get_rand_card():
    rnd_idx = random.randint(0, len(cards) - 1)
    # print(len(cards),rnd_idx)
    card = cards[rnd_idx]
    # del cards[rnd_idx]
    return card


dealer_sum = 0
def init():
    global dealer_sum
    dealer_sum = abs(get_rand_card())
    s = [abs(get_rand_card()), dealer_sum]
    # print(s)
    return s


def step(s, a):
    global dealer_sum
    player_sum = s[0]
    # dealer_sum = s[1]
    if a == 1:  ## take another card

        player_sum += get_rand_card()
        if player_sum > 21 or player_sum < 1:
            return -1, [player_sum, s[1]]

        # if dealer_sum <= 17:
        #     dealer_sum += get_rand_card()
        #     if dealer_sum > 21 or dealer_sum < 1:
        #         return +1, [player_sum, s[1]]

        return 0, [player_sum, s[1]]

    if a == 0:  ## stick
        while dealer_sum <= 17:
            # print('q')
            dealer_sum += get_rand_card()
            if dealer_sum > 21 or dealer_sum < 1:
                return +1, [player_sum, s[1]]

        if dealer_sum > player_sum:
            return -1, [player_sum, s[1]]
        elif dealer_sum < player_sum:
            return +1, [player_sum, s[1]]
        else:
            return 0, [player_sum, s[1]]
