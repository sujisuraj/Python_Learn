import numpy as np
import matplotlib.pyplot as plt
import seaborn


def put_payoff(sT,strike_price,premium):
    pnl=np.where(sT<strike_price,strike_price-sT,0)
    return pnl-premium

spot_price=900
strike_price=900
premium=20

sT=np.arange(0.9*spot_price,1.2*spot_price)

payoff_long_put=put_payoff(sT,strike_price,premium)

fig,ax=plt.subplots()
ax.spines['bottom'].set_position('zero')
ax.plot(sT,payoff_long_put,label='put option buyer payoff')
plt.xlabel('stock price')
plt.ylabel('Profit and Loss')
plt.legend()
plt.show()