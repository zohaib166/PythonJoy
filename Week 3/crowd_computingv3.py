# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:45:53 2024
Week 3: Crowd computing: just estimate Version 2

According to the video there is a glass jar of gems containing 300 gems. 75 people were asked to 
estimate the count of gems. After the samples were taken a statistical method called Trimmed Mean 
was used to Guess the Actual number of gems from the samples gathered from the crowd.

This program plot the estimate as well

@author: Zohaib
"""

#Actual no of gems is 300


from statistics import mean, median
from scipy import stats
import math
import matplotlib.pyplot as plt


estimates = [343,322,287,266,331,389,316,308,391,268,332,259,377,359,286,341,368,373,276,385,282,272,346,309,256,311,291,318,256,379,328,332,346,285,366,288,329,356,311,320,303,304,319,300,295,290,302,258,295,281,353,387,346,324,379,264,299,331,308,384,492,748,445,681,729,605,511,116,172,122,215,132,231,223,166]
estimates.sort()

m1 = mean(estimates)
m2 = median(estimates)

trimlen = math.floor(0.1*len(estimates))
estimates = estimates[trimlen:]
estimates = estimates[:len(estimates)-trimlen]

y = []
for i in range(len(estimates)):
    y.append(10)
m3 = stats.trim_mean(estimates,0.1)
plt.plot(estimates,y,"r--")
plt.plot([m1],[10],"g*")
plt.plot([m2],[10],"b*")
plt.plot([m3],[10],"k*")


