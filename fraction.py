def mul(x,y):
    result = {'s':x['s']*y['s'],'m':x['m']*y['m']}
    return result

def sum(x,y):
    result = {'s':x['s']*y['m']+x['m']*y['s'],'m':x['m']*y['m']}
    return result

def subtraction(x,y):
    result = {'s':x['s']*y['m']-x['m']*y['s'],'m':x['m']*y['m']}
    return result

def  div(x,y):
    result = { 's':x['s']*y['m'],'m':x['m']*y['s']}
    return result



print('aval vared koon 2ta kasr')
s = int(input("vared kon sorat kasr baraye moteghayer avali:"))
m = int(input("vared kon makhrag kasr baraye moteghayer avali:"))
a = {'s':s , 'm':m}


s = int(input("vared kon sorat kasr baraye moteghayer 2vomi:"))
m = int(input("vared kon makhrag kasr baraye moteghayer 2vomi:"))
b = {'s':s , 'm':m}

while True:
    print('entekhab koon amal mored nazar ro az list zir:')
    print('1-mul')
    print('2-sum')
    print('3-subtraction')
    print('4-div')
    print('5-exit')

    choice = int(input('entekhab kon ?:'))
    if choice == 1:
        c = mul(a,b)
        print('zarb 2 ta kasr hast:')
        print(c['s'],'/',c['m'])

    elif choice==2:
        c = sum(a,b)
        print('jame 2 ta kasr hast:')
        print(c['s'],'/',c['m'])

    elif choice ==3:
        c = subtraction(a,b)
        print('tafrighe 2 ta kasr hast:')
        print(c['s'],'/',c['m'])

    elif choice ==4:
        c =div(a,b)
        print('taghsim 2 ta kasr hast:')
        print(c['s'],'/',c['m'])

    elif choice ==5:
        exit()
    else:
        print('vared koon gozineh 2rost az meno :') 


 

