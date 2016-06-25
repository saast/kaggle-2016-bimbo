import pandas as pd


train_data_filename = 'data/train.csv'


#train_n = sum(1 for line in open(train_data_filename))
#print(train_n)
# 74 180 465


chunksize = 1000000
df_train = []
for df_train_part in pd.read_csv(train_data_filename, chunksize=chunksize):
	df_train.append(df_train_part[df_train_part['Producto_ID'] == 30314])

df_train = pd.concat(df_train)

print(len(df_train))

