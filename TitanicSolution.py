#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 20:48:49 2019

@author: adityamishra
"""

##For the data visualisation as centerd plots
from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""");

#%matplotlib inline
import warnings
warnings.filterwarnings('ignore')#Applying warning filter that if warning comes then ignore
warnings.filterwarnings('ignore', category=DeprecationWarning)

import pandas as pd
pd.options.display.max_columns = 100

from matplotlib import pyplot as plt
import numpy as np

import seaborn as sns#For data visualisation

import pylab as plot

params = {
    'axes.labelsize' : "large",
    'xtick.labelsize': "x-large",
    'legend.fontsize': 21,
    'figure.dpi' : 150,
    'figure.figsize' : [25,7]
}
plot.rcParams.update(params)

#loading the training data set

data = pd.read_csv('/Users/adityamishra/data/train.csv')# . signifies the current directory
print(data.shape)

data.head()
data.describe()

data['Age'] = data['Age'].fillna(data['Age'].median())#fillna fills the NaN values with a given number with which we want to substitute
#Checking the result
data.describe()