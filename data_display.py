import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os

if '폰트 설정':
    from matplotlib import font_manager, rc
    font_path = "/Users/kang_chanwoong/Desktop/빅 콘테스트/untitled folder/SB 어그로 L.ttf"
    font = font_manager.FontProperties(fname=font_path)

data = pd.read_csv('/Users/kang_chanwoong/BigContest2021/1_hongsu/data/training.csv')
data = data[:2892]

for i in range(1,7):
    col_tail = ['유역평균강수', '강우A', '강우B','강우C', '강우D', '수위E', '수위D']

    for ch in col_tail:
        title = str(i) + ch + '- 유입량 Graph'
        data.plot.scatter(str(i) + ch, '유입량' , s = 5, c = 'green', figsize = (6,6), alpha = 0.3)
        
        plt.xlabel(str(i) + ch, fontproperties=font)
        plt.ylabel('유입량', fontproperties=font)
        plt.title(title, fontproperties=font)

        script_dir = os.path.dirname(__file__)
        date_string = 'Results/'
        results_dir = os.path.join(script_dir, date_string)
        file_name = title + '.png'

        if not os.path.isdir(results_dir): 
            os.makedirs(results_dir)

        plt.savefig(results_dir + file_name, facecolor='#eeeeee')
        plt.close()

data.to_csv('/Users/kang_chanwoong/BigContest2021/1_hongsu/KCW/1. data preprocess/training_date_update.csv')
