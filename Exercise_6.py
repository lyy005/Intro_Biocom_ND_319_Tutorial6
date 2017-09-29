# Question 1-method 1-use groupby and apply function 
import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_table("/Users/chenyingying/Documents/Intro_Biocom_ND_319_Tutorial6/UWvMSU_1-22-13.txt")
data['cumulative score']=data.iloc[:,2]
data['cumulative score']=data.groupby('team')['cumulative score'].apply(lambda x: x.cumsum())
# Plot
fig,ax=plt.subplots(figsize=(8,6))
ax.set_xlabel('Time')
ax.set_ylabel('Score')
data.groupby('team')['cumulative score'].plot(legend=True)


# Question 1-method 2-use for loop and if function  
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_table("/Users/chenyingying/Documents/Intro_Biocom_ND_319_Tutorial6/UWvMSU_1-22-13.txt")
data['UWscore']=data.iloc[:,2]
data['UWtemp']=data.iloc[:,2]
data['MSUscore']=data.iloc[:,2]
data['MSUtemp']=data.iloc[:,2]
data.loc[data['team']=='MSU','UWscore']=np.nan
data.loc[data['team']=='MSU','UWtemp']=0
data.loc[data['team']=='UW','MSUscore']=np.nan
data.loc[data['team']=='UW','MSUtemp']=0
data.head(n=10)
for i in range (0,len(data.index)):
    if np.isnan(data.iloc[i,3])==False:
        data.iloc[i,3]=data.iloc[0:i+1,4].sum()
    if np.isnan(data.iloc[i,5])==False:
        data.iloc[i,5]=data.iloc[0:i+1,6].sum()
# Plot
fig,ax=plt.subplots(figsize=(8,6))
ax.set_xlabel('Time')
ax.set_ylabel('Score')
x1=data.loc[np.isfinite(data['UWscore']),'time']
x2=data.loc[np.isfinite(data['MSUscore']),'time']
plt.plot(x1, data['UWscore'].dropna(),label="UW")
plt.plot(x2, data['MSUscore'].dropna(),label="MSU")
plt.legend()


