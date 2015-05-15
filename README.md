# catpy

## Quickstart

```bash
$ pip install catpy
```

Let it out of the box...
```
from sklearn.linear_model import LinearRegression
from catpy import cereal

type(cereal)
# CategoricalDataFrame

cereal.head()
reg = LinearRegression()
reg.fit(cdf[['mfr', 'vitamins', 'fat']], cdf.calories)
```

## Installation
You'll need [`pandas`](), but any old version will do the 
trick. There is no `pandas` version pegged in the `setup.py`
file so installing `catpy` won't mess up your existing sci-py
setup.

```bash
$ pip install catpy
```


## Use
Just use it like any old data frame. That's really all there is
to it.

```
import catpy as cp

df = cp.CategoricalDataFrame({
    "x": range(5),
    "y": ["a", "b", "c", "a", "b"]
})


df = pd.read_csv("foo.csv")
cat_df = cp.CategoricalDataFrame(df)
```
