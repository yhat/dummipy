import pandas as pd
import inspect

        
class CategoricalDataFrame(pd.DataFrame):
    """
    A CategoricalDataFrame is the same as a regular DataFrame, except
    if you pass it to a scikit-learn function, it will automatically
    dummify categorical variables.

    Parameters
    ----------
    data : numpy ndarray (structured or homogeneous), dict, or DataFrame
        Dict can contain Series, arrays, constants, or list-like objects
    index : Index or array-like
        Index to use for resulting frame. Will default to np.arange(n) if
        no indexing information part of input data and no index provided
    columns : Index or array-like
        Column labels to use for resulting frame. Will default to
        np.arange(n) if no column labels are provided
    dtype : dtype, default None
        Data type to force, otherwise infer
    copy : boolean, default False
        Copy data from inputs. Only affects DataFrame / 2d ndarray input

    Examples
    --------
    >> regular_df = pd.DataFrame({
        "a": np.random.choice(["a", "b", "c"], 100),
        "x": np.arange(100) + np.random.normal(0, 1, 100),
        "y": np.arange(100)
    })
    >>> cat_df = CategoricalDataFrame({
    ...     "a": np.random.choice(["a", "b", "c"], 100),
    ...     "x": np.arange(100) + np.random.normal(0, 1, 100),
    ...     "y": np.arange(100)
    ... })
    >>> r = LinearRegression()
    >>> try:
    ...    r.fit(regular_df[['a', 'x']], regular_df.y)
    ... except Exception, e:
    ...     print "Error when running with normal data frame: ", e
    # Error when running with normal data frame:  could not convert string to float: c
    >>> print "Result when running with CategoricalDataFrame:"
    >>> print "\t", r.fit(cat_df[['a', 'x']], cat_df.y)
    # Result when running with CategoricalDataFrame:
    #   LinearRegression(copy_X=True, fit_intercept=True, normalize=False)

    See also
    --------
    DataFrame
    """

    @property
    def _constructor(self):
        """
        This makes all of pandas functions that return `self`, return a CategoricalDataFrame
        instead of a DataFrame.
        """
        return CategoricalDataFrame

    def __getitem__(self, keys):
        # amazing, I know. this is the key to everything. check and see what is
        # calling the getter (__getitem__ is invoked when you slice pandas. this
        # means df['foo'] or df[['a', 'b', 'c']]). once we know what code is calling
        # the getter, we take a look at it and see if it's wrapped in a `fit` or `transform`
        for item in inspect.stack():
            source = item[4]
            if source and len(source) > 0:
                source = source[0]
                if ".fit(" in source or ".transform(" in source:
                    return self._get_dummied(keys)
        else:
            return CategoricalDataFrame(super(CategoricalDataFrame, self).__getitem__(keys))

    def __array__(self, dtype=None):
        data = self._get_dummied()
        return pd.lib.values_from_object(data)

    def _get_dummied(self, keys=None):
        if keys is None:
            keys = self.columns

        data = super(CategoricalDataFrame, self).__getitem__(keys)
        if isinstance(data, pd.Series):
            return data

        new_keys = []
        if isinstance(keys, str):
            keys = [keys]
        for k in keys:
            if super(CategoricalDataFrame, self).__getitem__(k).dtype=="object":
                k_dummies = pd.get_dummies(super(CategoricalDataFrame, self).__getitem__(k))
                col_idx = k_dummies.columns[1:]
                for col in col_idx:
                    tmp_col = "%s(%s)" % (k, col)
                    data[tmp_col] = k_dummies[col]
                    new_keys.append(tmp_col)
            else:
                new_keys.append(k)

        return super(CategoricalDataFrame, data).__getitem__(new_keys)
