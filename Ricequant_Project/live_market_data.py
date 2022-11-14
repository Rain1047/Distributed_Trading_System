import rqdatac
from rqdatac import LiveMarketDataClient


rqdatac.init(username="license", password="tcp://license:PyTsyYnRPp5-b1EIW7lJ9dubDgSZRXBMjp4Mvumv-hRjYoiwt0RJyPFy8kZ2T6YmXfd5dMTiL7PJTrevDF2sipfewhaTDu5xY-yBd9QePbnQtzrr7iLL0AVNu6GKf6dl6qEBBjSk8OKckgIFrF54uj0V8SssOg27cKNDNTwj_Wg=gWaQAVkjkcs_sdVM7K4cDiMqYdsQlHrwx52Bnj9kI5gSF2diLSdRmHui8MUysGdfq3g_4JHEEM7EMW9fmT4eJd3nW69CMYI3vD9vD__px4UhA2dMyLnV2W6aSTtGl4If71_uStkVjhjqU9lfrcuJIQ055Jqhv1YmT0G0YRceAg8=@rqdatad-pro.ricequant.com:16011")
client = LiveMarketDataClient()
# 订阅一支tick标的
client.subscribe('tick_000001.XSHE')
# 订阅1分钟行情
client.subscribe('bar_000001.XSHE')
# 订阅多支tick标的
client.subscribe(['tick_000001.XSHE', 'tick_000002.XSHE'])

# 订阅3分钟行情，其它分钟线的命名方法类似，修改后缀即可
# client.subscribe('bar_000001.XSHE_3m')

# 取消订阅tick标的
client.unsubscribe('tick_000002.XSHE')

# 检听行情
# 1. 阻塞的方式
for market in client.listen():
    print(market)


# 2. 不阻塞的方式
def handle_msg(tick_or_bar):
    # 可以自行定义处理
    # queue.push(tick_or_bar)
    print(tick_or_bar)
client.listen(handler=handle_msg) # handler不为None


# [Out]
# {'datetime': 20210913094009000, 'order_book_id': '000001.XSHE', 'prev_close': 20.57, 'num_trades': 12786, 'volume': 13134791.0, 'total_turnover': 267427634, 'trading_phase_code': 'T', 'last': 20.26, 'open': 20.36, 'high': 20.51, 'low': 20.25, 'limit_up': 22.63, 'limit_down': 18.51, 'ask': [20.28, 20.3, 20.31, 20.32, 20.33], 'bid': [20.26, 20.25, 20.24, 20.23, 20.22], 'ask_vol': [37100.0, 33500.0, 13200.0, 16100.0, 3600.0], 'bid_vol': [4400.0, 198000.0, 6800.0, 17700.0, 33600.0], 'trading_date': 20210913, 'channel': 'tick_000001.XSHE', 'action': 'feed'}
# {'datetime': 20210913094012000, 'order_book_id': '000001.XSHE', 'prev_close': 20.57, 'num_trades': 12882, 'volume': 13278591.0, 'total_turnover': 270342631, 'trading_phase_code': 'T', 'last': 20.3, 'open': 20.36, 'high': 20.51, 'low': 20.25, 'limit_up': 22.63, 'limit_down': 18.51, 'ask': [20.3, 20.31, 20.32, 20.33, 20.34], 'bid': [20.28, 20.25, 20.24, 20.23, 20.22], 'ask_vol': [15000.0, 13200.0, 16100.0, 3600.0, 4500.0], 'bid_vol': [4400.0, 150000.0, 6800.0, 18500.0, 33600.0], 'trading_date': 20210913, 'channel': 'tick_000001.XSHE', 'action': 'feed'}
# {'datetime': 20210913094015000, 'order_book_id': '000001.XSHE', 'prev_close': 20.57, 'num_trades': 13014, 'volume': 13402691.0, 'total_turnover': 272859932, 'trading_phase_code': 'T', 'last': 20.26, 'open': 20.36, 'high': 20.51, 'low': 20.25, 'limit_up': 22.63, 'limit_down': 18.51, 'ask': [20.27, 20.29, 20.3, 20.32, 20.33], 'bid': [20.26, 20.25, 20.24, 20.23, 20.22], 'ask_vol': [3200.0, 2300.0, 3700.0, 1500.0, 3600.0], 'bid_vol': [500.0, 112400.0, 8000.0, 17700.0, 33600.0], 'trading_date': 20210913, 'channel': 'tick_000001.XSHE', 'action': 'feed'}
# {'datetime': 20210913094018000, 'order_book_id': '000001.XSHE', 'prev_close': 20.57, 'num_trades': 13110, 'volume': 13499491.0, 'total_turnover': 274820911, 'trading_phase_code': 'T', 'last': 20.28, 'open': 20.36, 'high': 20.51, 'low': 20.25, 'limit_up': 22.63, 'limit_down': 18.51, 'ask': [20.28, 20.29, 20.3, 20.32, 20.33], 'bid': [20.25, 20.24, 20.23, 20.22, 20.21], 'ask_vol': [9100.0, 6100.0, 4800.0, 1500.0, 2600.0], 'bid_vol': [52800.0, 8000.0, 17700.0, 33600.0, 165600.0], 'trading_date': 20210913, 'channel': 'tick_000001.XSHE', 'action': 'feed'}

