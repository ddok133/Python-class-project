import pandas as pd
import matplotlib.pyplot as plt

#人口分析
df=pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 現住人口數按性別及原住民身分分（新增區域代碼）.csv' ,encoding = 'utf-8-sig')
#df轉dict，以縣市為單位彙整資料
dictp=dict()
for i in range(len(df)):
    if df['site_id'][i][0:3] not in dictp:
        dictp[df['site_id'][i][0:3]]=df['people_total'][i]    
    else:
        dictp[df['site_id'][i][0:3]]=dictp[df['site_id'][i][0:3]]+df['people_total'][i]
#dict轉Series
gsite=pd.Series(dictp)
gsite=pd.DataFrame(gsite,columns=['Population'])
gsite=pd.DataFrame(gsite,columns=['Population','Marry','Birth','Death'])

#生育分析
df = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 嬰兒出生數按性別、生母單一年齡分(按登記).csv' ,encoding = 'utf-8-sig')
df['site_id'] = df['site_id'].astype(str)
#df轉dict，以縣市為單位彙整資料
dictb=dict()
for i in range(len(df)):
    if df['site_id'][i][0:3] not in dictb:
        dictb[df['site_id'][i][0:3]]=df['birth_count'][i]      
    else:
        dictb[df['site_id'][i][0:3]]=dictb[df['site_id'][i][0:3]]+df['birth_count'][i]
#dict轉Series
gsiteb=pd.Series(dictb)
gsiteb=pd.DataFrame(gsiteb,columns=['Birth'])
for i in range(len(gsiteb)):
    gsite['Birth'][i]=(gsiteb['Birth'][i])

#結婚分析
df = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 結婚對數按男女雙方年齡分(按登記).csv' ,encoding = 'utf-8-sig')
df['site_id'] = df['site_id'].astype(str)

#df轉dict，以縣市為單位彙整資料
dictm=dict()
for i in range(len(df)):
    if df['site_id'][i][0:3] not in dictm:
        dictm[df['site_id'][i][0:3]]=df['marry_pair'][i]       
    else:
        dictm[df['site_id'][i][0:3]]=dictm[df['site_id'][i][0:3]]+df['marry_pair'][i]
#dict轉Series
gsitem=pd.Series(dictm)
gsitem=pd.DataFrame(gsitem,columns=['Marry'])
for i in range(len(gsitem)):
    gsite['Marry'][i]=(gsitem['Marry'][i])
    
#死亡分析
df = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 人口死亡數按死亡者性別及死亡地點分（按登記）.csv' ,encoding = 'utf-8-sig')
df['site_id'] = df['site_id'].astype(str)

#df轉dict，以縣市為單位彙整資料
dictd=dict()
for i in range(len(df)):
    if df['site_id'][i][0:3] not in dictd:
        dictd[df['site_id'][i][0:3]]=df['population'][i]          
    else:
        dictd[df['site_id'][i][0:3]]=dictd[df['site_id'][i][0:3]]+df['population'][i]

#dict轉Series
gsited=pd.Series(dictd)
gsited=pd.DataFrame(gsited,columns=['Death'])
for i in range(len(gsited)):
    gsite['Death'][i]=(gsited['Death'][i])
   
#轉int
gsite['Marry']=gsite['Marry'].astype(int)
gsite['Birth']=gsite['Birth'].astype(int)
gsite['Death']=gsite['Death'].astype(int)

#依照總人口排序
gsitesp=gsite.sort_values('Population',ascending=False)

#取TOP10
gsitesptop10=(gsitesp.head(10))

#設定中文字體輸出
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
plt.rcParams['font.serif'] = ['Taipei Sans TC Beta']
plt.rcParams['axes.unicode_minus'] = False


#繪圖輸出
fig,ax = plt.subplots() 
fig.suptitle('Analysis',size=25)
ax.set_ylabel('Population',size=20)
ax.set_xlabel('City',size=20)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
ax2.set_ylabel('Rela-Population',size=20)

gsitesptop10['Population'].plot(kind='bar',ax=ax,rot=45)
gsitesptop10['Marry'].plot(ax=ax2,style='r')
gsitesptop10['Birth'].plot(ax=ax2,style='c')
gsitesptop10['Death'].plot(ax=ax2,style='k')
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()

#繪圖輸出
gsitesptop10.plot(kind='bar',rot=45)
plt.title('TOP10 Residents', size=25)
plt.xlabel('City',size=20)
plt.ylabel('Population',size=20)
plt.show()



print(gsite.info())
print('-------------------------')
print(gsitesptop10)
print('-------------------------')

#取人口總和
sum1=0
for j in range(len(gsitesp)):
    sum1 += gsitesp['Population'][j]
print('全台總人口 :',sum1,'人')    

#TOP10總和
sum2=0
for j in range(len(gsitesptop10)):
    sum2 += gsitesptop10['Population'][j]    
print('TOP10 城市人口總和 :',sum2,'人')
#TOP10 vs 全台佔比
rate=sum2/sum1*100
print('TOP10 城市佔全台人口比例 : %2.2f' % rate ,'%' )


