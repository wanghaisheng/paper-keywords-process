
import pandas as pd
import os

merged_data = pd.DataFrame()


# folder_path = '甘麦大枣'  # Replace with the actual folder path
# keyword='甘麦大枣'

folder_path = r'D:\workspace\无人机\xlsx'  # Replace with the actual folder path
keyword='无人机'




# Get all the file names in the folder
file_names = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xlsx') or file.endswith('.xls')]



# file_names = ['file1.xlsx', 'file2.xlsx', 'file3.xlsx']  # Replace with your actual file names

for file_name in file_names:
    # Read the Excel file into a DataFrame
    if file_name.endswith('.xls'):
        data = pd.read_excel(file_name,engine='calamine')
    else:
        data = pd.read_excel(file_name)
    
    # Append the data to the merged_data DataFrame
    merged_data = pd.concat([merged_data, data], ignore_index=True)
merged_data.to_excel(f'{keyword}-文献合并.xlsx', index=False)

