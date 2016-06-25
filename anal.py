import pandas as pd
import sys
import pickle


train_data_filename = 'data/train.csv'


#train_n = sum(1 for line in open(train_data_filename))
#print(train_n)
train_full_n = 74180465

print(train_full_n)
print('kala')

def read_train_from_csv(product_id):
    chunksize = 1000000
    df_train = []
    for df_train_part in pd.read_csv(train_data_filename, chunksize=chunksize):
        df_train.append(df_train_part[df_train_part['Producto_ID'] == product_id])
        print(len(df_train_part['Producto_ID'].unique()))

    df_train = pd.concat(df_train)

    # Save selected data
    with open('vars/df_train.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(df_train, f, pickle.HIGHEST_PROTOCOL)


def read_train_from_picklefile():
# Read selected data
    with open('vars/df_train.pickle', 'rb') as f:
        df_train = pickle.load(f)
    return df_train


def read_products_from_csv():
    products  =  pd.read_csv("data/producto_tabla.csv")
    products['short_name'] = products.NombreProducto.str.extract('^(\D*)', expand=False)
    products['brand'] = products.NombreProducto.str.extract('^.+\s(\D+) \d+$', expand=False)
    w = products.NombreProducto.str.extract('(\d+)(Kg|g)', expand=True)
    products['weight'] = w[0].astype('float')*w[1].map({'Kg':1000, 'g':1})
    products['pieces'] =  products.NombreProducto.str.extract('(\d+)p ', expand=False).astype('float')

    print(products.head())

    with open('vars/products.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(products, f, pickle.HIGHEST_PROTOCOL)

def read_products_from_pickle():
# Read selected data
    with open('vars/products.pickle', 'rb') as f:
        products = pickle.load(f)
    return products

#read_train_from_csv()
#df_train = read_train_from_picklefile()
#print(df_train.head())
#print(df_train.describe())

#read_products_from_csv()
products = read_products_from_pickle()
print(products.describe())
print(products.info())
print(products.iloc[1])
print(len(products))


