# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:45:53 2024
Week 3: Crowd computing: just estimate

According to the video there is a glass jar of gems containing 300 gems. 75 people were asked to 
estimate the count of gems. After the samples were taken a statistical method called Trimmed Mean 
was used to Guess the Actual number of gems from the samples gathered from the crowd.

@author: Zohaib
"""

#Actual no of gems is 300
import math
from statistics import mean

estimates = [343,322,287,266,331,389,316,308,391,268,332,259,377,359,286,341,368,373,276,385,282,272,346,309,256,311,291,318,256,379,328,332,346,285,366,288,329,356,311,320,303,304,319,300,295,290,302,258,295,281,353,387,346,324,379,264,299,331,308,384,492,748,445,681,729,605,511,116,172,122,215,132,231,223,166]
estimates.sort()
trimlen = math.floor(0.1*len(estimates))

estimates = estimates[trimlen:]
estimates = estimates[:len(estimates)-trimlen]
print(mean(estimates))



