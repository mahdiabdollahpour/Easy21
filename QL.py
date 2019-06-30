import numpy as np
import random
import game


def policy(epsilon, vec):
    rnd = random.random()
    if rnd > epsilon:
        return optimal_policy(vec)
    else:
        return np.random.randint(0, 1)


def optimal_policy(vec):
    return np.argmax(vec)


def Q_learning(epidoes, w):
    # action_value = np.random.random(size=(22, 22,2))
    action_value = np.zeros(shape=(22, 11,2))
    for i in range(epidoes):
        print("==============", i, "==============")
        ps = random.randint(1, 11)
        ds = random.randint(1, 11)

        r = 0
        while r == 0:
            a = policy(0.5, action_value[ps, ds])
            # print(a)
            r, s = game.step([ps, ds], a)
            # print("r",r,a,ps,ds)
            if r == 0 and a != 0:
                action_value[ps, ds, a] = (1 - w) * action_value[ps, ds, a] + w * (
                        r + action_value[s[0], s[1], optimal_policy(action_value[s[0], s[1]])])
                ps = s[0]
                ds = s[1]
            else:
                print(r)
                action_value[ps, ds, a] = (1 - w) * action_value[ps, ds, a] + w * (r)
                ps = s[0]
                ds = s[1]
                break

    return action_value
