# 分縣市排序TOP10 , for 迴圈 合併DF, 整合數據比對輸出
import pandas as pd
import matplotlib.pyplot as plt


#人口分析
dfp=pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 現住人口數按性別及原住民身分分（新增區域代碼）.csv' ,encoding = 'utf-8-sig')
dfp['site_id'] = dfp['site_id'].astype(str)
#df轉dict，以縣市為單位彙整資料
dictp=dict()
for i in range(len(dfp)):
    if dfp['site_id'][i][0:3] not in dictp:
        dictp[dfp['site_id'][i][0:3]]=dfp['people_total'][i]    
    else:
        dictp[dfp['site_id'][i][0:3]]=dictp[dfp['site_id'][i][0:3]]+dfp['people_total'][i]
#dict轉Series轉DataFrame
gsite=pd.Series(dictp)
gsite=pd.DataFrame(gsite,columns=['Population'])
gsite=pd.DataFrame(gsite,columns=['Population','Male','Female','Marry','Divorce','Marry %','Divorce %','Birth','Birth %','Birth_M','Birth_F','Death','Death_M','Death_F'])
# 人口男
dictpm=dict()
for i in range(len(dfp)):
    if dfp['site_id'][i][0:3] not in dictpm:
        dictpm[dfp['site_id'][i][0:3]]=dfp['people_total_m'][i]    
    else:
        dictpm[dfp['site_id'][i][0:3]]=dictpm[dfp['site_id'][i][0:3]]+dfp['people_total_m'][i]
#dict轉Series轉DataFrame
gsitem=pd.Series(dictpm)
gsitem=pd.DataFrame(gsitem,columns=['Male'])
for i in range(len(gsitem)):
    gsite['Male'][i]=(gsitem['Male'][i])
# 人口女
dictpf=dict()
for i in range(len(dfp)):
    if dfp['site_id'][i][0:3] not in dictpf:
        dictpf[dfp['site_id'][i][0:3]]=dfp['people_total_f'][i]    
    else:
        dictpf[dfp['site_id'][i][0:3]]=dictpf[dfp['site_id'][i][0:3]]+dfp['people_total_f'][i]
#dict轉Series轉DataFrame
gsitef=pd.Series(dictpf)
gsitef=pd.DataFrame(gsitef,columns=['Female'])
for i in range(len(gsitef)):
    gsite['Female'][i]=(gsitef['Female'][i])
 
# 結婚分析
dfm = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 結婚對數按男女雙方年齡分(按登記).csv' ,encoding = 'utf-8-sig')
dfm['site_id'] = dfm['site_id'].astype(str)
#df轉dict，以縣市為單位彙整資料
dictm=dict()
for i in range(len(dfm)):
    if dfm['site_id'][i][0:3] not in dictm:
        dictm[dfm['site_id'][i][0:3]]=dfm['marry_pair'][i]       
    else:
        dictm[dfm['site_id'][i][0:3]]=dictm[dfm['site_id'][i][0:3]]+dfm['marry_pair'][i]
#dict轉Series轉DataFrame
gsitem=pd.Series(dictm)
gsitem=pd.DataFrame(gsitem,columns=['Marry'])
for i in range(len(gsitem)):
    gsite['Marry'][i]=(gsitem['Marry'][i]*2)     
#離婚分析
dfdv = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 離婚人數按男女雙方年齡、原屬國籍（地區）及教育程度分.csv' ,encoding = 'utf-8-sig')
dfdv['site_id'] = dfdv['site_id'].astype(str)
#df轉dict，以縣市為單位彙整資料
dictdv=dict()
for i in range(len(dfdv)):
    if dfdv['site_id'][i][0:3] not in dictdv:
        dictdv[dfdv['site_id'][i][0:3]]=dfdv['divorce_count'][i]       
    else:
        dictdv[dfdv['site_id'][i][0:3]]=dictdv[dfdv['site_id'][i][0:3]]+dfdv['divorce_count'][i]
#dict轉Series轉DataFrame
gsitedv=pd.Series(dictdv)
gsitedv=pd.DataFrame(gsitedv,columns=['Divorce'])
for i in range(len(gsitedv)):
    gsite['Divorce'][i]=(gsitedv['Divorce'][i])    
   
#生育分析
dfb = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 嬰兒出生數按性別、生母單一年齡分(按登記).csv' ,encoding = 'utf-8-sig')
dfb['site_id'] = dfb['site_id'].astype(str)
#df轉dict，以縣市為單位彙整資料
dictb=dict()
for i in range(len(dfb)):
    if dfb['site_id'][i][0:3] not in dictb:
        dictb[dfb['site_id'][i][0:3]]=dfb['birth_count'][i]
    else:
        dictb[dfb['site_id'][i][0:3]]=dictb[dfb['site_id'][i][0:3]]+dfb['birth_count'][i]
