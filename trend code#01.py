import matplotlib.pyplot as plt

def estimate_trend(y, d):
    n = len(y)
    trend = [0]*n
    for t in range(n):
        if d % 2 == 1:  # odd d
            sum_y = sum(y[max(0, t-d//2):min(n, t+d//2+1)])
            count = min(t+1, n-t, d)
        else:  # even d
            sum_y = sum(y[max(0, t-d//2+1):min(n, t+d//2+1)])
            count = min(t+1, n-t, d)
        trend[t] = sum_y / count
    return trend

def estimate_seasonality(y, d, trend):
    n = len(y)
    seasonality = [0]*n
    for t in range(n):
        seasonality[t] = y[t] / trend[t]
    return seasonality

# Example usage:
y = [2011,
2015,
2023,
2013,
2020,
2002,
2024,
1991,
2019,
2024,
2016,
2017,
2005,
1993,
2022,
2010,
2012,
1997,
2009,
2016,
2011,
]
 # Time series data
d = 3  # Number of seasons (odd)
# d = 4  # Number of seasons (even)

trend = estimate_trend(y, d)
seasonality = estimate_seasonality(y, d, trend)
# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(y, label='Original Time Series')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(trend, label='Trend Component')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(seasonality, label='Seasonality Component')
plt.legend()

plt.tight_layout()
plt.show()



