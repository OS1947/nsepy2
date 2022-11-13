from nsepy import get_history
from datetime import date
import matplotlib as plt

data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
data[['Close']].plot()