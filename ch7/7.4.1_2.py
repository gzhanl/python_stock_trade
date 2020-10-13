import json

stock_index = [{'指数':
                    {'上证综指': 'sh.000001',
                     '深证成指': 'sz.399001',
                     '沪深300': 'sz.000300',
                     '创业板指': 'sz.399006',
                     '上证50': 'sh.000016',
                     '中证500': 'sh.000905',
                     '中小板指': 'sz.399005',
                     '上证180': 'sh.000010'}},
               {'股票':
                    {'格力电器': '000651.SZ',
                     '平安银行': '000001.SZ',
                     '同花顺': '300033.SZ',
                     '贵州茅台': '600519.SH',
                     '浙大网新': '600797.SH'}}]

json_str=json.dumps(stock_index)

print(json_str)

# dump: 将数据写入json文件中
with open("stock_pool.json", "w", encoding='utf-8') as json_f:
        json.dump(stock_index, json_f, ensure_ascii=False, indent=4)
