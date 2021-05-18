'''会员  >=200  8折
        >=100  9折
        不打折
    非会员  >=200  9.5折
           不打折'''
answer=input('您是会员吗？y/n')
#外层判断是否是会员
pay=float(input('请输入您的商品总价格：'))
if answer==('y'): #会员
    if pay>=200:
        print('打八折，您需要付款', pay*0.8,'元')
    elif pay>=100:
        print('打九折，您需要付款', pay*0.9, '元')
    else:
        print('您需要付款',pay,'元')
else: #非会员
    if pay>=200:
        print('打九五折，您需要付款', pay*0.95, '元')
    else:
        print('您需要付款', pay, '元')