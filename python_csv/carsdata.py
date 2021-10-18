# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:13:18 2021

@author: ZeRoyale
"""

#%%

import pandas as pd

cars_table = pd.read_html("https://en.wikipedia.org/wiki/Comma-separated_values")
cars_table[1] 

carsdata_csv = cars_table[1]
carsdata_csv.to_csv("carsdatatable.csv")

#%%