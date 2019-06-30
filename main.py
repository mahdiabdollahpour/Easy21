import QL
import plot
from MonteCarloControl import MonteCarloControl


mcc = MonteCarloControl(1000000, df=1, No=100)
mcc.train()
plot.surface_plot(mcc.get_value_function())
