import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as dr
import datetime
import seaborn

end_date=datetime.datetime.now()
start_date=end_date-datetime.timedelta(days=365)

data=dr.get_data_google('AMD',start=start_date,end=end_date)

print(data.head())