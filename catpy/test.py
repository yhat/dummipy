import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

from catpy import CategoricalDataFrame

regular_df = pd.DataFrame({
    "a": np.random.choice(["a", "b", "c"], 100),
    "x": np.arange(100) + np.random.normal(0, 1, 100),
    "y": np.arange(100)
})

cat_df = CategoricalDataFrame({
    "a": np.random.choice(["a", "b", "c"], 100),
    "x": np.arange(100) + np.random.normal(0, 1, 100),
    "y": np.arange(100)
})

r = LinearRegression()
r = RidgeCV()

# try:
#     r.fit(regular_df[['a', 'x']], regular_df.y)
# except Exception, e:
#     print "Error when running with normal data frame: ", e

# print "Reuslt when running with CategoricalDataFrame:"
# print "\t", r.fit(cat_df[['a', 'x']], cat_df.y)


print type(cat_df)
# d = cat_df[['a', 'x']].head()
d = cat_df[['a', 'x']].tail()
y = cat_df.y
print type(d)
data = d
print y
print r.fit(data, y.head())
print r.fit(cat_df[['a']], y)
print r.fit(cat_df[['a', 'x']], y)