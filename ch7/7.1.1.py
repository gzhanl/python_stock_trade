import pandas_datareader.data as web

import datetime

df_stockload= web.DataReader("000001.SS", "yahoo",datetime.datetime(2009,1,1),datetime.datetime(2019,6,1))

print(df_stockload.head())

print(df_stockload.tail())