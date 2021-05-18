'''一、使用print方式进行分输出（输出目的地是文件）'''
fp=open('f:/实操1（1）.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()

'''方法二，使用文件读写操作'''
with open('f:/实操1（2）.txt','w') as fp:
    fp.write('奋斗成就更好的你')