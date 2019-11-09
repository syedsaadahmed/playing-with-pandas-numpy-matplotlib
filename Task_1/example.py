import pandas as pd
import csv
import matplotlib.pyplot as plt
import math

df=pd.read_csv("dataset.csv")
df.sort_values('time_in_seconds',inplace=True)
# plt.scatter(df.index,df.time_in_seconds,s=2)
# plt.xlabel("Index of URL")
# plt.ylabel("Time in seconds")
# plt.suptitle('Time Distribution of dataset.csv', fontsize=22)
# plt.show()



# count_row = math.floor(df.shape[0]*0.2)
# df.drop(df.tail(count_row).index,inplace=True) # drop last n rows
# plt.scatter(df.index,df.time_in_seconds,s=4)
# plt.suptitle('Time Distribution of dataset.csv after 20 percent reduction', fontsize=22)
# plt.show()



columns = ['time_in_seconds']
df = df.replace(0, pd.np.nan).dropna(axis=0, how='any', subset=columns).fillna(0)
df.sort_values('time_in_seconds',inplace=True)
plt.scatter(df.index,df.time_in_seconds,s=2)
plt.suptitle('Time Distribution of dataset.csv after time_in_seconds 0 removal', fontsize=22)
plt.show()
