
import pandas as pd
import os

merged_data = pd.DataFrame()
#当文献数量大于500  cnki必须分批次下载才行，这里是合并成一个大的excel

folder_path = '甘麦大枣'  # Replace with the actual folder path

# Get all the file names in the folder
file_names = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xlsx')]



# file_names = ['file1.xlsx', 'file2.xlsx', 'file3.xlsx']  # Replace with your actual file names

for file_name in file_names:
    # Read the Excel file into a DataFrame
    if file_name.endswith('.xls'):
        data = pd.read_excel(file_name, engine='openpyxl')
    else:
        data = pd.read_excel(file_name)
    
    # Append the data to the merged_data DataFrame
    merged_data = pd.concat([merged_data, data], ignore_index=True)
merged_data.to_excel('文献合并.xlsx', index=False)

#读取合并后的excel，处理关键词成词频形式 方便绘制词云
data=pd.read_excel('甘麦大枣/甘麦大枣-文献导出后的关键词.xlsx')
# 获取关键词列
print()
# print(data[['Keyword-关键词']])
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


        values = keywords[i].split(",")
        for value in values:
            value = value.strip()
            if value in results:
                results[value] += 1
            else:
                results[value] = 1
print(len(keywords))

keywords.to_csv('过滤后的关键词.csv')
df = pd.DataFrame.from_dict(results, orient='index', columns=['Count'])
df.index.name = 'Value'
df.reset_index(inplace=True)
df.to_csv('关键词词频.csv', index=False)


import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Create a string of all the values
text = ' '.join(df['Value'])

# Generate the word cloud
wordcloud = WordCloud().generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
