#RC_7_3: 上網抓資料並畫K線圖
#需要pip install mpl_finance
import matplotlib.pyplot as plt
import matplotlib.dates as dts
import yfinance as yf
import mplfinance as fplt
import datetime


#下載資料起迄日, 日期格式與股票代號
start = datetime.datetime(2016,4,1)
end = datetime.datetime(2016,4,25)

#以pandas_datareader的get_data_yahoo抓取資料
ohlc = yf.download('AAPL',start,end)
ohlc = ohlc.loc[:, ["Open", "High", "Low", "Close", "Volume"]]

# 設定圖標的顏色
mc = fplt.make_marketcolors(
     up='tab:red',down='tab:green',
     wick={'up':'red','down':'green'},
     volume='tab:green',
    )
s  = fplt.make_mpf_style(marketcolors=mc)

# 繪製K線圖
fplt.plot(
        ohlc,
        type = 'candle',
        style = s,
        title = 'AAPL',
        ylabel = 'Price ($)', 
        volume = True,
        #savefig='stock_Kbar.png',  # 存檔
    )

#畫K線圖並顯示
plt.show()