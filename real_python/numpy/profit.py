import numpy as np
import matplotlib.pyplot as plt

def profit(prices):
    max_px = 0
    min_px = prices[0]
    for px in prices[1:]:
        min_px = min(min_px,px)
        max_px = max(px-min_px,max_px)
    return max_px
prices = (20,18,14,17,20,21,15)
prices += np.random.randn(len(prices))
print(prices)
print(profit(prices))

#Create mostly NaN array with a few 'turning points'(local min/max).
prices = np.full(100, fill_value=np.nan)
print(prices)
prices[[0,25,60,-1]] =[80.,30.,75.,50.]
print(prices)
# Linearly interpolate the missing values and add some noise.
x = np.arange(len(prices))
print(x)
is_valid = ~np.isnan(prices)
print(is_valid)
prices = np.interp(x=x, xp=x[is_valid], fp=prices[is_valid])
print(x,x[is_valid],prices[is_valid])
print(prices)
prices += np.random.randn(len(prices)) * 2
print (prices)



# Warning ! This isn't a fully correct solution, but it works for nowself.
# If the absolute min came after the absolute max, you'd have touble.
mn = np.argmin(prices)
mx = mn + np.argmin(prices[mn:])

kwargs = {'markersize':12, 'linestyle':''}
fig, ax = plt.subplots()
ax.plot(prices)
ax.set_title('Price History')
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.plot(mn, prices[mn],color='green',**kwargs)
ax.plot(mx, prices[mx], color='red', **kwargs)
