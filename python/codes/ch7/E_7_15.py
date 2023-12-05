#E_7_15: 上網路抓取股價資料
import yfinance as yf
import pandas as pd
import datetime
#下載資料起始日與股票代號
yf.pdr_override() # <== that's all it takes :-)
start = datetime.datetime(2016,1,1)
end = datetime.datetime(2018,3,1)
df = yf.download('2330.tw',start,end)
#日股價資料寫入excel檔
writer=pd.ExcelWriter('./file/2330.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()