import pandas as pd
import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
start=datetime.datetime(2012,1,1)
end=datetime.datetime(2015,1,1)
df=web.DataReader("XOM","yahoo",start,end)
print(df.head())
df['Adj Close'].plot()
plt.show()