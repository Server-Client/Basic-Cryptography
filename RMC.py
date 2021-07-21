x = input('Type String: ')
y = input('Character to Replace & Character to Replace with (ex: e,r.r,t.h,x): ')
z = y.split('.')
w = str(z).replace("'", "").replace('[', '').replace(']', '').replace(',', '')
u = w.replace(' ', '')
v = len(u)/2
if v == 2.0:
    a,b,c,d = u
    print(x.replace(a,b).replace(c,d))

elif v == 3.0:
    a,b,c,d,e,f = u
    print(x.replace(a,b).replace(c,d).replace(e,f))

elif v == 4.0:
    a,b,c,d,e,f,g,h = u
    print(x.replace(a,b).replace(c,d).replace(e,f).replace(g,h))

elif v == 5.0:
    a,b,c,d,e,f,g,h,i,j = u
    print(x.replace(a,b).replace(c,d).replace(e,f).replace(g,h).replace(i,j))
