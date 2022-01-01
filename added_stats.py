# print("Hello World!")

# plotly standard imports
import plotly.graph_objs as go
import chart_studio.plotly as py

# Cufflinks wrapper on plotly
import cufflinks

# Data science imports
import pandas as pd
import numpy as np

# Options for pandas
pd.options.display.max_columns = 999

# Display all cell outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

# from __future__ import print_function, division
import matplotlib as mpl
import matplotlib.pyplot as plt


from plotly.offline import iplot
cufflinks.go_offline()

# Set global theme
cufflinks.set_config_file(world_readable=True, theme='pearl')

# Get slugging percentages from Batting data
slugpct = pd.read_csv("https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/Batting.csv",sep=',')
# Get batters who are sluggers from People data
slugppl = pd.read_csv("https://raw.githubusercontent.com/chadwickbureau/baseballdatabank/master/core/People.csv",sep=',')

# print(slugpct)
# print("Hello World! Py file")

sluggers = slugpct.to_numpy()

# Print players from San Francisco Giants - Buster Posey
# Did not play in 2020 due to COVID-19 pandemic, opted out
# 2021 stats: https://www.baseball-reference.com/players/p/poseybu01.shtml

posey_stats = [None] * 11
counter = 0
posey_hr = [None] * 11
posey_yr = [None] * 11
posey_ba = [None] * 11

for a in sluggers:
    if a[0] == 'poseybu01':
        posey_stats[counter] = a
        posey_hr[counter] = a[12]
        posey_yr[counter] = a[1]
        posey_ba[counter] = a[8] / a[6]
        # print(a)
        counter += 1
        

# posey_yr = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]


plt.bar(posey_yr, posey_hr)
plt.title("Buster Posey HR Count, 2009-2019")
plt.xlabel("Season of Play")
plt.ylabel("Home Runs Hit")
plt.show()


plt.plot(posey_yr, posey_ba)
plt.title("Buster Posey Batting Average, 2009-2019")
plt.xlabel("Season of Play")
plt.ylabel("Batting Average")
plt.show()


