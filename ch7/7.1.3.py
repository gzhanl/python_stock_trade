import baostock as bs
import pandas as pd

# 参数设置
pd.set_option('display.expand_frame_repr',False) # False不允许换行
pd.set_option('display.max_rows', 10) # 显示的最大行数
pd.set_option('display.max_columns', 6) # 显示的最大列数
pd.set_option('precision', 2) # 显示小数点后的位数

#lg=bs.login(user_id='anonymous', password='123456', options=0)
lg=bs.login()

fields= "date,open,high,low,close,volume"
df_bs=bs.query_history_k_data("sh.000001",fields,start_date='2020-01-01',end_date='2020-06-01')


# print(df_bs)  #    接口返回的是可迭代對象  <baostock.data.resultset.ResultData object at 0x00000202A80E9780>

data_list=[ ]  # create list for append data

while (df_bs.error_code == '0') & df_bs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(df_bs.get_row_data())

# columns=df_bs.fields  -->> ['date', 'open', 'high', 'low', 'close', 'volume']
result = pd.DataFrame(data_list, columns=df_bs.fields)
result.index = pd.to_datetime(result.date)
result.open = result.open.astype('float64')
result.high = result.high.astype('float64')
result.low = result.low.astype('float64')
result.close = result.close.astype('float64')
#result.volume = result.volume.astype('int')    # 因太大不能轉爲int


print(result.head())

print(result.info())

bs.logout()
