import pandas as pd
from GetData import get_ticker_hst, get_earnings_history
from CalGrowth import calGrowth
from Global import *

ticket = 'goog'
get_ticker_hst(ticket, PERIOD)

df = get_earnings_history(ticket)
growth = calGrowth(df)
data = [growth]
dfGrowth = pd.DataFrame(data, columns = ['Recomended Growth'])
print(dfGrowth)
name = 'FinalGrowth.csv'
dfGrowth.to_csv(DIR + f'{name}', index = False, header = True)