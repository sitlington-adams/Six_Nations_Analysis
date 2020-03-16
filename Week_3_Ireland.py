#!/usr/bin/env python
# coding: utf-8

# # Week 3 - England v Ireland
# ## Visualize data

# ### Import libraries

# In[2]:


# WHAT THIS DOES
# Loads in the matplotlib and seaborn libraries that are used to create charts in python

import pandas as pd
import matplotlib.pyplot as pit
import seaborn as sb


# In[24]:


#WHAT THIS DOES
#Sets up notebook for data visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
pit.rcParams["figure.figsize"] = 19,9 # defines the size of the figure (in inches)
sb.set_style("dark")


# ### Load and tidy up the data

# In[6]:


# WHAT THIS DOES
# Selects the spreadsheet you'd like to analyse
# This week, we're telling Python: 'please order this data by the column called 'Date' which represents a time' 
address = r"C:\Users\RMAda\PycharmProjects\SixNations Analysis\Week_3_Ireland-20200224T161046Z-001\Week_3_Ireland\Starter_Materials\Ireland_Rugby_Data.csv"
ireland = pd.read_csv(address, index_col = "Date", parse_dates = True)
ireland.tail(30)


# In[ ]:





# In[12]:


#WHAT THIS DOES
#Let's you drop columns you don't need
ireland_clean = ireland.drop(["HTf", "HTa", "Unnamed: 7", "Unnamed: 11"], axis=1)
ireland_clean.columns = ["Team", "Result", "For", "Aga", "Diff", "Opposition", "Ground"]
ireland_clean.tail(5)


# ###  Select rows
# #### _6N matches at Twickenham in the professional era_

# In[14]:


#WHAT THIS DOES
#Keeps rows from 1995
ireland_prof = ireland_clean.loc["1995-01-21": , :]
ireland_prof


# In[16]:


# WHAT THIS DOES 
# Creates a dataframe that only includes the 6N matches
ireland_6N = ireland_prof.drop(pd.to_datetime(["2019-08-24","2015-09-05","2011-08-27","2001-10-20",]))
ireland_6N


# In[17]:


# WHAT THIS DOES 
# Creates a dataframe that only includes the home matches
ireland_twickenham = ireland_6N[ireland_6N.Ground == "Twickenham"]
ireland_twickenham


# ### Chart the data

# In[25]:


# WHAT THIS DOES
# Draws the chart
# Uses object orientated method of charting

# Creates the canvas to draw the chart
fig = pit.figure()
ax = fig.add_axes([.1, .1, 1, 1])

x = ireland_twickenham.index
y = ireland_twickenham["Diff"]

#Draws the chart

ax.plot(x,y,color="seagreen", marker = "o", linestyle="dashed", linewidth=2, markersize=12)

#set tickmarks

ax.set_xticks(x)

#Labels the axes

ax.set_title("Points difference between England and Ireland")
ax.set_xlabel("Year")
ax.set_ylabel("Points")

#Saves the plot in the working directory

pit.savefig("ireland_bar_chart.png", bbox_inches="tight")


# In[23]:


#WHAT THIS DOES
#tells you where the working directory is in case you've forgotten
get_ipython().run_line_magic('pwd', '')


# ## Useful links

# If you'd like to explore further what we've learned this week, here are some useful links:
# 
# - [Seaborn](https://seaborn.pydata.org/)
# - [matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html)
# - [seaborn.set_style](https://seaborn.pydata.org/generated/seaborn.set_style.html)
# - [Data School - Pandas Index](https://www.youtube.com/watch?v=OYZNk7Z9s6I)
# - [Matplotlib colour](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)
