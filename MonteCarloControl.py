import random
from Agent import Agent
import numpy as np
import game


class MonteCarloControl(Agent):

    def __init__(self, episodes, df, No):
        super(MonteCarloControl, self).__init__()
        self.No = No
        self.df = df
        self.episodes = episodes
        # self.w = w

    def get_alpha(self, s, a):
        return 1.0 / (self.N[s[0]][s[1]][a])

    def get_e(self, s):

        return self.No / ((self.No + sum(self.N[s[0], s[1], :]) * 1.0))

    def policy(self, epsilon, vec):
        rnd = random.random()
        if rnd > epsilon:
            return self.optimal_policy(vec)
        else:
            return np.random.randint(0, 2)

    def optimal_policy(self, vec):
        return np.argmax(vec)

    def control(self, episode):
        j = 0
        for s, a, _ in episode:
            ps = s[0]
            ds = s[1]

            Gt = sum([x[2] * (self.df ** i) for i, x in enumerate(episode[j:])])

            self.N[ps][ds][a] += 1

            error = Gt - self.Q[ps][ds][a]
            self.Q[ps][ds][a] += self.get_alpha(s, a) * error

            j += 1

    def train(self):
        for i in range(self.episodes):
            print("==============", i, "==============")
            episode = []
            s = game.init()

            ps = s[0]
            ds = s[1]

            r = 0
            while r == 0:
                a = self.policy(self.get_e(s), self.Q[ps, ds])
                # print(a)
                r, s = game.step([ps, ds], a)
                # print("r",r,a,ps,ds)
                episode.append([[ps, ds], a, r])
                if a == 0:
                    # print(r)
                    break
                else:
                    ps = s[0]
                    ds = s[1]

            self.control(episode)

        return self.Q
