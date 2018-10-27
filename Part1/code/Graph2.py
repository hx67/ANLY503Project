# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 21:29:20 2018

@author: hongx
"""

# import packages

import pandas as pd
from langdetect import detect, DetectorFactory
from collections import Counter
import matplotlib.pyplot as plt

# read the csv file
df = pd.read_csv("music_lyrics.csv")

# remove columns that contains N/A values
df.drop(df.columns[[0, 1]], axis=1, inplace = True)
df1 = df.dropna()
mydf = df1[df1.lyrics != 'No Lyrics']
DetectorFactory.seed = 0

# detect lyrics language types
lang = []
for i in list(set(mydf.lyrics)):
    lang.append(detect(i))

# get the counts for languages of lyrics
Counter(lang)

# Pie chart for English lyrics and lyrics of other languages 
labels = ['English', 'Other languages']
sizes = [3982, 37]

# change figure size with modify figsize
fig, ax1 = plt.subplots(figsize=(8, 8))

# explsion
explode = (0.05,0.05)
ax1.pie(
    sizes, labels=labels, autopct='%1.1f%%', startangle=90, 
    pctdistance=0.55, explode = explode)

#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.title("Pie chart for lyric languages " + "(2008 - 2018)")
fig.savefig("Pie chart for lyric languages (2008 - 2018)")

# Pie chart for English lyrics and lyrics of other languages 
pieLabels = 'es', 'tl', 'ko', 'so', 'cy', 'pt'

numofsongs = [29, 1, 2, 1, 2, 2]

# explsion
explodeTuple = (0.05, 0.0, 0.0, 0.0, 0.0, 0.0,)

# figure
# change figure size with modify figsize
figureObject, axesObject = plt.subplots(figsize=(8, 8))

axesObject.pie(numofsongs, explode=explodeTuple,

        labels=pieLabels,

        autopct='%1.1f',

        startangle=90)

axesObject.axis('equal')
plt.title("Pie chart for lyric languages without English " + "(2008 - 2018)")
figureObject = plt.gcf()
figureObject.savefig(
    "Pie chart for lyric languages without English (2008 - 2018)")