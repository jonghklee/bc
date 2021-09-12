import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import os
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor as rfr
from scipy.optimize import curve_fit

import scipy.stats as stats

def sin_func(x,a):
    return a*x**2

if '폰트 설정':
    from matplotlib import font_manager, rc
    font_path = "/Users/kang_chanwoong/Desktop/빅 콘테스트/untitled folder/SB 어그로 L.ttf"
    font = font_manager.FontProperties(fname=font_path)

os.system('clear')

data = pd.read_csv('/Users/kang_chanwoong/Desktop/빅 콘테스트/untitled folder/training.csv')
data = data[:2891]

x,y = data['1수위E'],data['유입량']
train_X, test_X, train_Y, test_Y = train_test_split(x, y, test_size=0.3)

popt, pcov = curve_fit(sin_func, train_X, train_Y)
regress_sin = lambda x : sin_func(x, popt[0])
pred_Y = pd.Series(map(regress_sin, test_X))

plt.scatter(test_X,pred_Y, s = 3, c = 'green', alpha = 0.9)
plt.scatter(test_X,test_Y, s = 10, c = 'red', alpha = 0.2)

plt.show()