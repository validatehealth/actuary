"""
Module with helper functions to help with linear regression
"""
import pandas as pd
import numpy as np
from scipy import stats
from sklearn import linear_model

from ..utils.formatting import format_perc


def lm(X, y, sample_weight=None):
    """
    lm

    Enhanced sklearn code for running a linear regression including pandas support and p-values
    Returns a linear model with R^2 automatically calculated as the r2 attribute and T-statistics/p-values as result attribute
    X: A DataFrame containing the independent variables
    y: A ndarray containing the outcome variable
    sample_weight: An optional argument containing sample weights for each row of X
    """
    X_cols = X.columns.tolist()
    X = np.array(X)
    y = y.values.reshape(-1, 1)
    model = linear_model.LinearRegression()
    if sample_weight is not None:
        model.fit(X, y, sample_weight=sample_weight)
    else:
        model.fit(X, y)
    params = np.append(model.intercept_, model.coef_)
    predictions = model.predict(X)
    newX = pd.DataFrame({"Constant":np.ones(len(X))}).join(pd.DataFrame(X))
    MSE = (sum((y-predictions)**2))/(len(newX)-len(newX.columns))
    var_b = MSE*(np.linalg.inv(np.dot(newX.T,newX)).diagonal())
    sd_b = np.sqrt(var_b)
    ts_b = params/ sd_b
    p_values =[2*(1-stats.t.cdf(np.abs(i),(len(newX)-1))) for i in ts_b]
    sd_b = np.round(sd_b,3)
    ts_b = np.round(ts_b,3)
    p_values = np.round(p_values,3)
    params = np.round(params,4)
    result = pd.DataFrame([params, sd_b, ts_b, p_values]).transpose()
    result.columns = ['coef','se','t_val','p_val']
    result.index=['intercept'] + X_cols
    model.result = result
    model.r2 = format_perc(model.score(X, y, sample_weight=sample_weight))
    return model