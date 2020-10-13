import json
import tushare as ts
token='67bcc08d60c4287441a1a80dd58701c5fd2d2c916bbf6758bb9cc05d'
pro=ts.pro_api(token)

index = {'上证综指': 'sh.000001',
         '深证成指': 'sz.399001',
         '沪深300': 'sz.000300',
         '创业板指': 'sz.399006',
         '上证50': 'sh.000016',
         '中证500': 'sh.000905',
         '中小板指': 'sz.399005',
         '上证180': 'sh.000010'}

df = pro.stock_basic(exchange='', list_status='L')
# print(df.head())
print(df.head())

codes=df.ts_code.values
names = df.name.values
stock = dict(zip(names, codes))  # 將 name 設爲鍵， codes 設爲 值
#print(stock)


stock_index = {'上证综指': 'sh.000001',
                     '深证成指': 'sz.399001',
                     '沪深300': 'sz.000300',
                     '创业板指': 'sz.399006',
                     '上证50': 'sh.000016',
                     '中证500': 'sh.000905',
                     '中小板指': 'sz.399005',
                     '上证180': 'sh.000010'}

stock_index = dict([('指数', index), ('股票', stock)])
#print(stock_index)
# dump: 将数据写入json文件中
with open("stock_pool.json", "w", encoding='utf-8') as json_f:
        json.dump(stock_index, json_f, ensure_ascii=False, indent=4)