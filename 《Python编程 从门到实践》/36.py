dinner=['a','b','c']
print(f'邀请{dinner[0]},{dinner[1]},{dinner[2]}共进晚餐')
print(f'{dinner[2]}无法赴约')
dinner[2]='d'
print(f'邀请{dinner[0]},{dinner[1]},{dinner[2]}共进晚餐')
print('找到了更大的餐桌')
dinner.insert(0,'e')
dinner.insert(2,'f')
dinner.append('g')
print(f'邀请{dinner[0]},{dinner[1]},{dinner[2]},{dinner[3]},{dinner[4]},{dinner[5]}共进晚餐')
print('大餐桌无法及时送达，只能邀请两名')
l5=dinner.pop(5)
print(f'{l5},很抱歉，无法邀请你来共进晚餐')
l4=dinner.pop(4)
print(f'{l4},很抱歉，无法邀请你来共进晚餐')
l3=dinner.pop(3)
print(f'{l3},很抱歉，无法邀请你来共进晚餐')
l2=dinner.pop(2)
print(f'{l2},很抱歉，无法邀请你来共进晚餐')
print(f'{dinner[0]}你依然在受邀人之列')
print(f'{dinner[1]}你依然在受邀人之列')
len=len(dinner)
print(f'邀请了{len}位嘉宾共进晚餐')
del dinner[1]
del dinner[0]
print(dinner)