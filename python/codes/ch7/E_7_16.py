#E_7_16: 上網路抓取多家股價資料
from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
import datetime
import time
starttime = time.process_time()
#下載資料起始日與股票代號
yf.pdr_override() # <== that's all it takes :-)
start = datetime.datetime(2016,1,1)
end = datetime.datetime(2018,3,1)
stockid=('2303', '2330', '3008', '2498', '2409', '2357', '2317')
writer=pd.ExcelWriter('./file/stocprice_revised.xlsx')
print(type(stockid))
for i in range(0,len(stockid)):
    sid=stockid[i]+'.tw'
    try:
        df = pdr.get_data_yahoo(sid, start, end)
    except:
        print(stockid[i] +"出錯")
        continue
    df.to_excel(writer,stockid[i])
writer.save()
endtime = time.process_time()
print(' 程式執行時間 = %d %s' %(round(endtime - starttime), ' 秒'))