#dict轉Series轉DataFrame
gsiteb=pd.Series(dictb)
gsiteb=pd.DataFrame(gsiteb,columns=['Birth'])
for i in range(len(gsiteb)):
    gsite['Birth'][i]=(gsiteb['Birth'][i])    
# 生育女    
for i in range(len(dfb)):
    if dfb['birth_sex'][i] == '男':
        dfb=dfb.drop([i],axis=0)        
dfb.to_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 嬰兒出生數按性別、生母單一年齡分(按登記)_dfbf.csv',encoding = 'utf-8-sig')
dfb = pd.read_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 嬰兒出生數按性別、生母單一年齡分(按登記)_dfbf.csv' ,encoding = 'utf-8-sig')
dfb['site_id'] = dfb['site_id'].astype(str)      
dictbf=dict()
for i in range(len(dfb)):
    if dfb['site_id'][i][0:3] not in dictbf:
        dictbf[dfb['site_id'][i][0:3]]=dfb['birth_count'][i]
    else:
        dictbf[dfb['site_id'][i][0:3]]=dictbf[dfb['site_id'][i][0:3]]+dfb['birth_count'][i]
#dict轉Series轉DataFrame
gsitebf=pd.Series(dictbf)
gsitebf=pd.DataFrame(gsitebf,columns=['Birth_F'])
for i in range(len(gsitebf)):
    gsite['Birth_F'][i]=(gsitebf['Birth_F'][i])
# 生育男
dfb = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 嬰兒出生數按性別、生母單一年齡分(按登記).csv' ,encoding = 'utf-8-sig')
dfb['site_id'] = dfb['site_id'].astype(str)
for i in range(len(dfb)):
    if dfb['birth_sex'][i] == '女':
        dfb=dfb.drop([i],axis=0)        
dfb.to_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 嬰兒出生數按性別、生母單一年齡分(按登記)_dfbm.csv',encoding = 'utf-8-sig')
dfb = pd.read_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 嬰兒出生數按性別、生母單一年齡分(按登記)_dfbm.csv' ,encoding = 'utf-8-sig')
dfb['site_id'] = dfb['site_id'].astype(str)      
dictbm=dict()
for i in range(len(dfb)):
    if dfb['site_id'][i][0:3] not in dictbm:
        dictbm[dfb['site_id'][i][0:3]]=dfb['birth_count'][i]
    else:
        dictbm[dfb['site_id'][i][0:3]]=dictbm[dfb['site_id'][i][0:3]]+dfb['birth_count'][i]
#dict轉Series轉DataFrame
gsitebm=pd.Series(dictbm)
gsitebm=pd.DataFrame(gsitebm,columns=['Birth_M'])
for i in range(len(gsitebm)):
    gsite['Birth_M'][i]=(gsitebm['Birth_M'][i])

#死亡分析
dfd = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 人口死亡數按死亡者性別及死亡地點分（按登記）.csv' ,encoding = 'utf-8-sig')
dfd['site_id'] = dfd['site_id'].astype(str)
#df轉dict，以縣市為單位彙整資料
dictd=dict()
for i in range(len(dfd)):
    if dfd['site_id'][i][0:3] not in dictd:
        dictd[dfd['site_id'][i][0:3]]=dfd['population'][i]          
    else:
        dictd[dfd['site_id'][i][0:3]]=dictd[dfd['site_id'][i][0:3]]+dfd['population'][i]
#dict轉Series轉DataFrame
gsited=pd.Series(dictd)
gsited=pd.DataFrame(gsited,columns=['Death'])
for i in range(len(gsited)):
    gsite['Death'][i]=(gsited['Death'][i])  
# 死亡女    
for i in range(len(dfd)):
    if dfd['sex'][i] == '男':
        dfd=dfd.drop([i],axis=0)       
dfd.to_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 人口死亡數按死亡者性別及死亡地點分（按登記）_dfdf.csv',encoding = 'utf-8-sig')
dfd = pd.read_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 人口死亡數按死亡者性別及死亡地點分（按登記）_dfdf.csv' ,encoding = 'utf-8-sig')
dfd['site_id'] = dfd['site_id'].astype(str)      
dictdf=dict()
for i in range(len(dfd)):
    if dfd['site_id'][i][0:3] not in dictdf:
        dictdf[dfd['site_id'][i][0:3]]=dfd['population'][i]
    else:
        dictdf[dfd['site_id'][i][0:3]]=dictdf[dfd['site_id'][i][0:3]]+dfd['population'][i]
