
zimu=['a','v','g']
finish=[]

def send_message(list,hlist):
    while list:
        att=list.pop()
        hlist.append(att)
    print(hlist)

def show_message(list):
    for li in list:
        print(li)


send_message(zimu[:],finish)
show_message(zimu)
