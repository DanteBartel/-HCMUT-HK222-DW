import pandas as pd
from GetData import get_ticker_hst, get_earnings_history
from CalGrowth import calGrowth
from Global import *

get_ticker_hst(INPUTTICKER, PERIOD)

df = get_earnings_history(INPUTTICKER)
growth = calGrowth(df)
data = [growth]
dfGrowth = pd.DataFrame(data, columns = ['Recomended Growth'])
print(dfGrowth)
name = INPUTTICKER + '_growth.csv'
dfGrowth.to_csv(DIR + f'{name}', index = False, header = True)