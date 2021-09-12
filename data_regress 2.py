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


if '폰트 설정':
    from matplotlib import font_manager, rc
    font_path = "/Users/kang_chanwoong/Desktop/빅 콘테스트/untitled folder/SB 어그로 L.ttf"
    font = font_manager.FontProperties(fname=font_path)

os.system('clear')

data = pd.read_csv('/Users/kang_chanwoong/Desktop/빅 콘테스트/untitled folder/training.csv')
data = data[:2891]

for ch in ['유역평균강수','강우A','강우B','강우C','강우D','수위E','수위D']:
    for i in range(1,7):
        column = str(i) + ch
        x,y = data[[column]],data['유입량']
        train_X, test_X, train_Y, test_Y = train_test_split(x, y, test_size=0.3)

        reg = LinearRegression()
        reg.fit(train_X, train_Y)
        pred_Y = reg.predict(test_X)

        title = str(i) + ch + '- 유입량 Linear regression Graph'
        plt.scatter(test_X,pred_Y, s = 3, c = 'green', alpha = 0.9)
        plt.scatter(test_X,test_Y, s = 10, c = 'red', alpha = 0.2)
        
        plt.xlabel(str(i) + ch, fontproperties=font)
        plt.ylabel('유입량', fontproperties=font)
        plt.title(title, fontproperties=font)

        script_dir = os.path.dirname(__file__)
        date_string = 'Results/'
        results_dir = os.path.join(script_dir, date_string)
        file_name = 'regress' + title + '.png'

        if not os.path.isdir(results_dir): 
            os.makedirs(results_dir)

        plt.savefig(results_dir + file_name, facecolor='#eeeeee')
        plt.close()