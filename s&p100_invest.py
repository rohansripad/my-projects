#pip install iexfinance
import pandas as pd
from iexfinance import get_historical_data
from datetime import datetime

pd.options.display.max_rows = 200

sp100 = ['AAPL', 'ABBV', 'ABT', 'ACN', 'AGN', 'AIG', 'ALL', 'AMGN', 'AMZN', 'AXP', 'BA', 'BAC', 'BIIB', 'BK', 'BKNG', 'BLK', 'BMY', 'BRK.B', 'C', 'CAT', 'CELG', 'CHTR', 'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CSCO', 'CVS', 'CVX', 'DHR', 'DIS', 'DUK', 'DWDP', 'EMR', 'EXC', 'F', 'FB', 'FDX', 'FOX', 'FOXA', 'GD', 'GE', 'GILD', 'GM', 'GOOG', 'GOOGL', 'GS', 'HAL', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KHC', 'KMI', 'KO', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MDT', 'MET', 'MMM', 'MO', 'MRK', 'MS', 'MSFT', 'NEE', 'NFLX', 'NKE', 'NVDA', 'ORCL', 'OXY', 'PEP', 'PFE', 'PG', 'PM', 'PYPL', 'QCOM', 'RTN', 'SBUX', 'SLB', 'SO', 'SPG', 'T', 'TGT', 'TXN', 'UNH', 'UNP', 'UPS', 'USB', 'UTX', 'V', 'VZ', 'WBA', 'WFC', 'WMT', 'XOM']

start = datetime(2018, 4, 5)
end = datetime(2018, 10, 5)

data = pd.DataFrame(columns = ['Stock','%','Time-Period High','Cur. Price','Diff'])
for stock in sp100:
    df = get_historical_data(stock, start=start, end=end, output_format='pandas')
    price = Stock(stock).get_close()
    high = max(df['close'])
    perc = (high-price)/high
    data = data.append({'Stock':stock, '%':round(perc*100,1),'Time-Period High':round(high,2),'Cur. Price':round(price,2),'Diff': round(perc*high,2)},ignore_index=True)
data.sort_values(by = '%', ascending = 0)
