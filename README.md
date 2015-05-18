# dummipy

## Quickstart

```bash
$ pip install dummipy
```

Let it out of the box...
```
from sklearn.linear_model import LinearRegression
from dummipy import cereal

type(cereal)
# CategoricalDataFrame

cereal.head()
reg = LinearRegression()
reg.fit(cereal[['mfr', 'vitamins', 'fat']], cereal.calories)
```

## Installation
You'll need [`pandas`](http://pandas.pydata.org/), but any old version will do 
the trick. There is no `pandas` version pegged in the `setup.py` file so 
installing `dummipy` won't mess up your existing sci-py setup.

```bash
$ pip install dummipy
```


## Use
Just use it like any old data frame. That's really all there is to it.

```
import dummipy as dp

df = dp.CategoricalDataFrame({
    "x": range(5),
    "y": ["a", "b", "c", "a", "b"]
})


df = pd.read_csv("foo.csv")
df = dp.CategoricalDataFrame(df)
```