#dict轉Series轉DataFrame
gsitedf=pd.Series(dictdf)
gsitedf=pd.DataFrame(gsitedf,columns=['Death_F'])
for i in range(len(gsitedf)):
    gsite['Death_F'][i]=(gsitedf['Death_F'][i])
# 死亡男
dfd = pd.read_csv('/Users/martychen/Documents/Python/Python Analysis Report/108 年度 人口死亡數按死亡者性別及死亡地點分（按登記）.csv' ,encoding = 'utf-8-sig')
dfd['site_id'] = dfd['site_id'].astype(str)
for i in range(len(dfd)):
    if dfd['sex'][i] == '女':
        dfd=dfd.drop([i],axis=0)      
dfd.to_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 人口死亡數按死亡者性別及死亡地點分（按登記）_dfdm.csv',encoding = 'utf-8-sig')
dfd = pd.read_csv(r'/Users/martychen/Documents/Python/Python Analysis Report/108 年度 人口死亡數按死亡者性別及死亡地點分（按登記）_dfdm.csv' ,encoding = 'utf-8-sig')
dfd['site_id'] = dfd['site_id'].astype(str)      
dictdm=dict()
for i in range(len(dfd)):
    if dfd['site_id'][i][0:3] not in dictdm:
        dictdm[dfd['site_id'][i][0:3]]=dfd['population'][i]
    else:
        dictdm[dfd['site_id'][i][0:3]]=dictdm[dfd['site_id'][i][0:3]]+dfd['population'][i]

#dict轉Series轉DataFrame
gsitedm=pd.Series(dictdm)
gsitedm=pd.DataFrame(gsitedm,columns=['Death_M'])
for i in range(len(gsitedm)):
    gsite['Death_M'][i]=(gsitedm['Death_M'][i])
    
gsite['Population']=gsite['Population'].astype(int) 
gsite['Male']=gsite['Male'].astype(int)   
gsite['Female']=gsite['Female'].astype(int)   
gsite['Marry']=gsite['Marry'].astype(int)   
gsite['Divorce']=gsite['Divorce'].astype(int)    
gsite['Birth']=gsite['Birth'].astype(int)   
gsite['Birth_M']=gsite['Birth_M'].astype(int) 
gsite['Birth_F']=gsite['Birth_F'].astype(int)   
gsite['Death']=gsite['Death'].astype(int)   
gsite['Death_M']=gsite['Death_M'].astype(int)
gsite['Death_F']=gsite['Death_F'].astype(int)  
    
# 離婚率
for i in range(len(gsite)):
    gsite['Divorce %'][i]= gsite['Divorce'][i]*500/ gsite['Population'][i]   
# 結婚率
for i in range(len(gsite)):
    gsite['Marry %'][i]= gsite['Marry'][i]*500 / gsite['Population'][i]

    
#依照總人口排序
gsitesp=gsite.sort_values('Population',ascending=False)
#取TOP10
gsitesptop10=(gsitesp.head(10))

 

#設定中文字體輸出
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
plt.rcParams['font.serif'] = ['Taipei Sans TC Beta']
plt.rcParams['axes.unicode_minus'] = False

# 總表
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Population'].plot(kind='bar',ax=ax,rot=45,figsize=(10,6))
gsitesptop10['Marry'].plot(ax=ax2,style='r')
gsitesptop10['Divorce'].plot(ax=ax2,style='g')
gsitesptop10['Birth'].plot(ax=ax2,style='c')
gsitesptop10['Death'].plot(ax=ax2,style='k')

ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()


# Marry vs Birth vs Death 繪圖輸出
plt.figure(dpi=240)
mbd=gsitesptop10[['Marry','Birth','Death']]
mbd.plot(kind='bar',rot=45,figsize=(10,6))
# plt.title('', size=25)
plt.xlabel('城市',size=12)
plt.ylabel('人口數',size=12)
plt.show()

# 結婚離婚人數繪圖輸出
plt.figure(dpi=240)
MDV=gsitesptop10[['Marry','Divorce']]
MDV.plot(kind='bar',rot=45,figsize=(10,6))
# plt.title('', size=25)
plt.xlabel('城市',size=12)
plt.ylabel('人口數',size=12)
plt.show()

# 結婚離婚率繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Population'].plot(kind='bar',style='c',ax=ax,figsize=(10,6))
MDVp=gsitesptop10[['Marry %','Divorce %']]
MDVp.plot(ax=ax2,rot=45)
ax2.legend(loc=2)
ax.legend(loc=1)
plt.show()


MDMD=gsitesptop10[['Marry','Marry %','Divorce','Divorce %']]
print(MDMD)

