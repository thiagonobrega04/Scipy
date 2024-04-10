import numpy as np
from scipy.stats import stats

# Simulating temperature data for a year in a city
temp_data = np.random.normal(loc=30, scale=10, size=365) # para gerar exemplos randômicos de dados, podemos usar o comando numpy.random
# In this scenario, we generate an array of 365 values, which are normally distributed with mean=30 and std=10. Note, that in numpy random, loc stands for mean, and scale stands for std.

data = np.random.normal(size=1000)

# Compute skewness - a measure of data asymmetry
data_skewness = stats.skew(data)

# Compute kurtosis - a measure of data "tailedness" or outliers
data_kurtosis = stats.kurtosis(data)

print(f"Skewness: {data_skewness}\nKurtosis: {data_kurtosis}")