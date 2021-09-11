import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor as rfr

import scipy.stats as stats

os.system('clear')

data = pd.read_csv('/Users/kang_chanwoong/Desktop/빅 콘테스트/untitled folder/training.csv')
data = data[:2891]

print('','','slope', 'inter', 'r val', 'p val', 'stderr', sep = '\t')
for ch in ['유역평균강수','강우A','강우B','강우C','강우D','수위E','수위D']:
    for i in range(1,7):
        column = str(i) + ch
        x,y = data[[column]],data['유입량']
        train_X, test_X, train_Y, test_Y = train_test_split(x, y, test_size=0.3)

        reg = LinearRegression()
        reg.fit(train_X, train_Y)
        pred_Y = reg.predict(test_X)
        

        plt.scatter(test_X,pred_Y, alpha = 0.5)
        plt.scatter(test_X,test_Y, alpha = 0.5)
        plt.show()