# 結婚離婚-比例繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸

gsitesptop10['Marry %'].plot(ax=ax2,style='r',figsize=(10,6))
gsitesptop10['Divorce %'].plot(ax=ax2,style='g')
MDV.plot(kind='bar',ax=ax,rot=12)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()


# 結婚離婚-生育繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸

gsitesptop10['Birth'].plot(ax=ax2,style='c',figsize=(10,6))
MDV.plot(kind='bar',ax=ax,rot=12)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()



# 男女比例繪圖輸出
plt.figure(dpi=240)
MF=gsitesptop10[['Male','Female']]
MF.plot(kind='bar',rot=45,figsize=(10,6))
# plt.title('', size=25)
plt.xlabel('城市',size=12)
plt.ylabel('人口數',size=12)
plt.show()

# 結婚-男女比例繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Marry'].plot(style='r',ax=ax2,figsize=(10,6))
MF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()

# 生育-男女比例繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Birth'].plot(style='g',ax=ax2,figsize=(10,6))
MF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()

# 離婚-男女比例繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Divorce'].plot(style='c',ax=ax2,figsize=(10,6))
MF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()


# 生育男女繪圖輸出
plt.figure(dpi=240)
gsitesptop10[['Birth_M','Birth_F']].plot(kind='bar',rot=45,align='edge',figsize=(10,6))
# plt.title('', size=25)
plt.xlabel('城市',size=12)
plt.ylabel('人口數',size=12)
plt.show()


# 結婚率-生育男女繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Marry %'].plot(style='r',ax=ax2,figsize=(10,6))
gsitesptop10[['Birth_M','Birth_F']].plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()

print(gsitesptop10[['Birth','Birth_M','Birth_F']])


# 結婚數-生育男女繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Marry'].plot(style='r',ax=ax2,figsize=(10,6))
gsitesptop10[['Birth_M','Birth_F']].plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()



# 生育男女-男女繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Male'].plot(style='c',ax=ax2,figsize=(10,6))
gsitesptop10['Female'].plot(style='m',ax=ax2)
gsitesptop10[['Birth_M','Birth_F']].plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()


# 死亡男女繪圖輸出
plt.figure(dpi=240)
DMF=gsitesptop10[['Death_M','Death_F']]
DMF.plot(kind='bar',rot=45,figsize=(10,6))
# plt.title('', size=25)
plt.xlabel('城市',size=12)
plt.ylabel('人口數',size=12)
plt.show()


# 死亡男女-人口例繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Population'].plot(style='b',ax=ax2,figsize=(10,6))
DMF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()

print(gsitesptop10[['Death','Death_M','Death_F']])

# 死亡男女-出生繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Birth'].plot(style='b',ax=ax2,figsize=(10,6))
DMF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()

# 死亡男女-出生男女繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Birth_M'].plot(style='c',ax=ax2,figsize=(10,6))
gsitesptop10['Birth_F'].plot(style='m',ax=ax2)
DMF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()

# 死亡男女-男女繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Male'].plot(style='c',ax=ax2,figsize=(10,6))
gsitesptop10['Female'].plot(style='m',ax=ax2)
DMF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
plt.show()


# 人口男女-出生男女-死亡男女繪圖輸出
plt.figure(dpi=240)
fig,ax = plt.subplots() 
# fig.suptitle('',size=25)
ax.set_ylabel('人口數',size=12)
ax.set_xlabel('城市',size=12)

ax2 = ax.twinx() # ax.twinx：產生一個新軸
# ax2.set_ylabel('人口數',size=12)

gsitesptop10['Birth_M'].plot(style='c',ax=ax2,figsize=(10,6))
gsitesptop10['Birth_F'].plot(style='r',ax=ax2)
gsitesptop10['Death_M'].plot(style='b',ax=ax2)
gsitesptop10['Death_F'].plot(style='m',ax=ax2)
MF.plot(kind='bar',ax=ax,rot=45)
ax2.legend(loc=1)
ax.legend(loc=2)
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
print('TOP10城市 人口總和 :',sum2,'人')

#TOP10 vs 全台佔比
rate=sum2/sum1*100
print('TOP10 城市佔全台人口比例 : %2.2f' % rate ,'%' )


sumM=0
for j in range(len(gsitesptop10)):
    sumM += gsitesptop10['Male'][j]    
print('TOP10城市 男性人口總和 :',sumM,'人')

sumF=0
for j in range(len(gsitesptop10)):
    sumF += gsitesptop10['Female'][j]    
print('TOP10城市 女性人口總和 :',sumF,'人')


g=gsitesptop10[['Population','Marry','Divorce','Birth','Death']]
print(g)



