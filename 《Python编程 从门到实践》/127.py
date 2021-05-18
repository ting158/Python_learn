def make_album(singer,name,num=None):
    if num:
        full={'singer':singer.title(),'name':name.title(),'num':num}
        return full
    else:
        full={'singer':singer.title(),'name':name.title()}
        return full

while True:
    sing=input('输入歌手名称（输入p退出）：')
    if sing=='p':
        break
    nam=input('输入专辑名称（输入p退出）：')
    if nam=='p':
        break
    nu=input('输入专辑所含的歌曲数（输入p退出）：')
    if nu=='p':
        break
    else:
        ret=make_album(sing,nam,nu)
        print(ret)