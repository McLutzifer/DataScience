#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:37:37 2021

@author: lukas
"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# create a line chart, years on x-axis, gdp on y-axis
plt.plot(years, gdp, color='red', marker='x', linestyle = 'dotted')

# add a title
plt.title("Nomnal GDP")

# add a label to the y-axis
plt.ylabel("Billions of $")
plt.show()
