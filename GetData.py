from yahoo_fin import *
import yfinance as yf 
import yahoo_fin as y_f
import pandas as pd
from yahoo_fin import stock_info as si
import numpy as np

industry_ticker = {
    "Basic Materials": ['BHP','LIN','RIO','CTA-PB','APD','VALE','SCCO','SHW'],
    "HealthCare": ['JNJ', 'UNH', 'NVO', 'LLY', 'MRK', 'ABBV', 'AZN', 'PFE'],
    "Energy": ['XOM','CVX','SHEL','TTE','COP','BP','EQNR','ENB'],
    "Consumer Cyclical": ['AMZN','TSLA','HD','BABA','MCD','NKE','TM','LOW'],
    "Communication Services": ['GOOG','GOOGL','META','DIS','TMUS','CMCSA','VZ','NFLX']
}

# def get_company_info(ticker):
#     company_info = yf.Ticker(ticker)
#     print(company_info.info['industry'])

# get_company_info("AAPL")

# msft = yf.Ticker("aapl")
# msft.info
# print(msft.info)

def get_company_info(ticker, attribute):
    com_info = yf.Ticker(ticker)
    if attribute == 'all':
        result = com_info.info
    else:
        result = com_info.info[attribute]
    print(result)
    return result

def get_industry_by_ticker(ticker):
    for x in industry_ticker:
        for tick in industry_ticker[x]:
            if tick == ticker:
                return industry_ticker[x]
    return None

def get_ticker_hst(ticker, period):
    """period Value = 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y"""
    com = yf.Ticker(ticker)
    # dataframe = com.history(period="1mo")
    # print(dataframe) # period Value = 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y
    # url = f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}"
    # headers = {'User-agent': 'Mozilla/5.0'}
    # comData = data.TickerData(ticker)
    # response = comData.get(url)
    # print(response)
    df = com.history(period=period)
    df.index = df.index.date
    df.index.name = 'Date'
    df = df.drop(labels=['Dividends', 'Stock Splits'], axis=1)
    df['Adj Close'] = 0
    name = ticker + '_hst.csv'
    df.to_csv(f'E:\HCMUT\Data Warehouse\Stock\-HCMUT-HK222-DW\csv\{name}', index = True, header = True)
    return df

def get_earnings_history(ticker):
    url = 'https://finance.yahoo.com/calendar/earnings?symbol=' + ticker
    headers = {'User-agent': 'Mozilla/5.0'}

    table = pd.read_html(requests.get(url, headers=headers).text)
    name = ticker + '_eps.csv'
    df = table[0]
    df = df.drop('Reported EPS', axis=1)
    df = df.drop('Surprise(%)', axis=1)
    df = df.replace('-', np.nan)
    df = df.dropna()
    for ind in df.index:
        df['Earnings Date'][ind] = df['Earnings Date'][ind][0:12]
        df['Earnings Date'][ind] = pd.to_datetime(df['Earnings Date'][ind])
        print(df['Earnings Date'][ind])
    df.to_csv(f'E:\HCMUT\Data Warehouse\Stock\-HCMUT-HK222-DW\csv\{name}', index = True, header = True)
    return df

# get_company_info('aapl', 'industry')
# get_ticker_hst('aapl', "1mo")
# get_earnings_history('aapl')
a = get_industry_by_ticker('GOOG')
print(a)
print(a[0])
get_company_info(a[0], 'sector')