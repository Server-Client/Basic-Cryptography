x = input('Type String Here: ')
y = input('Character to Replace & Character to Replace with (ex: e,r): ')
z = y.split(',', 1)
a,b = z
print(x.replace(a, b))
