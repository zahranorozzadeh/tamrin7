


def second_to_time(x):
    result = {'h':x['h'] // 3600 ,'m' :x['m'] // 60,'s':x['s']}
    return result



def time_to_second(x):
    result = {'h':x['h'] *3600 ,'m' :x['m'] * 60,'s':x['s']}
    return result    



def sum(x,y):
    result = {'h':x['h']+y['h'],'m':x['m']+y['m'],'s':x['s']+y['s']}
    if result['s']> 59:
        result['m'] += 1
        result['s'] -=60
    if result['m'] >59:
        result['h'] += 1
        result['m'] -= 60

    return result



def subtraction(x,y):
    result = {'h':x['h']-y['h'],'m':x['m']-y['m'],'s':x['s']-y['s']}
    if result['s'] < 0:
        result['m'] -= 1
        result['s'] +=60

    if result['m'] < 0:
        result['h'] -=1
        result['m'] +=60

    return result


while True:
    print('1-jame do zaman')
    print('2-tafrighe do zaman')
    print('3-tabdile saniyeh be zaman')
    print('4- tabdile zaman be saniyeh ')
    print('5-khorog')

    choice = int(input('kodom ro entekhab mikonid?:'))
    if choice == 1:
        h = int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh:"))
        a = {'h':h ,'m':m ,'s':s}

        h = int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh:"))
        b = {'h':h ,'m':m ,'s':s}

        c= sum(a,b)
        print('majmoe in do zaman hast:')
        print(c['h'],':',c['m'],':',c['s'])

    elif choice == 2:
        h = int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh:"))
        a = {'h':h,'m':m ,'s':s}

        h= int(input("vared kon saat:"))
        m = int(input("vared kon daghighe:"))
        s = int(input("vared kon saniyeh"))
        b = {'h':h ,'m':m ,'s':s}

        c= subtraction(a,b)
        print('tafrighe in do zaman hast:')
        print(c['h'],':',c['m'],':',c['s']) 

    elif choice == 3:
        a = int(input('vared kon saniyeh:'))
        c = second_to_time(a)
        print('zaman hast:')
        print(c['h'],':',c['m'],':',c['s'])


    elif choice == 4:
        a = int(input('vared kon saniyeh:'))
        c = time_to_second(a)
        print('zaman hast:')
        print(c['h'],':',c['m'],':',c['s'])



    elif choice ==5:
        exit()
    else:
        print('vared koon gozineh sahih ra az meno')



