from operator import index
import rqdatac
import pandas as pd

rqdatac.init()
# pdf = rqdatac.get_live_ticks(order_book_ids=['10002726'],start_dt='20210309094000',end_dt='20210309094002')
# pdf.to_csv('tick_data.csv',index=None)
# res:permission denied


pdf = rqdatac.get_price('000001.XSHE', start_date='20220321', end_date='20220321', frequency='tick',expect_df=False)
print(pdf)
pdf.to_csv('tick_data.csv',index=None)


pdf = rqdatac.get_price(['000001.XSHE', '000002.XSHE'], start_date='2022-11-02', end_date='2022-11-02',frequency='tick')
pdf.to_csv('./tick_data_multi.csv',index=None)