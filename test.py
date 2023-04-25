import yfinance as yf
import pandas as pd

def get_company_info(ticker, attribute):
    com_info = yf.Ticker(ticker)
    if attribute == 'all':
        result = com_info.info
    else:
        result = com_info.info[attribute]
    return result

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
    df.index.labels = 'Date'
    df.index.name = 'Date'
    df = df.drop(labels=['Dividends', 'Stock Splits'], axis=1)
    df['Adj Close'] = 0
    print(df)
    return df
    # name = ticker + '_hst.csv'
    # df.to_csv(f'E:\HCMUT\Data Warehouse\Stock\-HCMUT-HK222-DW\csv\{name}', index = True, header = True)

get_ticker_hst('aapl', '1mo')