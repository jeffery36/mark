import pandas as pd
import os
print(os.getcwd())

df1 = pd.read_csv('./hate_sampling_tomato.csv', encoding = 'utf-8-sig')
df2 = pd.read_csv('./hate_sampling2.csv', encoding = 'utf-8-sig')

df3 = pd.concat([df1, df2], axis=0)

df3.to_csv('hate_sampling_neww.csv', encoding = 'utf-8-sig')