#列出指定目录下的所有py文件
import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    if filename.endswith('py'):
        print(filename)