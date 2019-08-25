import numpy as np
import pandas as pd

sample = {}
feature = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V9', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V18', 'V19']

dev = pd.read_csv('./creditcard.csv')
data = {"id":[],"x0":[],"x1":[],"x2":[],"x3":[],"x4":[],"x5":[],"x6":[],"x7":[]}
data_b = {"id":[], "y":[],"x0":[],"x1":[],"x2":[],"x3":[],"x4":[],"x5":[],"x6":[],"x7":[]}

for i in range(len(dev)):
    if int(dev.iloc[i]['Class'])==1:
        data["id"].append(i)

        data_b["id"].append(i)
        data_b["y"].append(int(dev.iloc[i]['Class']))

        key = list(data.keys())
        for idx, k in enumerate(key[1:]):
            data[k].append(dev.iloc[i][feature[idx-1]])
            data_b[k].append(dev.iloc[i][feature[idx +7]])

    elif i%560==0:
        data["id"].append(i)
        data_b["id"].append(i)
        data_b["y"].append(int(dev.iloc[i]['Class']))

        key = list(data.keys())
        for idx, k in enumerate(key[1:]):
            data[k].append(dev.iloc[i][feature[idx - 1]])
            data_b[k].append(dev.iloc[i][feature[idx + 7]])

train = pd.DataFrame(data, columns=["id","x0","x1","x2","x3","x4","x5","x6","x7"])
train_b = pd.DataFrame(data_b, columns=["id","y","x0","x1","x2","x3","x4","x5","x6","x7"])

train.to_csv(r'C:\Users\hengtao_t\Desktop\FATE\fate-data\my_data_a.csv',encoding='gbk',index=None)
train_b.to_csv(r'C:\Users\hengtao_t\Desktop\FATE\fate-data\my_data_b.csv',encoding='gbk',index=None)

