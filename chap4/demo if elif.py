'''多分支结构，多选一执行
从键盘录入一个整数成绩
90-100  A
80-89   B
70-79   C
60-69   D
0-59    E
小于0或大于100为非法数据（不是成绩的有效范围）
'''
score=float(input('请输入一个成绩：'))
if 90<=score<=100:  #Python独特写法  一般为  score>=90 and score<=100
    print('A')
elif 80<=score<=89:
    print('B')
elif 70<=score<=79:
    print('C')
elif 60<=score<=69:
    print('D')
elif 0<=score<=59:
    print('E')
else:
    print('对不起，成绩有误，不在成绩的有效范围')