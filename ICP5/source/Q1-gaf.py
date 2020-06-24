import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

data_frame = pd.read_csv('./train.csv')
# print(data_frame['GarageArea'])
# print(data_frame['SalePrice'])
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)
plt.scatter(data_frame['GarageArea'],data_frame['SalePrice'])
plt.show()

filter_data = data_frame[(data_frame['GarageArea'] < 1000) & (data_frame['SalePrice'] < 500000) & (data_frame['GarageArea'] > 400)]
plt1.scatter(filter_data['GarageArea'],filter_data['SalePrice'],color='b')
plt1.show()
