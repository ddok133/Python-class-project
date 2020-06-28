import pandas as pd
import matplotlib.pyplot as plt

#人口分析
df = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 現住人口數按性別及原住民身分分（新增區域代碼）.csv' ,encoding = 'utf-8-sig')
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
    gsite['Birth'][i]=int(gsiteb['Birth'][i])

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
    gsite['Marry'][i]=int(gsitem['Marry'][i])
    
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
    gsite['Death'][i]=int(gsited['Death'][i])

#依照總人口排序
gsite=gsite.sort_values('Population',ascending=False)
#取TOP10
gsite=(gsite.head(10))

print(gsite)



#設定中文字體輸出
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
plt.rcParams['font.serif'] = ['Taipei Sans TC Beta']
plt.rcParams['axes.unicode_minus'] = False

# #繪圖輸出
gsite.plot(kind='bar',rot=45,stacked=False)
plt.title('TOP10 總人口排序', size=25)
plt.xlabel('City',size=20)
plt.ylabel('Population',size=20)
# for x,y in enumerate(gsite):plt.text(x,y,'%s'%y,ha='center',size=8)
plt.show()

# =============================================================================
# =============================================================================
# fig, ax1 = plt.subplots() 
# fig.suptitle('分析') # 標題
# ax1.set_ylabel('Population') # 設定y軸標題文字
# ax1.set_xlabel('City') # 設定x軸標題文字
# 
# ax2 = ax1.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('相對人口')
# gsite['birth'].plot(ax=ax1,style='p',rot=45) # rot：旋轉座標刻度
# gsite['death'].plot(ax=ax2,style='g') # style : 顏色
# ax1.legend(loc=1) # loc =1  左上
# ax2.legend(loc=2) # loc =2  右上
# 
# plt.show()
# # 
# =============================================================================
# =============================================================================
