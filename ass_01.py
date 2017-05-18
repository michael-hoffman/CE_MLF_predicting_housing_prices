import graphlab
import matplotlib.pyplot as plt

sales = graphlab.SFrame('home_data.gl/')

train_data, test_data = sales.random_split(.8, seed=0)

"""
1. Selection and summary statistics: In the notebook we covered in the module, we discovered which neighborhood 
(zip code) of Seattle had the highest average house sale price. Now, take the sales data, select only the houses with 
this zip code, and compute the average price. Save this result to answer the quiz at the end.
"""

nice_zip = sales[sales['zipcode'] == '98039']

print('Fancy zip average price: %d' % nice_zip['price'].mean())
# result: 2160606.6

"""
2. Filtering data: One of the key features we used in our model was the number of square feet of living space 
('sqft_living') in the house. For this part, we are going to use the idea of filtering (selecting) data.

In particular, we are going to use logical filters to select rows of an SFrame. You can find more info in the Logical 
Filter section of this documentation.Using such filters, first select the houses that have 'sqft_living' higher than 
2000 sqft but no larger than 4000 sqft.What fraction of the all houses have 'sqft_living' in this range? Save this 
result to answer the quiz at the end.
"""

big_houses = sales[2000 < sales['sqft_living']]
fraction = len(big_houses)/float(len(sales))
print('fraction: %d' % fraction)
