def moving_average(d,extra_periods=1,n=3):
    d=np.array(d)
    cols=len(d)
    d=np.append(d,[np.nan]*extra_periods)
    f=np.full(cols+extra_periods,np.nan)
    for t in range(n,cols+1):
        f[t]=np.mean(d[t-n:t])
    f[cols+1:]=f[t]
    df=pd.DataFrame.from_dict({"Demand" :d,"Forecast":f,"Erro":d-f})
    return df

import pandas as pd
import numpy as np

d =[28,19,18.13,19,16,19,18,13,16,16,11,18,15,13,15,13,11,13,10,12]
df = moving_average(d)

df[["Demand","Forecast"]].plot()

df[["Demand","Forecast"]].plot(figsize=(8,3),title="Moving Average",ylim=(0,30),style=["-","--"])


