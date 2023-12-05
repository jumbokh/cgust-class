#RC_7_5: 計算技術指標- 相對強弱指標RSI
import yfinance as yf
import pandas as pd
import datetime

yf.pdr_override() # <== that's all it takes :-)
start=datetime.datetime(2013,1,1)
end=datetime.datetime(2015,12,31)
df1 = yf.download('2379.tw',start,end)

roi=df1[df1.columns[0]].pct_change()

def rsi(n,roi):
	rsiv=[]
	for i in range (n, roi.count()):
		ups=0
		downs=0
		u=0
		d=0
		ud=0
		for j in range(i-n+1,i+1):
			if roi[j]>=0.00000000:
				u=u+roi[j]
			else:
				d=d+roi[j]
		if u == 0:
			u = 0.00000001
		if d == 0 :
			d = 0.00000001
		ups=u/n
		downs=abs(d/n)
		ud=ups/downs
		rsiv.append(abs(100-(100/(1+ud))))
	return rsiv

for n in range(5, 11, 5):
	rsi_data=[]
	rsi_data=rsi(n,roi)#呼叫rsi自訂函數
	Colname='rsi'+str(n)
	df2=pd.DataFrame(columns=[Colname],index=df1.index)
	for i in range(n,len(df1.index)-1):
		df2['rsi'+str(n)][i+1]=rsi_data.pop(0)
	df1=pd.concat([df1,df2],axis=1)
    
df1.to_excel('file/2379.xlsx','2379')

