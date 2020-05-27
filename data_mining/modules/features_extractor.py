import pandas as pd
import ta

stonks = pd.read_csv('stocks.csv')
stonks.PREABE

indicator_bb = ta.volatility.BollingerBands(close=stonks['PREABE'], n=20, ndev=2)

bb_bbm = indicator_bb.bollinger_mavg()
bb_bbh = indicator_bb.bollinger_hband()
bb_bbl = indicator_bb.bollinger_lband()
