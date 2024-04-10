from scipy import stats
import numpy as np

# Simulating temperature data for a year in a city
temp_data = np.random.normal(loc=30, scale=10, size=365)

# Calculate skewness - this will help understand if the data is symmetric or not
temp_skewness = stats.skew(temp_data)

# Calculate kurtosis - this will help understand presence of extreme values (outliers) in the data
temp_kurtosis = stats.kurtosis(temp_data)

print(f"Temperature Skewness: {temp_skewness:.2f}\nTemperature Kurtosis: {temp_kurtosis:.2f}")

weather_data = np.random.normal(loc=35, scale=10, size=1000)  # A populated weather data (secured from a suitable weather database)

# Compute skewness - representing the direction of skew (departure from horizontal symmetry)
weather_skewness = stats.skew(weather_data)

# Compute kurtosis - shows the height and sharpness of the data at the center
weather_kurtosis = stats.kurtosis(weather_data)

print(f"Weather Data Skewness: {weather_skewness:.2f}\nWeather Data Kurtosis: {weather_kurtosis:.2f}")

temperature_data = np.array([25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35])

# Compute skewness - a measure of data asymmetry
temp_skewness = stats.skew(temperature_data)

# Compute kurtosis - a measure of data "tailedness" or outliers
temp_kurtosis = stats.kurtosis(temperature_data)

print(f"Skewness: {temp_skewness:.2f}\nKurtosis: {temp_kurtosis:.2f}")

# Given temperature data
data = np.array([22.2, 27.5, 24.3, 21.6, 23.1, 26.9, 24.6, 25.4, 23.5, 27.1, 22.5, 24.7])

# TODO: Compute skewness of the data
temperature_skewness = stats.skew(data)

# TODO: Compute kurtosis of the data
temperature_kurtosis = stats.kurtosis(data)

print(f"Skewness: {temperature_skewness:.2f}\nKurtosis: {temperature_kurtosis:.2f}")

# Assume we have temperature data of a city for a year
# TODO: generate data sample

temperature_data = np.random.normal(loc=20, scale=5, size=365)

# Calculate and print skewness to understand if the data is symmetric
temp_skewness = stats.skew(temperature_data)

print(f"Skewness of the temperature data: {temp_skewness:.2f}")

# Calculate and print the kurtosis to understand the presence of outliers
temp_kurtosis = stats.kurtosis(temperature_data)

print(f"Kurtosis of the temperature data: {temp_kurtosis:.2f}")