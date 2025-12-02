import pandas as pd
pd.set_option('display.max_columns',None)
data = pd.read_csv('winemag-data-130k-v2.csv')
new_data = data.drop('region_2',axis=1)
new_data = data.dropna(subset=['country'])
mean_price = new_data['price'].sum()/new_data['price'].count()
print(new_data[new_data.price > 300 & (new_data.country == 'Italy')])

