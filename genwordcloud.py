data=pd.read_excel('无人机-文献合并.xlsx')
# 获取关键词列
print()
data['Keyword-关键词'] = data['Keyword-关键词'].astype(str)
keywords = data['Keyword-关键词']

# 定义特殊字符列表
special_characters = ['！', '@', '＃', '$', '％', '^', '＆', '*', '（', '）', '_', '+', '{', '}', '：“', '<', '>', '？', '|', '\\', '[', ']', ';', "'", '，', '。', '/', '：“']
results = {}

# 遍历关键词并替换全角字符为半角字符
for i in range(len(keywords)):

    if type(keywords[i])==str:

        # for char in special_characters:
        #     if char in keywords[i]:
        #         keywords[i] = keywords[i].replace(char, char.encode('ascii', 'ignore').decode('ascii'))
        keywords[i] = keywords[i].replace(';', ',')
        keywords[i] = keywords[i].replace('；', ',')
        keywords[i] = keywords[i].replace('，', ',')        
        keywords[i] = keywords[i].replace('、', ',')


        keywords[i] = keywords[i].replace('／', ',')

        keywords[i] = keywords[i].replace('/', ',')
        keywords[i] = keywords[i].replace('%', '')
        keywords[i] = keywords[i].replace('@', '')
        keywords[i] = keywords[i].replace('"', '')
        # keywords[i] = keywords[i].replace('合', ',')
        # keywords[i] = keywords[i].replace('加味', '')


        values = keywords[i].split(",")
        for value in values:
            value = value.strip()
            if value is None or value =='':
                pass
            else:
                if value in results:
                    results[value] += 1
                else:
                    results[value] = 1
print(len(keywords))


keywords.to_csv('无人机-过滤后的关键词.csv')
df = pd.DataFrame.from_dict(results, orient='index', columns=['Count'])
df.index.name = 'Value'
df.reset_index(inplace=True)
df.to_csv('无人机/关键词词频.csv', index=False)

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from collections import Counter

word_cloud_lst = Counter(keywords)

# 生成词云
wordcloud = WordCloud(font_path='simhei.ttf',max_font_size=50, max_words=100, background_color="white").generate_from_frequencies(word_cloud_lst)


# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
