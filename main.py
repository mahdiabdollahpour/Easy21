import RL
import plot
from MonteCarloControl import MonteCarloControl

# ss = RL.Q_learning(1800000, 0.6)
mcc = MonteCarloControl(500000, 0.4, 1, 100)
ss = mcc.train()
plot.surface_plot(ss)
