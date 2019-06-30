import numpy as np


class Agent:

    def __init__(self):
        self.N = np.zeros(shape=(22, 11, 2))
        self.Q = np.zeros(shape=(22, 11, 2))
        self.V = np.zeros([22, 11])

    def train(self):
        pass

    def get_value_function(self):

        for i in range(22):
            for j in range(11):
                self.V[i][j] = max(self.Q[i][j])
        return self.V

    def control(self, episode):
        pass
